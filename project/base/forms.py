from django import forms

from .models import Comment,Message

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class messageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ["message",]
    labels = {"message": "Message",}