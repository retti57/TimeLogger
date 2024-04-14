from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from time_logger_backend_app.models import Log


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('contact')
        self.helper.add_input(Submit('submit', "Submit"))


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('contact')
        self.helper.add_input(Submit('submit', "Submit"))


class CreateLogForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = '__all__'
        widgets = {
            "crew": forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('logs')
        self.helper.add_input(Submit('submit', "Submit"))

