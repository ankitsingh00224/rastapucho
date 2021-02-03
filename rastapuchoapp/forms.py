from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name','your_image','message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'your_image': forms.FileInput(attrs={'placeholder': 'Upload your image'}),
            'message':  forms.Textarea(attrs={'placeholder': 'Write your reviews'}),
        }
