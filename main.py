import operator
import glob, os
from collections import defaultdict
from document import Document
from table import Table

# Amount of most common words to retrieve
words_to_retrieve = 10
# Location of the input files
files_path = '/home/vjfn1990/Desktop/interesting_words/input_files/'
# All the file names with extension .txt are retrieved
os.chdir(files_path)
file_names = []
for file_name in glob.glob('*.txt'):
    file_names.append(file_name)
file_names = sorted(file_names)
# A list of documents is created
overall_most_common_words = []
# The list is filled with Document objects
documents = [Document(files_path + file_name) for file_name in file_names]
# For every file, the significant words are determined, their frequency and the sentences where they appear
for document_index, document in enumerate(documents):
    print('Processing file \'' + file_names[document_index] + '\'...')
    document.assign_sentences_to_words()
    document.determine_most_common_words(words_to_retrieve)
    document.assign_sentences_to_words()
    document.determine_most_common_words(words_to_retrieve)
    # All the words retrieved from every file, are stored in one list
    overall_most_common_words += document.get_most_common_words()
# A table of entries is generated, formatted according to the requirements
table = Table(overall_most_common_words)
table_of_entries = table.get_entries()
print(table_of_entries)
