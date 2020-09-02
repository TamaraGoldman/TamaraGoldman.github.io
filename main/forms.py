from .models import Feedback
from django.forms import ModelForm, Textarea
from django.utils import timezone


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["feedback"]
        widgets = {
            "feedback": Textarea(attrs={
                'placeholder': 'Ваш текст',
                'class': 'form'
            }),
        }
