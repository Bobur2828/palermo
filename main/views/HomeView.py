from rest_framework.response import Response
from rest_framework.views import APIView
from main import models
from main import serializers
from main import functions

class HomeHeaderAPIView(APIView):
    def get(self, request, lang):
        home_data = models.HomePG.objects.first()  # Faqat 1 ta obyekt olinadi

        if not home_data:
            return Response({"error": "Ma'lumot topilmadi"}, status=404)

        serializer = serializers.HomeHeaderSR(home_data, context={'lang': lang})

        return functions.custom_response(serializer.data)
