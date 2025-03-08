from rest_framework.views import APIView
from rest_framework.response import Response
from main.models.homePG import  HomePGAbout, HomePGOffers
from main.serializers.HomePGSR import HomeHeaderSR,HomeAboutSR, HomeOffersSR


class HomePGView(APIView):
    def get(self, request, lang=None):
        #models
        # header = HomePageHeader.objects.last()
        about = HomePGAbout.objects.last()
        offers = HomePGOffers.objects.filter().order_by('-id')[:4]

        #serializers
        # headerSR = HomeHeaderSR(header, context={'lang': lang, 'request': request})
        aboutSR = HomeAboutSR(about,context={'lang': lang, 'request': request})
        offersSR = HomeOffersSR(offers, many=True, context={'lang': lang, 'request': request})

        data = {
            # "header": headerSR.data,
            "about": aboutSR.data,
            "offers": offersSR.data,

        }

        response_data =  {
            'success': True,
            "message": "Success",
            "data": data
        }

        return Response(response_data)
