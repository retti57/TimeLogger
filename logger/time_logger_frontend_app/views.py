from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, ListView
from time_logger_backend_app.models import Log, MilPerson
from time_logger_frontend_app.forms import ContactForm, SignUpForm, CreateLogForm




class HomeView(TemplateView):
    template_name = 'time_logger_frontend_app/home.html'


class TabView(TemplateView):
    template_name = 'time_logger_frontend_app/tab.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'time_logger_frontend_app/contact.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form: ContactForm) -> HttpResponse:

        print(form.cleaned_data)
#  @TODO automatyczne wypełanianie imienia
        return super().form_valid(form)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'time_logger_frontend_app/signup.html'
    success_url = reverse_lazy('home')


class CreateLogView(LoginRequiredMixin,CreateView):
    form_class = CreateLogForm
    template_name = 'time_logger_frontend_app/createlog_form.html'
    success_url = reverse_lazy('logs')


@login_required
def logsview(request:HttpRequest):
    # logs = Log.objects.all()
    # mil_person = MilPerson.objects.get(user__username=request.user.username)
    user_logs = Log.objects.filter(crew__user__username=request.user.username)
    # user_logs = Log.objects.filter(crew__last_name=mil_person.last_name)
    # filtered_logs = []
    # for log in user_logs:
    #     crew = log.crew.all()  # lista załogi
    #     if mil_person in crew:
    #         filtered_logs.append(log)
    context = {"mil_person": mil_person,
               # "user_logs": filtered_logs,
               "user_logs": user_logs}

    return render(request, 'time_logger_frontend_app/logs_list.html',context=context)
