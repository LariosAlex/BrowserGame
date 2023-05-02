from django.utils import timezone
from .models import Log
from django.contrib.auth import get_user_model
import inspect

def save_log(type_log, message, request):
    user = request.user if request.user.is_authenticated else None
    log = Log(
        type_log=type_log,
        current_time=timezone.now(),
        user=user,
        message=message,
        document=inspect.getframeinfo(inspect.currentframe()).filename,
        line= inspect.getframeinfo(inspect.currentframe()).lineno
    )
    log.save()