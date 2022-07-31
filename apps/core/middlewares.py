from django.core.handlers.asgi import ASGIRequest
from django.middleware.http import MiddlewareMixin, ConditionalGetMiddleware
from django.shortcuts import redirect

from settings.environment.settings import get_settings_module

settings = get_settings_module()


class RedirectAllowedHostMiddleware(MiddlewareMixin):
    def process_response(self, request: ASGIRequest, response):
        if request.get_host() == 'codefather-dev.herokuapp.com':
            return redirect('https://codefather.dev')
        return response
