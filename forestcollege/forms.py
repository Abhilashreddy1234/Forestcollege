from django import forms
# forms.py

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)


class EmailSubscriptionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email address'
    }))
