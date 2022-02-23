from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.book
        fields = "__all__"