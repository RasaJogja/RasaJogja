from django.forms import ModelForm
from autentikasi.models import MoodEntry

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["mood", "feelings", "mood_intensity"]