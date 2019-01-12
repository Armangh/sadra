from django.forms import ModelForm
from .models import Replay

class ReplayForm(ModelForm):
    class Meta:
        model = Replay
        fields = ['text']
