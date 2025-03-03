from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'category', 'content', 'image', 'video']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'ckeditor'}),
        }