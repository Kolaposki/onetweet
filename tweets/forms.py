from django import forms
from .models import Tweet

MAX_TWEET_LENGTH = 280


class TweetForm(forms.ModelForm):
    content = forms.Textarea(attrs={'placeholder': 'Enter tweet...'})

    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError('Tweet must not exceed 280 characters')
        return content
