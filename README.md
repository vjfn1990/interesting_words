# Interesting Words

## Parameters to be modified on the file 'main.py'

'words_to_retrieve' and 'files_path' should be modified, in order to execute the solution properly. More elegant solutions can be made, including the use of a webaapp which ask the user to upload the files.

In order to be able to test the solution, execute the following commands.

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

The use of 'virtualenv' allows an isolated installation of the components needed to execute the solution. The command 'virtualenv --version' is used to check the proper installation of 'virtualenv' in case its not installed on the system.

## Docker to isolate componentes and installations

Another way that I could tackle this problem, would be using Docker to isolate the components and installations over containers.

## Use of Django to create a web application

THe solution as a webapp would be possible also, using Django as the framework to build a webapp that is executed over a web server.

## Level of completeness

The code is self-explained, with many comments over the different features. Two classes were added: Document & Table.

The first one allows the calculation of the significant words, their frequency and their existence over the differente sentences.

The second one combines the words found over the different Documents, merging the frequencies and the presence of them on the sentences of each Document.

Different Python tools were used to accomplish the process, including the use of the Spacy package for Natural Language Processing.

The output could be shown on a much more readable way, also replacing the indexes that points to the sentences, by the sentences itself, as the test given by the company stablishs.

I wanted to invest more time over the logic of the application, the Object Oriented approach, the pythonic way to do things, and the different packages that are helpful to accoplish these kind of Text Analysis tasks.