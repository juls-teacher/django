from django import forms


class AddProductForm(forms.Form):
    title = forms.CharField(max_length=255)
    price = forms.IntegerField()
    color = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)