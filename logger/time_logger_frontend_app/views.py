from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView
# from time_logger_backend_app.models import FunctionOnBoard
from django.contrib.auth.forms import UserCreationForm

from logger.time_logger_frontend_app.forms import ContactForm


# Create your views here.

# class UserDetailAdditionalInfoView(CreateView):
#     model = FunctionOnBoard
#     fields = '__all__'
#     template_name = 'time_logger_frontend_app/userdetailmodel_form.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'time_logger_frontend_app/signup.html'
    success_url = reverse_lazy('login')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'time_logger_frontend_app/contact.html'

    def form_valid(self, form: ContactForm) -> HttpResponse:
        print(form.cleaned_data['name'])
        return super().form_valid(form)


class TabView(TemplateView):
    template_name = 'time_logger_frontend_app/tab.html'


class HomeView(TemplateView):
    template_name = 'time_logger_frontend_app/home.html'


