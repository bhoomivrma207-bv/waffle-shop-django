from django import forms
from .models import WaffleVariety


class WaffleVarietyForm (forms.Form):
 #   waffle_variety = forms.ModelChoiceField
  #  (queryset=WaffleVariety.objects.all(), label="select chai variety")

    waffle_variety = forms.ModelChoiceField(
        queryset=WaffleVariety.objects.all(),
        label="Select waffle variety"
    )