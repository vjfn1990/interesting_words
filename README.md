# Interesting Words

cd interesting_words
pip install virtualenv
virtualenv --version
virtualenv projectenv
. projectenv/bin/activate
pip install -r requirements.txt
python -m spacy download en
python main.py
