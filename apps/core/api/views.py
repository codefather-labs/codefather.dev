from typing import Union

from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from apps.core.api import models, constants
from apps.core.utils import generate_api_response
from settings.logger import system_message


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


@swagger_auto_schema(
    methods=['delete', 'post', 'patch', 'put'],
    request_body=models.request_post_model,
    manual_parameters=models.request_post_manual_params,
    responses={
        200: generate_api_response(success=True, details_schema=models.response_post_model)
    },
    tags=['post'],
    operation_description=constants.POST_ENDPOINT_DESCRIPTION
)
@api_view(['DELETE', 'POST', 'PATCH', 'PUT'])
def post(request: Request, reference: Union[str, str]):
    """
    :param request:
    :param reference: Post.UUID or Post.Slug
    :return: models.base_api_response
    """
    return Response(data={
        "error": False,
        "status": "Success",
        "details": None
    })


@swagger_auto_schema(
    method='get',
    manual_parameters=models.request_post_manual_params,
    responses={
        200: generate_api_response(success=True, details_schema=models.response_post_model)
    },
    tags=['post'],
    operation_description=constants.POST_ENDPOINT_DESCRIPTION
)
@api_view(['GET'])
def post_get(request: Request, reference: Union[str, str]):
    """
    :param request:
    :param reference: Post.UUID or Post.Slug
    :return: models.base_api_response
    """
    return Response(data={
        "error": False,
        "status": "Success",
        "details": None
    })
