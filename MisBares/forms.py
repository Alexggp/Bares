from django import forms

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=30)
    image = forms. ImageField ()
