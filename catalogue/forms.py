
from django import forms

from .models import MailingListSubscriber

class MailingListForm(forms.ModelForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(MailingListForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs = {'class': 'form-control', 'required': True, 'placeholder': 'Your Email Address'}

    class Meta:
        model = MailingListSubscriber
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and MailingListSubscriber.objects.filter(email=email):
            raise forms.ValidationError('That email address is already subscribed.')
        return email
