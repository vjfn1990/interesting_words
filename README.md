# Interesting Words

## Parameters to be modified on the file 'main.py'

'words_to_retrieve' and 'files_path' should be modified, in order to execute the solution successfully.

In order to be able to test the solution, execute the following commands:

```bash
cd interesting_words
pip install virtualenv
virtualenv --version
virtualenv projectenv
. projectenv/bin/activate
pip install -r requirements.txt
python -m spacy download en
python main.py
```

## Use of virtualenv

The use of 'virtualenv', allows an isolated installation of the components needed to execute the solution. The command 'virtualenv --version' is used to check the proper installation of 'virtualenv' in case is not installed on the system.

## Overview of the solution

The code is self-explained, with many comments over the different features. Two classes were added: Document & Table.

The first one allows the calculation of the significant words, their frequency and their existence over the differente sentences.

The second one combines the words found over the different Documents, merging the frequencies and the presence of them on the sentences of each Document.

Different Python tools were used to accomplish this process, including the use of the Spacy package for Natural Language Processing.
