from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, ListView
from time_logger_backend_app.models import Log
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


class LogsView(LoginRequiredMixin, ListView):
    model = Log
    template_name = 'time_logger_frontend_app/logs_list.html'

    def get_queryset(self):
        return Log.objects.filter(crew=self.request.user)

# @ TODO  widok HOMEPAGE po zalogowaniu : wyświetla wszystkie logi lotów, chronologicznie - datą, i dodatkowo
#  wyświetla obliczony czas powietrza i ziemii z funkcji w logger/logger_utils.py
@login_required
def logsview(request:HttpRequest):
    logs = Log.objects.all()
    # mil_person = MilPerson.objects.all().filter(id=User.get(pk=pk))
    # user_logs = Log.objects.all()
    context = {'logs': logs}

    return render(request, 'time_logger_frontend_app/logs_list.html',context=context)
