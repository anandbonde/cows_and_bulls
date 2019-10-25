import pytest


class TestWordParser:
    word_len = 4

    @classmethod
    def setup_class(cls):
        from nltk.corpus import words
        from src.cows_and_bulls.game_logic.word_parser import WordParser
        cls.word_parser = WordParser(word_len=TestWordParser.word_len, dictionary=words.words())

    @pytest.mark.parametrize("word", [
        ("  "),
        (""),
        ("t"),
        ("ts"),
        ("tes"),
        ("parse"),
        ("parser")
    ])
    def test_parse_with_other_than_desired_number_of_characters_raises_exception(self, word):
        with pytest.raises(Exception):
            self.word_parser.parse(word)

    @pytest.mark.parametrize("word", [
        ("aaaa"),
        ("test"),
        ("abbc"),
        ("abad")
    ])
    def test_parse_with_repeating_characters_raises_exception(self, word):
        with pytest.raises(Exception):
            self.word_parser.parse(word)

    @pytest.mark.parametrize("word", {
        ("wrod"),
        ("brid"),
        ("fnie"),
        ("ture"),
    })
    def test_parse_with_non_dictionary_word_raises_exception(self, word):
        with pytest.raises(Exception):
            self.word_parser.parse(word)

    @pytest.mark.parametrize("word", {
        ("word"),
        ("bird"),
        ("fine"),
        ("true"),
    })
    def test_parse_with_valid_and_dictionary_word_does_not_raises_exception(self, word):
        self.word_parser.parse(word)
