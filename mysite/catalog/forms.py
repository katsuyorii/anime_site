from django import forms
from .models import Comment
from users.models import UserAnimeWatchPlanned


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


class AddAnimeToList(forms.ModelForm):
    status = forms.ChoiceField(choices=UserAnimeWatchPlanned.Status.choices, widget=forms.Select)

    class Meta:
        model = UserAnimeWatchPlanned
        fields = [
            'status',
        ]
