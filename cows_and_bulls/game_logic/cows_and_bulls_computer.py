class CowsAndBullsComputer:
    def __init__(self, word_parser, game_policy):
        self.parser = word_parser
        self.game_policy = game_policy
        self.number_of_tries = 0

    def compute(self, word1, word2):
        self.parse_words(word1, word2)
        self.number_of_tries += 1
        if self.game_policy.tries_have_exceeded(self.number_of_tries):
            raise Exception('Game over! You lose. Number of tries have exceeded, game over...!')
        number_of_cows = CowsAndBullsComputer.compute_number_of_cows(word1, word2)
        number_of_bulls = CowsAndBullsComputer.compute_number_of_bulls(word1, word2)
        game_result = self.game_policy.is_winner(self.number_of_tries, number_of_bulls)
        return number_of_cows, number_of_bulls, game_result

    def parse_words(self, word1, word2):
        self.parser.parse(word1)
        self.parser.parse(word2)

    @staticmethod
    def compute_number_of_cows(word1, word2):
        number_of_characters = len(word1)
        number_of_cows = 0
        for i in range(number_of_characters):
            if word1[i] != word2[i] and word1[i] in word2:
                number_of_cows += 1
        return number_of_cows

    @staticmethod
    def compute_number_of_bulls(word1, word2):
        number_of_characters = len(word1)
        number_of_bulls = 0
        for i in range(number_of_characters):
            if word1[i] == word2[i]:
                number_of_bulls += 1
        return number_of_bulls
