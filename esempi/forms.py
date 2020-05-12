from django import forms

class FormContatto(forms.Form):
    nome = forms.CharField(label='Il tuo nome', max_length=100)
    cognome = forms.CharField(label='Il tuo cognome', max_length=100)
    email = forms.EmailField()
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Area di testo scrivi qui"}))
''' 
from django.core import validators
from django.core.exceptions import ValidationError

# DOCUMENTAZIONE UTILE:
# BUILT-IN VALIDATORS:  https://docs.djangoproject.com/en/3.0/ref/validators/
# LINK VALIDAZIONE:     https://docs.djangoproject.com/en/3.0/ref/forms/validation/
# FORM API:             https://docs.djangoproject.com/en/3.0/ref/forms/api/
# WORKING WITH FORMS:   https://docs.djangoproject.com/en/3.0/topics/forms/

class FormContatto(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
        attrs={"class": "form-control"}))
    cognome = forms.CharField(
        widget=forms.TextInput(
        attrs={"class": "form-control"}))
    email = forms.EmailField(
        widget=forms.TextInput(
        attrs={"class": "form-control"}))
    contenuto = forms.CharField(
        widget=forms.Textarea(
        attrs={"placeholder": "Area Testuale! Scrivi pure!", "class": "form-control"}),
        validators=[validators.MinLengthValidator(10)])

    def clean_contenuto(self):
        dati = self.cleaned_data["contenuto"]
        if "parola" in dati:
            raise ValidationError("Il contenuto inserito viola le norme del sito!")
        return dati
'''