
from django import forms

from .models import MailingListSubscriber

class MailingListForm(forms.ModelForm):

    class Meta:
        model = MailingListSubscriber
        fields = ('email',)
