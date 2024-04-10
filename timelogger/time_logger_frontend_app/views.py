from django.http import HttpResponse
from django.views.generic import CreateView, FormView, TemplateView
from time_logger_backend_app.models import UserDetailModel
from django.contrib.auth.forms import UserCreationForm

from time_logger_frontend_app.forms import ContactForm


# Create your views here.

class UserDetailAdditionalInfoView(CreateView):
    model = UserDetailModel
    fields = '__all__'
    template_name = 'time_logger_frontend_app/userdetailmodel_form.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'time_logger_frontend_app/signup.html'


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


