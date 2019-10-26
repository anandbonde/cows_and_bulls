class GamePolicy:
    def __init__(self, max_number_of_tries=12, number_of_bulls_required=4):
        self.max_number_of_tries = max_number_of_tries
        self.required_number_of_bulls = number_of_bulls_required

    def tries_have_exceeded(self, number_of_tries):
        return number_of_tries > self.max_number_of_tries

    def is_winner(self, number_of_tries, number_of_bulls):
        return self.tries_have_exceeded(number_of_tries) is False \
               and number_of_bulls == self.required_number_of_bulls
