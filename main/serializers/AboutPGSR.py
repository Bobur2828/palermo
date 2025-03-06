from rest_framework.serializers import ModelSerializer
from main.models import AboutPGHeader, OurWorksTitle, OurWorks, AboutPGBlog,Testimonial
from main.serializers.functions import GeneralMixin

from rest_framework import serializers


class AboutHeaderSR(ModelSerializer, GeneralMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = AboutPGHeader
        fields = ('image', 'title', 'description', 'description_color', 'color1', 'color2', 'color3')

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')

    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')


class WorksTitleSR(ModelSerializer, GeneralMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = OurWorksTitle
        fields = ['title', 'description']

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')

    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')


class WorksSR(ModelSerializer, GeneralMixin):
    class Meta:
        model = OurWorks
        fields = '__all__'


class AboutBlogSR(ModelSerializer, GeneralMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = AboutPGBlog
        fields = ('id', 'title', 'description', 'image')

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')

    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')


class TestimonialSR(ModelSerializer, GeneralMixin):
    class Meta:
        model = Testimonial
        fields = '__all__'
