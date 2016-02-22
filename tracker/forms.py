from django import forms
from .models import Tracker

class TrackerForm(forms.ModelForm):

    class Meta:
        model = Tracker
        fields = ('requester_name', 'email', 'accession', 'study_name', 'source', 'link', 'samples', 'tissue', 'adult_or_pediatric', 'citation', 'details', 'priority')
        widgets = {'myfield': forms.TextInput(attrs={'div': 'field-style-vert'})}
