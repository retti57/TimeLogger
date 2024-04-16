from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, TemplateView, ListView, DetailView
from time_logger_backend_app.models import Log, MilPerson
from time_logger_frontend_app.forms import ContactForm, SignUpForm, CreateLogForm
from logger.logger_utils import TimeCalculation



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


class CreateLogView(LoginRequiredMixin, CreateView):
    form_class = CreateLogForm
    template_name = 'time_logger_frontend_app/createlog_form.html'
    success_url = reverse_lazy('logs')


@login_required
def logsview(request: HttpRequest):
    user_logs = Log.objects.filter(crew__user__username=request.user.username)

    # logs = Log.objects.all()
    # mil_person = MilPerson.objects.get(user__username=request.user.username)
    # user_logs = Log.objects.filter(crew__last_name=mil_person.last_name)
    # filtered_logs = []
    # for log in user_logs:
    #     crew = log.crew.all()  # lista załogi
    #     if mil_person in crew:
    #         filtered_logs.append(log)
    context = {"user_logs": user_logs}

    return render(request, 'time_logger_frontend_app/logs_list.html', context=context)


@login_required
def tab2(request: HttpRequest):
    mil_person = MilPerson.objects.get(user__id=request.user.id)
    logs = Log.objects.filter(Q(crew__user_id=mil_person.user))
    context = {"mil_person": mil_person, "logs": logs}
    return render(request, 'time_logger_frontend_app/tab2.html', context=context)

@login_required
def detaillog(request: HttpRequest, pk):
    log = Log.objects.get(id=pk)
    crew = log.crew.all()
    # time calculation

    Times = TimeCalculation(log)
    times_named_tup = Times.get_times()
    context = {
        "times": times_named_tup,
        "log": log,
        "crew": crew
    }
    return render(request, 'time_logger_frontend_app/log_detail.html', context)

