from django import forms
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        # widgets = {
        #     'text': forms.TextInput(attrs={'placeholder': 'Комментарий'}),
        # }
