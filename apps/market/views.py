from django.http import HttpRequest, JsonResponse


def base(request: HttpRequest):
    return JsonResponse(data={})
