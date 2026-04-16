from django import forms
from tinymce.widgets import TinyMCE

from .models import Work


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = "__all__"
        widgets = {
            "description": TinyMCE(attrs={"cols": 80, "rows": 30}),
        }
