from django import forms

from .models import File

FileForm = forms.modelform_factory(
    File,
    fields=("file",),
    widgets={
        "file": forms.FileInput(attrs={"class": "form-control"}),
    },
)


class EmailForm(forms.Form):
    email = forms.EmailField()

    class Meta:
        widgets = {
            "file": forms.TextInput(attrs={"class": "form-control"}),
        }


EmailFormset = forms.formset_factory(
    EmailForm,
    extra=5,
    max_num=5,
    validate_max=True,
    min_num=1,
    validate_min=True,
)
