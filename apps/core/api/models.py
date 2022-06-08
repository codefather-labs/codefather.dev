from drf_yasg import openapi

from settings.environment.settings import get_settings_module

settings = get_settings_module()

base_api_response = openapi.Schema(
    type=openapi.TYPE_OBJECT, properties={
        "error": openapi.Schema(type=openapi.TYPE_BOOLEAN),
        "status": openapi.Schema(type=openapi.TYPE_STRING),
        "details": openapi.Schema(type=openapi.TYPE_OBJECT),
    }
)

request_post_manual_params = [
    openapi.Parameter(
        'reference',
        openapi.IN_PATH,
        type=openapi.TYPE_STRING,
        required=True
    )
]

request_post_model = openapi.Schema(
    type=openapi.TYPE_OBJECT, properties={
        "language": openapi.Schema(
            type=openapi.TYPE_STRING,
            enum=settings.languages
        ),

        "author": openapi.Schema(type=openapi.TYPE_STRING),
        "author_contact": openapi.Schema(type=openapi.TYPE_STRING),
        "title": openapi.Schema(type=openapi.TYPE_STRING),
        "slug": openapi.Schema(type=openapi.TYPE_STRING),
        "body": openapi.Schema(type=openapi.TYPE_STRING),
        "tag": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_STRING
            ))
    })

response_post_model = openapi.Schema(
    type=openapi.TYPE_OBJECT, properties={
        "uuid": openapi.Schema(type=openapi.TYPE_STRING),
        "language": openapi.Schema(
            type=openapi.TYPE_STRING,
            enum=settings.languages
        ),
        "author": openapi.Schema(type=openapi.TYPE_STRING),
        "author_contact": openapi.Schema(type=openapi.TYPE_STRING),
        "title": openapi.Schema(type=openapi.TYPE_STRING),
        "slug": openapi.Schema(type=openapi.TYPE_STRING),
        "body": openapi.Schema(type=openapi.TYPE_STRING),
        "tag": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_STRING
            ))
    })
