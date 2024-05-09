import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import json

from django.db.models import Q
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, DetailView
from time_logger_backend_app.models import Log, MilPerson
from time_logger_frontend_app.forms import ContactForm, SignUpForm, CreateLogForm, MilPersonForm, CreateGridForm
from logger.logger_utils import TimeCalculation
from urllib.parse import quote
from django.http import FileResponse, HttpResponse



def spiderpoints(request: HttpRequest):
    """ Widok renderuje formularz do wpisania danych do przekazania do API . Wciśnięcie przycisku wysyła zapytanie do API
    . API tworzy plik który następnie odsyła do klienta by pobrał. Odpowienio jest to plik kml lub gpx """
    form = CreateGridForm()
    context = {"form": form}
    if request.method == "GET":
        form = CreateGridForm(request.GET)
        if form.is_valid():

            data = {
                'initial_point': form.cleaned_data['initial_point'],
                'occurrence': str(form.cleaned_data['occurrence']),
                'distance': str(form.cleaned_data['distance']),
            }

            try:
                files = requests.post('http://localhost:5000/points/', json=data)
                file_content = files.content
                response = HttpResponse(file_content, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="punkty.gpx"'

                return response
            except Exception as e:
                return JsonResponse({"success": False, "message": str(e)}, status=500)

    return render(request, "spiderpoints/spiderpoints.html", context=context)


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
    success_url = reverse_lazy('milperson')


class MilpersonView(CreateView):
    form_class = MilPersonForm
    template_name = 'time_logger_frontend_app/milperson.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: MilPersonForm):
        # @TODO cleand_data na pole formularza user
        user_credential = form.cleaned_data.get('username')
        print(user_credential)

        return super().form_valid(form)


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


# @login_required
# def detaillog(request: HttpRequest, pk):
#     log = Log.objects.get(id=pk)
#     crew = log.crew.all()
#     # time calculation
#
#     Times = TimeCalculation(log)
#     times_named_tup = Times.get_times()
#     context = {
#         "times": times_named_tup,
#         "log": log,
#         "crew": crew
#     }
#     return render(request, 'time_logger_frontend_app/log_detail.html', context)


class LogDetail(LoginRequiredMixin, DetailView):
    model = Log
    template_name = 'time_logger_frontend_app/log_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Times = TimeCalculation(self.model.objects.get(id=self.kwargs.get('pk')))
        context["times"] = Times.get_times()
        return context
