class WordParser:
    def __init__(self, word_len, dictionary):
        self.word_len = word_len
        self.dictionary = dictionary

    def parse(self, word):
        self.verify_length(word)
        self.verify_uniqueness(word)
        self.verify_with_dictionary(word)

    def verify_length(self, word):
        if len(word) != self.word_len:
            raise Exception('Word must be of length {} ({})'.format(
                self.word_len, word))

    def verify_uniqueness(self, word):
        unique_letters = WordParser.get_unique_letters(word=word)
        if len(unique_letters) != self.word_len:
            raise Exception("Word must have 4 unique letters. ({})".format(word))

    @staticmethod
    def get_unique_letters(word):
        unique_letters = set()
        for letter in word:
            unique_letters.add(letter)
        return unique_letters

    def verify_with_dictionary(self, word):
        if self.word_not_found_in_dictionary(word):
            raise Exception("Word must be valid in the English language. ({})"
                            .format(word))

    def word_not_found_in_dictionary(self, word):
        return word not in self.dictionary \
               and not self.is_singular_version_in_dictionary(word)

    def is_singular_version_in_dictionary(self, word):
        return word[self.word_len - 1] is 's' \
               and word[:-1] in self.dictionary
