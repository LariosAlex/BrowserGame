from .utils import save_log
from django.shortcuts import redirect
from . import views

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        save_log('INF', 'Accediendo a vista ', request)
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated and request.user.username not in ['super', 'admin']:
            views.activate_cron(request)
        return None


    