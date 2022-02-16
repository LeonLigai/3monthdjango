from django import forms
from . import models

class BookShowForm(forms.ModelForm):
    class Meta:
        model = models.book
        fields = "__all__"