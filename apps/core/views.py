from django.shortcuts import redirect
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from apps.core.utils import generate_api_response


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


@swagger_auto_schema(
    method='get',
    responses={
        200: generate_api_response(success=True)
    },
    tags=['test']
)
@api_view(['GET'])
def test(request: Request):
    return Response(data={
        "error": False,
        "status": "Success",
        "details": None
    })


def main(request: Request):
    return redirect('schema-swagger-ui')
