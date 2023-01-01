from rest_framework import status
from users.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

class RegisterView(APIView):
    def post(self, request):
        print("Resgister users")
        return Response(status=status.HTTP_400_BAD_REQUEST)