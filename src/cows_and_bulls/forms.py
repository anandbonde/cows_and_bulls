from django import forms
from nltk.corpus import words
from .game_logic.word_parser import WordParser


class WordForm(forms.Form):
    word = forms.CharField(
        label='Enter a 4-letter word',
        required=True,
        min_length=4,
        max_length=4,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Guess the word in my mind',
                'autofocus': True,
            }
        )
    )

    def clean_word(self):
        word = self.cleaned_data.get('word').lower()
        if len(word) != 4:
            raise forms.ValidationError('Your word must be of length 4.')
        if len(set(word)) != 4:
            raise forms.ValidationError('Your word cannot have repeating letters.')
        word_parser = WordParser(word_len=4, dictionary=words.words())
        try:
            word_parser.parse(word)
        except Exception as exception:
            raise forms.ValidationError(exception)
        return word
