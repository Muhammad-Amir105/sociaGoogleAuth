from .utils import GoogleAuth
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserProfile
from .serializers import IdTokenSerializer
from .utils import GoogleAuth


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }


class googleAuthentication(APIView):

    def get(self, request):
        return Response({"message": "Hello World!"})

    def post(self, request, *args, **kwargs):
        serializer = IdTokenSerializer(data=request.data)
        if serializer.is_valid():
            id_token = serializer.validated_data['id_token']
            # Process id_token and get result
            if id_token:
                try:
                    payload = GoogleAuth.verify_id_token(id_token)
                    if payload:
                        user_id = payload.get('sub')
                        email = payload.get("email")
                        name = payload.get("name")

                        user, created = UserProfile.objects.get_or_create(
                            google_user_id=user_id,
                            defaults={'email': email, 'name': name}
                        )
                        response_data = get_token_for_user(user)
                        return Response(response_data, status=status.HTTP_200_OK)

                    else:
                        return Response({'error': 'invalid id token'}, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'missing id_token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
