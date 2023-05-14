import pytest

from cows_and_bulls.game_logic.cows_and_bulls_computer import CowsAndBullsComputer


class TestCowsAndBullsComputer:
    word_len = 4

    @classmethod
    def setup_class(cls):
        from nltk.corpus import words
        from cows_and_bulls.game_logic.word_parser import WordParser
        cls.word_parser = WordParser(TestCowsAndBullsComputer.word_len, dictionary=words.words())
        from cows_and_bulls.game_logic.game_policy import GamePolicy
        cls.game_policy = GamePolicy()

    @pytest.mark.parametrize("word1, word2, expected_number_of_cows, expected_number_of_bulls, expected_game_result", [
        ("game", "play", 1, 0, False),
        ("cows", "cows", 0, 4, True),
        ("cows", "snow", 3, 0, False),
        ("slow", "snow", 0, 3, False),
        ("stew", "fast", 2, 0, False)
    ])
    def test_compute_with_valid_words_returns_correct_values(self, word1, word2, expected_number_of_cows,
                                                             expected_number_of_bulls, expected_game_result):
        computer = CowsAndBullsComputer(self.word_parser, self.game_policy)
        (actual_number_of_cows, actual_number_of_bulls, actual_game_result) = computer.compute(word1, word2)
        assert (expected_number_of_cows == actual_number_of_cows)
        assert (expected_number_of_bulls == actual_number_of_bulls)
        assert (expected_game_result == actual_game_result)
