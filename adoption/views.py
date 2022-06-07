from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import AdoptionSerializer
from .email_service import sendEmailConfirmation


class AdoptionList(APIView):
    def post(self, request, format=None):
        serializer = AdoptionSerializer(data=request.data)
        if serializer.is_valid():
            adoptionData = serializer.save()
            sendEmailConfirmation(adoptionData)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "erros": serializer.errors,
                "message": "Validation error happened",
            },
            status=HTTP_400_BAD_REQUEST,
        )
