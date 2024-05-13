from django.http import HttpResponseRedirect
from django.urls import resolve, reverse


class RedirectInvalidURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            resolve(request.path)
        except:
            return HttpResponseRedirect(reverse('invalid_url'))  # Redirect to a custom page for invalid URLs

        response = self.get_response(request)
        return response
