from django import forms
from .models import BlogPostModel,BlogCommentModel


class BlogPostModelForm(forms.ModelForm):

    class Meta:
        model = BlogPostModel
        #fields = "__all__"
        fields = ["titolo","contenuto", 'bozza']

class BlogCommentModelForm(forms.ModelForm):
    class Meta:
        model = BlogCommentModel
        fields = ['contenuto']