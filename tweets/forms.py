from django import forms
from tweets.models import Tweet

class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "What's happening?",
                'maxlength': 280,
                'rows': 5,
            })
        }
