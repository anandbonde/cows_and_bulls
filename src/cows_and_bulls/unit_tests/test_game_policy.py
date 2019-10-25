import pytest

from src.cows_and_bulls.game_logic.game_policy import GamePolicy


class TestGamePolicy:
    @classmethod
    def setup_class(cls):
        cls.game_policy = GamePolicy()

    @pytest.mark.parametrize("number_of_tries, expected_tries_have_exceeded", [
        (11, False),
        (12, False),
        (13, True),
        (11, False)
    ])
    def test_tries_have_exceeded(self, number_of_tries, expected_tries_have_exceeded):
        assert (expected_tries_have_exceeded == self.game_policy.tries_have_exceeded(number_of_tries))

    @pytest.mark.parametrize("number_of_tries, number_of_bulls, expected_is_winner", [
        (11, 4, True),
        (12, 4, True),
        (13, 4, False),
        (11, 3, False)
    ])
    def test_is_winner(self, number_of_tries, number_of_bulls, expected_is_winner):
        assert (expected_is_winner == self.game_policy.is_winner(number_of_tries, number_of_bulls))
