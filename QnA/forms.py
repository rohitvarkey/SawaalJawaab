from django import forms
from QnA.models import *

class QuestionForm(forms.Form):
    explanation = forms.CharField(
            max_length=100,
            required=True,
            help_text="Enter the title for the question",
            label="Title",
            )
    body = forms.CharField(
            widget=forms.Textarea,
            required=True,
            label="Body",
            help_text="Detailed explanation of the question",
            )
    topics = forms.CharField(
            widget=forms.Textarea,
            required=True,
            label="Topics",
            help_text="Enter topics seperated by a space",
            )

class AnswerForm(forms.Form):
    body = forms.CharField(
            widget=forms.Textarea,
            required=True,
            label="Answer",
            )
class CommentForm(forms.Form):
    body = forms.CharField(
            required=True,
            label="Comment"
            )
