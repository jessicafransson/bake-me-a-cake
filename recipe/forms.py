from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreateRecipe(forms.Form):
    class Meta:
        title = forms.CharField()
        content = forms.CharField()

        def clean_title(self):
            cleaned_data = self.cleaned_data # dictionary
            print(cleaned_data)
            title = cleaned_data.get('title')
            print(title)
            return title
