from django import forms


class ContactForm(forms.Form):
    Email_Address = forms.EmailField(
        help_text='Please provide a valid email address.')
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '\
        Please provide as much detail about your project as possible'}))
