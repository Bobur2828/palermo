from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import aboutPG
from main.serializers import AboutPGSR


class AboutPGView(APIView):
    def get(self, request, lang=None):
        # models
        header = aboutPG.AboutPGHeader.objects.last()
        works_title = aboutPG.OurWorksTitle.objects.last()
        works_list = aboutPG.OurWorks.objects.all()
        about_blogs = aboutPG.AboutPGBlog.objects.filter()[:3]
        testimonial = aboutPG.Testimonial.objects.all()

        # serializers
        headerSR = AboutPGSR.AboutHeaderSR(header, context={'lang': lang, 'request': request})
        works_titleSR = AboutPGSR.WorksTitleSR(works_title, context={'lang': lang, 'request': request})
        works_listSR = AboutPGSR.WorksSR(works_list, many=True, context={'lang': lang, 'request': request})
        about_blogsSR = AboutPGSR.AboutBlogSR(about_blogs, many=True, context={'lang': lang, 'request': request})
        testimonialSR = AboutPGSR.TestimonialSR(testimonial, many=True, context={'lang': lang, 'request': request})

        data = {
            'header': headerSR.data,
            'works_title': works_titleSR.data,
            'works_list': works_listSR.data,
            'about_blogs': about_blogsSR.data,
            'testimonial': testimonialSR.data,
        }

        response_data = {
            'success': True,
            "message": "Success",
            "data": data
        }

        return Response(response_data)
