import os.path
import json
from argparse import ArgumentParser
from itertools import chain


def parse_db(db_path, pos):
    with open(os.path.join(db_path, "data.{}".format(pos)), "r") as f:
        raw_index = f.readlines()[29:]

    for r in raw_index:
        buff = r.strip().split(" ")
        (word_id, _, _, ref_count, word, postfix, *other) = buff
        data = {
            "pos": pos,
            "wordnet_id": word_id,
            "word": word,
            "key": "{}_{}".format(word, ref_count),
            "synonyms": [other[i] for i in range(0, int(ref_count, 16) - 1, 2)]
        }
        yield data

def main(args):
    path = args.db_path
    results = sorted(chain(parse_db(path, "adv"), parse_db(path, "adj"), parse_db(path, "noun"), parse_db(path, "verb")), key=lambda o: o["word"])
    with open(args.output, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--db_path", help="Directory where wordnet data files are located", default=".")
    parser.add_argument("output", help="Output file, jsonl extension")
    main(parser.parse_args())