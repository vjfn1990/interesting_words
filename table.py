class Table:

    def __init__(self, combined_document):
        self._entries = []
        # A table of entries is defined, based on a merge between the words found on the different documents
        for x_index, x in enumerate(combined_document):
            if self.word_exists_in_entries(x):
                # If the current word is already stored on the table of entries, the values of both are merged
                self.update_word_information(x)
            else:
                # If not, the new word is added to the table of entries
                self.insert_word_information(x)

    def get_entries(self):
        return self._entries

    def word_exists_in_entries(self, new_word):
        # It returns True is the word already exist on the table of entries, and False otherwise
        for stored_word in self._entries:
            if stored_word['value'] == new_word['value']:
                return True
        return False

    def insert_word_information(self, new_word):
        # It adds the new word to the table of entries
        self._entries.append({
            'value': new_word['value'],
            'frequency': new_word['frequency'],
            'files': [new_word['file']],
            'sentences_by_file': [new_word['sentences']]
        })

    def update_word_information(self, new_word):
        # It merges the new word with the one already stored on the table of entries,
        # adding the frequency of appearance, and appending the list of sentences where the word exist on the current document
        for stored_word_index, stored_word in enumerate(self._entries):
            if stored_word['value'] == new_word['value']:
                self._entries[stored_word_index]['frequency'] += new_word['frequency']
                self._entries[stored_word_index]['files'].append(new_word['file'])
                self._entries[stored_word_index]['sentences_by_file'].append(new_word['sentences'])
