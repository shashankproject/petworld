from django import forms
from testapp.models import feedback

class FeedBackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'
