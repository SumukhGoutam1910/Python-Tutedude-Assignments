from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-pill px-4'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }
