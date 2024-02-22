from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import secrets


class ResultAPI(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    # For Debugging
    def initial(self, request, *args, **kwargs):
        # Perform any pre-authentication checks here
        # print(f"API: {request.COOKIES}")
        
        # If the pre-authentication checks pass, continue with the default initialization
        return super().initial(request, *args, **kwargs)

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, format=None):
        condition = secrets.choice([True, False])

        if condition:
            data = {"result": "Прогноз: 1"}
        else:
            data = {"result": "Прогноз: 2"}

        return Response(data=data, status=status.HTTP_200_OK)
