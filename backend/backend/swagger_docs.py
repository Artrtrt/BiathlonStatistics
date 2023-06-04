from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from competitions_control.serializers import *
from chat_control.serializers import *
from users_control.serializers import *

category_create = swagger_auto_schema(
    operation_summary='Create category',
    tags=['Result'],
    request_body=ResultSerializer,
    responses={
        201: ResultSerializer,
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }

)

competition_create = swagger_auto_schema(
    operation_summary='Create competition',
    tags=['Competition'],
    request_body=CompetitionSerializer,
    responses={
        201: CompetitionSerializer,
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }

)

season_create = swagger_auto_schema(
    operation_summary='Create season',
    tags=['Season'],
    request_body=SeasonSerializer,
    responses={
        201: SeasonSerializer,
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden'
    }

)

message_create = swagger_auto_schema(
    operation_summary='Create message',
    tags=['Message'],
    request_body=MessageSerializer,
    responses={
        201: MessageSerializer,
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden'
    }

)

message_get_all = swagger_auto_schema(
    operation_summary='Get all messages',
    tags=['Message'],
    responses={
        201: MessageSerializer,
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }
)
competition_get_all = swagger_auto_schema(
    operation_summary='Get all competitions',
    tags=['Competition'],
    responses={
        200: CompetitionSerializer,
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }
)
result_get_all = swagger_auto_schema(
    operation_summary='Get all results',
    tags=['Result'],
    responses={
        200: ResultSerializer,
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

season_get_all = swagger_auto_schema(
    operation_summary='Get all seasons',
    tags=['Season'],
    responses={
        200: ResultSerializer,
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

competition_delete = swagger_auto_schema(
    operation_summary='Delete a competition',
    tags=['Competition'],
    responses={
        204: 'The competition has been deleted',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed'
    }
)

result_delete = swagger_auto_schema(
    operation_summary='Delete a result',
    tags=['Result'],
    responses={
        204: 'The result has been deleted',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed'
    }
)

category_delete = swagger_auto_schema(
    operation_summary='Delete a category',
    tags=['Result'],
    responses={
        204: 'The result has been deleted',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed'
    }
)
season_delete = swagger_auto_schema(
    operation_summary='Delete a season',
    tags=['Season'],
    responses={
        204: 'The season has been deleted',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed'
    }
)

season_put = swagger_auto_schema(
    operation_summary='Update season',
    tags=['Season'],
    responses={
        200: SeasonSerializer,
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

season_patch = swagger_auto_schema(
    operation_summary='Partial season update',
    tags=['Season'],
    responses={
        200: SeasonSerializer,
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)
competition_put = swagger_auto_schema(
    operation_summary='Update competition',
    tags=['Competition'],
    responses={
        200: CompetitionSerializer,
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

competition_patch = swagger_auto_schema(
    operation_summary='Partial competition update',
    tags=['Competition'],
    responses={
        200: CompetitionSerializer,
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

result_put = swagger_auto_schema(
    operation_summary='Update results',
    tags=['Result'],
    responses={
        200: ResultSerializer,
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

result_patch = swagger_auto_schema(
    operation_summary='Partial result update',
    tags=['Result'],
    responses={
        200: ResultSerializer,
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found'
    }
)

user_registration = swagger_auto_schema(
    operation_summary='User registration',
    tags=['User'],
    responses={
        200: UserRegistrSerializer,
        400: 'Bad Request',
        403: 'Forbidden'
    }
)

user_login = swagger_auto_schema(
    operation_summary='User authorization',
    tags=['User'],

)
