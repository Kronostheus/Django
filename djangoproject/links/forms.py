from django import forms

from .models import Link, Comment, Vote

# Create/Edit Link
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("submitter", "rank")

# Comment/Reply
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

#Updoot
class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'
