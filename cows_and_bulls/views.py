from django.http import JsonResponse
from django.shortcuts import render
import random
from nltk.corpus import words
from .forms import WordForm
from cows_and_bulls.game_logic.word_parser import WordParser
from cows_and_bulls.game_logic.cows_and_bulls_computer import CowsAndBullsComputer
from cows_and_bulls.game_logic.game_policy import GamePolicy


def landing_page(request):
    word_form = WordForm()
    seed_game(request)
    context = {
        'form': word_form
    }
    return render(request, 'landing_page.html', context)


def seed_game(request):
    request.session['seed_word'] = select_random_word().lower()
    request.session['number_of_attempts'] = 0


def select_random_word():
    word_list = [w for w in words.words() if len(w) == 4 and len(set(w)) == 4]
    random_word_index = random.randint(0, len(word_list) - 1)
    return word_list[random_word_index]


def ajax_handler_for_word_submit(request):
    if request.method == "POST" and request.is_ajax():
        word_form = WordForm(request.POST)
        if word_form.is_valid():
            attempted_word = word_form.cleaned_data.get('word').lower()
            seed_word = request.session.get('seed_word')
            number_of_attempts = request.session.get('number_of_attempts')
            request.session['number_of_attempts'] = number_of_attempts+1
            word_parser = WordParser(word_len=4, dictionary=words.words())
            cows_and_bulls_computer = CowsAndBullsComputer(word_parser, GamePolicy(max_number_of_tries=1))
            number_of_cows, number_of_bulls, is_winner = cows_and_bulls_computer.compute(seed_word, attempted_word)
            return JsonResponse({
                "success": True,
                "original_word": seed_word if number_of_attempts == 14 else None,
                "attempted_word": attempted_word,
                "number_of_attempts_exceeded" : number_of_attempts == 14,
                "number_of_cows": number_of_cows,
                "number_of_bulls": number_of_bulls,
                "is_winner": is_winner,
            }, status=200)
    return JsonResponse({"success": False, "error": word_form.errors}, status=400)
