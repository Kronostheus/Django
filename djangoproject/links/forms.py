from django import forms

from .models import Link, Comment

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("submitter", "rank")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
