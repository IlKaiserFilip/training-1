from django import forms
from .models import BlogPostModel


class BlogPostModelForm(forms.ModelForm):

    class Meta:
        model = BlogPostModel
        #fields = "__all__"
        fields = ["titolo","contenuto", 'bozza']