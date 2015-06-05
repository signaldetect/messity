"""
Forms of the `critic` app
"""

from django import forms


class ReviewForm(forms.Form):
    DEFAULT_BOOK_CHOICES = (('---', 'No books available'),)

    book = forms.ChoiceField(choices=DEFAULT_BOOK_CHOICES)
    text = forms.CharField(widget=forms.Textarea)
