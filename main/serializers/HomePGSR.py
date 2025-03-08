from main.models import HomePGAbout, HomePGOffers
from rest_framework.serializers import ModelSerializer
from main.serializers.functions import GeneralMixin
from rest_framework import serializers


class HomeHeaderSR(ModelSerializer,GeneralMixin):
    title = serializers.SerializerMethodField()
    text1 = serializers.SerializerMethodField()
    text2 = serializers.SerializerMethodField()
    # class Meta:
    #     model = HomePageHeader
    #     fields = ['title', 'text1', 'text2','image', 'color_image_1', 'color_image_2']

    # def get_title(self, obj):
    #     return self.get_translated_field(obj, 'title')

    # def get_text1(self, obj):
    #     return self.get_translated_field(obj, 'text1')

    # def get_text2(self, obj):
    #     return self.get_translated_field(obj, 'text2')


class  HomeAboutSR(ModelSerializer, GeneralMixin):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    class Meta:
        model = HomePGAbout
        fields = ['title', 'text']

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')

    def get_text(self, obj):
        return self.get_translated_field(obj, 'text')

class HomeOffersSR(ModelSerializer, GeneralMixin):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = HomePGOffers
        fields = ['title', 'description', 'image']

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')

    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')