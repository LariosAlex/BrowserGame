from .utils import save_log

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        save_log('INF', 'Accediendo a vista', request)
        response = self.get_response(request)
        return response