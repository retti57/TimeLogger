from django.views.generic import CreateView
from timelogger.time_logger_backend_app.models import UserModel

# Create your views here.

class CreateUserView(CreateView):
    model = UserModel
