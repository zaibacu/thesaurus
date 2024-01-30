# thesaurus
Offline database of synonyms/thesaurus

# Format
It follows `jsonl` format - meaning, that each line is a separate `json` document.
It contains:
```
word: (String) Actual word
wordnet_id: (String) internal wordnet reference
key: (String) Some words can have multiple meanings. Each meaning will have same word, but different key.
pos: (String) part of speech tag, eg. `noun`, `verb`
synonyms: (Array of String) synonyms related to this key
desc: (Array of String)  description of word
```


# Languages

## English

File: `en_thesaurus.jsonl`

It's an extration out of [WordNet](https://wordnet.princeton.edu). Refer to [WordNet License](https://wordnet.princeton.edu/license-and-commercial-use) for usage. As of today:

```
License and Commercial Use of WordNet

WordNet® is unencumbered, and may be used in commercial applications in accordance with the following license agreement. An attorney representing the commercial interest should review this WordNet license with respect to the intended use.

WordNet License

This license is available as the file LICENSE in any downloaded version of WordNet.

WordNet 3.0 license: (Download)

WordNet Release 3.0 This software and database is being provided to you, the LICENSEE, by Princeton University under the following license. By obtaining, using and/or copying this software and database, you agree that you have read, understood, and will comply with these terms and conditions.: Permission to use, copy, modify and distribute this software and database and its documentation for any purpose and without fee or royalty is hereby granted, provided that you agree to comply with the following copyright notice and statements, including the disclaimer, and that the same appear on ALL copies of the software, database and documentation, including modifications that you make for internal use or for distribution. WordNet 3.0 Copyright 2006 by Princeton University. All rights reserved. THIS SOFTWARE AND DATABASE IS PROVIDED "AS IS" AND PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES OF MERCHANT- ABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE LICENSED SOFTWARE, DATABASE OR DOCUMENTATION WILL NOT INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS OR OTHER RIGHTS. The name of Princeton University or Princeton may not be used in advertising or publicity pertaining to distribution of the software and/or database. Title to copyright in this software, database and any associated documentation shall at all times remain with Princeton University and LICENSEE agrees to preserve same.

```

### Tool to update data

`wordnet_extract.py` can be run without any additional dependencies, Python3.6+ is required to be able to execute it

It parses WordNet database and creates `.jsonl` file.

English database can be found: [WordNet](https://wordnet.princeton.edu/download)

If any other language strictly follows same format, it should work as well.

Usage:
```
usage: wordnet_extract.py [-h] [--db_path DB_PATH] output

positional arguments:
  output             Output file, jsonl extension

optional arguments:
  -h, --help         show this help message and exit
  --db_path DB_PATH  Directory where wordnet data files are located
```


