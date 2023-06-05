from django import forms


class AddNoteForm(forms.Form):
    title = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=500, widget=forms.Textarea)
