

from rest_framework.response import Response

def custom_response(data, success=True, message="Success"):

    return Response({
        'success': success,
        'message': message,
        'data': data
    })

