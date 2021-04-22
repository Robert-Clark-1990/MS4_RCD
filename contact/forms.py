from django import forms


# Contact form thanks to LearnDjango.com - Link in README
class ContactForm(forms.Form):
    email_address = forms.EmailField(
        help_text='Please provide a valid email address.', required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '\
        Please provide as much detail about your project as possible'}),
                              required=True)
