from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import ServicePG
from main.serializers import ServicePGSR


class ServicePGView(APIView):
    def get(self, request, lang=None):
        # models
        header = ServicePGSR.ServicePGHeader.objects.last()
        consultations1 = ServicePGSR.Consultations1.objects.last()
        consultations2 = ServicePGSR.Consultations2.objects.last()
        consultations3 = ServicePGSR.Consultations3.objects.last()
        clients = ServicePGSR.ServicePGClientsTitle.objects.last()

        # serializers
        header_serializer = ServicePGSR.ServiceHeaderSR(header)
        consultations1_serializer = ServicePGSR.Consultations1SR(consultations1)
        consultations2_serializer = ServicePGSR.Consultations2SR(consultations2)
        consultations3_serializer = ServicePGSR.Consultations3SR(consultations3)
        clients_serializer = ServicePGSR.ServicePGClientsTitleSR(clients)

        # data
        data = {
            "header": header_serializer.data,
            "consultations1": consultations1_serializer.data,
            "consultations2": consultations2_serializer.data,
            "consultations3": consultations3_serializer.data,
            "clients": clients_serializer.data
        }

        response_data = {
            'success': True,
            "message": "Success",
            "data": data
        }

        return Response(response_data)
