from django import forms
from .models import Comment, Message, Subscriber
   
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['created']
        
class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'
        exclude = ['subscribed_at']
    