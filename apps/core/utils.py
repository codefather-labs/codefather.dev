from drf_yasg import openapi


def generate_api_response(success: bool, status: str = None, details_schema: openapi.Schema = None):
    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(
                type=openapi.TYPE_BOOLEAN, default=False if success else True
            ),
            'status': openapi.Schema(
                type=openapi.TYPE_STRING,
                default='Success' if success and not status else status if status else 'Failed',
            ),
            'details': details_schema if details_schema \
                else openapi.Schema(type=openapi.TYPE_OBJECT)
        })
