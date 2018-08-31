from django import forms


class ContactForm(forms.Form):
    author = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
