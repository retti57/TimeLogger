from datetime import datetime

import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, DetailView, ListView
from time_logger_backend_app.models import Log, Notes
from time_logger_frontend_app.forms import ContactForm, SignUpForm, CreateLogForm, MilPersonForm, CreateGridForm, \
    CreateNoteForm
from logger.time_calculator.TimeCalculation import TimeCalculation



def spiderpoints(request: HttpRequest):
    """ Widok renderuje formularz do wpisania danych do przekazania do API . Wciśnięcie przycisku wysyła zapytanie do
    API. API tworzy plik który następnie odsyła do klienta by pobrał. Odpowienio jest to plik kml lub gpx """
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
            from urllib3 import HTTPConnectionPool
            try:
                file = requests.post('http://localhost:5000/points/', json=data)
                file_content = file.content
                response = HttpResponse(file_content, content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="punkty.gpx"'

                return response
            except ConnectionError:
                from spiderpoints.spiderpoints import SpiderPoints
                timestmp = datetime.now().strftime('%d%m%Y_%H%M%S')

                filename = f'punkty_{timestmp}'

                SpiderPoints(data['initial_point'],
                             data['occurrence'],
                             data['distance']
                             ).create_kml_gpx(filename=filename)
                file_to_send = open(f'{filename}.gpx')
                response = HttpResponse(bytes(file_to_send. read().encode()), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="punkty.gpx"'
                file_to_send.close()
                return HttpResponse('<h1>No internet connection</h1>')
            except HTTPConnectionPool as e:
                print("Exeption: ", e)
                print('I do it anyway...')
                from spiderpoints.spiderpoints import SpiderPoints
                timestmp = datetime.now().strftime('%d%m%Y_%H%M%S')

                filename = f'punkty_{timestmp}'

                SpiderPoints(data['initial_point'],
                             data['occurrence'],
                             data['distance']
                             ).create_kml_gpx(filename=filename)

                file_to_send = open(f'{filename}.gpx')
                response = HttpResponse(bytes(file_to_send.read().encode()), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="punkty.gpx"'
                file_to_send.close()
                return response

    return render(request, "spiderpoints/spiderpoints.html", context=context)


class HomeView(TemplateView):
    template_name = 'time_logger_frontend_app/home.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'time_logger_frontend_app/contact.html'
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'time_logger_frontend_app/signup.html'
    success_url = reverse_lazy('milperson')


class MilpersonView(CreateView):
    form_class = MilPersonForm
    template_name = 'time_logger_frontend_app/milperson.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: MilPersonForm):
        user_credential = form.cleaned_data.get('username')
        print(user_credential)

        return super().form_valid(form)


class CreateLogView(LoginRequiredMixin, CreateView):
    form_class = CreateLogForm
    template_name = 'time_logger_frontend_app/createlog_form.html'
    success_url = reverse_lazy('logs')


@login_required
def logsview(request: HttpRequest):
    if request.user.is_superuser:
        user_logs = Log.objects.all()
        print('all')
    else:
        user_logs = Log.objects.filter(crew__user__username=request.user.username)

    context = {"user_logs": user_logs, "count_logs": len(user_logs)}

    return render(request, 'time_logger_frontend_app/logs_list.html', context=context)



class LogDetail(LoginRequiredMixin, DetailView):
    model = Log
    template_name = 'time_logger_frontend_app/log_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Times = TimeCalculation(self.model.objects.get(id=self.kwargs.get('pk')))
        context["times"] = Times.get_times()

        crew_list = [p.last_name for p in self.model.objects.get(id=self.kwargs.get('pk')).crew.all()]
        context["crew"] = crew_list
        return context


class NotesView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'time_logger_frontend_app/notes.html'
    success_url = reverse_lazy('home')


class AddNotesView(LoginRequiredMixin, CreateView):
    form_class = CreateNoteForm
    template_name = 'time_logger_frontend_app/add_notes.html'
    success_url = reverse_lazy('home')

