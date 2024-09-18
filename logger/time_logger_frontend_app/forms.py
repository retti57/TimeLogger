from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from time_logger_backend_app.models import Log, MilPerson, Notes, OrderForFlight


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

    def clean(self):
        """ Validators """
        cleaned_data = super().clean()
        datetime_dof = cleaned_data.get("date_of_flight")
        datetime_start_up = cleaned_data.get("start_up")
        datetime_takeoff = cleaned_data.get("take_off")
        datetime_land = cleaned_data.get("land")
        datetime_shutdown = cleaned_data.get("shut_down")
        if str(datetime_dof) not in str(datetime_start_up):

            error_message = _("Data wylotu jest niezgodna z pozostałymi polami")
            self.add_error('date_of_flight', error_message)
        else:
            if datetime_start_up and datetime_takeoff:
                if datetime_takeoff < datetime_start_up:
                    error_message = _("Czas startu nie może być wcześniejszy niż czas uruchomienia")
                    self.add_error('take_off', error_message)

            if datetime_takeoff and datetime_land:
                if datetime_land < datetime_takeoff:
                    error_message = _("Czas lądowania nie może być wcześniejszy niż czas startu")

                    self.add_error('land', error_message)

            if datetime_land and datetime_shutdown:
                if datetime_shutdown < datetime_land:
                    error_message = _("Czas wyłączenia nie może być wcześniejszy niż czas lądowania")

                    self.add_error('shut_down', error_message)

            if datetime_start_up == datetime_shutdown:
                error_message_su = _("Czas uruchomienia nie może być równy czasowi wyłączenia")
                error_message_sd = _("Czas wyłączenia nie może być równy czasowi uruchomienia")

                self.add_error('shut_down', error_message_sd)
                self.add_error('start_up', error_message_su)

        return cleaned_data


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


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = OrderForFlight
        fields = '__all__'
        widgets = {
            "number": forms.IntegerField(),
            "crew": forms.SelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('logs')
        self.helper.add_input(Submit('submit', "Wyślij"))

