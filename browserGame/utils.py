from django.utils import timezone
from .models import Log
from django.contrib.auth import get_user_model
import traceback, os


def save_log(type_log, message, request):
    if request.user.is_authenticated:
        user = request.user 
    else:
        user = None
    tb = traceback.extract_stack()[-2]
    log = Log(
        type_log=type_log,
        current_time=timezone.now(),
        user=user,
        message=message,
        document=os.path.basename(tb.filename),
        line= tb.lineno
    )
    log.save()