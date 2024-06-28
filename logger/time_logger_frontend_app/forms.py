from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from time_logger_backend_app.models import Log, MilPerson, Notes


class MilPersonForm(forms.ModelForm):
    class Meta:
        model = MilPerson
        fields = ['rank', 'first_name', 'last_name', 'function_on_board']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('contact')
        self.helper.add_input(Submit('submit', "Wyślij"))


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('contact')
        self.helper.add_input(Submit('submit', "Dalej"))


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('contact')
        self.helper.add_input(Submit('submit', "Wyślij"))


class CreateLogForm(forms.ModelForm):

    field_order = 'aircraft', 'exercise', 'date_of_flight', 'start_up', 'take_off', 'land', 'shut_down', 'crew'

    class Meta:
        model = Log

        fields = '__all__'
        widgets = {
            "crew": forms.CheckboxSelectMultiple(),
            "date_of_flight": forms.DateInput(
                attrs={
                    'type': 'date',
                    'id': 'date_of_flight',
                    'data-datetime-field-id': 'date_of_flight'
                }),
            "start_up": forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'id': 'datetime-start_up',
                }),
            "take_off": forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'id': 'datetime-take_off',
                }),
            "land": forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'id': 'datetime-land',
                }),
            "shut_down": forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'id': 'datetime-shut_down',
                }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('logs')
        self.helper.add_input(Submit('submit', "Wyślij"))


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        widgets = {
            "note": forms.Textarea()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('logs')
        self.helper.add_input(Submit('submit', "Wyślij"))


class CreateGridForm(forms.Form):
    initial_point = forms.CharField()
    distance = forms.IntegerField()
    occurrence = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = reverse_lazy('spiderpoints')
        self.helper.add_input(Submit('submit', "Utwórz"))
