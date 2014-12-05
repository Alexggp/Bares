from django import forms

class UploadFileForm(forms.Form):
    bar_id= forms.IntegerField()
    image = forms. ImageField ()
