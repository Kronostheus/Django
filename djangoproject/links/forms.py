from django import forms

from .models import Link, Comment, Vote

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("submitter", "rank")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'
