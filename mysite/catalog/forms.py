from django import forms
from .models import Comment


class AddCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '4',
        'placeholder': 'Текст комментария...',
    }))

    class Meta:
        model = Comment
        fields = [
            'content',
        ]