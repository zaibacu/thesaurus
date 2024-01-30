import json
import logging
import os.path
from argparse import ArgumentParser
from collections import defaultdict
from itertools import chain

logger = logging.getLogger(__name__)

POS_MAP = {
    "n": "noun",
    "v": "verb",
    "a": "adjective",
    "s": "adjective satellite",
    "r": "adverb",
}


ref_count = defaultdict(int)


def parse_db(db_path, pos):
    with open(os.path.join(db_path, "data.{}".format(pos)), "r") as f:
        raw_data = f.readlines()[29:]

    with open(os.path.join(db_path, "index.{}".format(pos)), "r") as f:
        raw_index = f.readlines()[29:]

    linked_synonyms = defaultdict(lambda: set())
    for r in raw_index:
        buff = r.strip().split(" ")
        n = len(buff)
        (lemma, _, synset_cnt, *other) = buff
        refs = buff[n - int(synset_cnt) :]
        word = lemma

        logger.debug("Raw index line: {0}".format(list(enumerate(buff))))
        logger.debug("Word: {0}, Refs: {1}".format(word, refs))
        for r in refs:
            linked_synonyms[r].add(lemma)

    matched = set()
    for r in raw_data:
        (data, gloss) = r.strip().split("|")
        buff = data.strip().split(" ")
        logger.debug("Raw line: {0}".format(buff))
        (word_id, _, _, _, word, postfix, *other) = buff

        synset = linked_synonyms[word_id] - set([word])
        ref_count[word] += 1
        data = {
            "pos": pos,
            "wordnet_id": word_id,
            "word": word,
            "key": "{}_{}".format(word, ref_count[word]),
            "synonyms": list(synset),
            "desc": [g.strip() for g in gloss.split(";")],
        }
        logger.debug("Parsed line: {0}".format(data))
        matched.add(word_id)
        yield data


def main(args):
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    path = args.db_path
    results = sorted(
        chain(
            parse_db(path, "adv"),
            parse_db(path, "adj"),
            parse_db(path, "noun"),
            parse_db(path, "verb"),
        ),
        key=lambda o: o["key"],
    )
    with open(args.output, "w") as f:
        for r in results:
            if not args.noop:
                f.write(json.dumps(r) + "\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--db_path",
        "--db-path",
        help="Directory where wordnet data files are located",
        default=".",
    )
    parser.add_argument(
        "--debug", action="store_true", default=False, help="Show debug output"
    )
    parser.add_argument(
        "--noop",
        action="store_true",
        default=False,
        help="Don't write output to file. Use for debugging purposes",
    )
    parser.add_argument("output", help="Output file, jsonl extension")
    main(parser.parse_args())

