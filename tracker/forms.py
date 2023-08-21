from django import forms
from .models import FencedField

class FencedFieldForm(forms.ModelForm):
    class Meta:
        model = FencedField
        fields = ['point1lon', 'point1lat','point2lon','point2lat', 'point3lon','point3lat','point4lon','point4lat']