from django import forms
from main.models import PostComment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']
        labels = {
            'comment': "Izoh"
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 2})
        }
