
from django import forms

from .models import MailingListSubscriber

class MailingListForm(forms.ModelForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(MailingListForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Your Email Address'}


    class Meta:
        model = MailingListSubscriber
        fields = ('email',)
