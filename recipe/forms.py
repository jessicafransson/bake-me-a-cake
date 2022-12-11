from django.forms import ModelForm
from .models import Comment, Post
from django import forms


# what model form to use, and what fields to display
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)


class CreateRecipe(forms.ModelForm):
    class Meta:
        # title = forms.CharField()
        # content = forms.CharField()
        model = Post
        fields = (
            'title', 'content',
        )

        # def clean_title(self):
            # cleaned_data = self.cleaned_data  # dictionary
            # print(cleaned_data)
            # title = cleaned_data.get('title')
            # print(title)
            # return title
