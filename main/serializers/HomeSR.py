from main import models
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from main.serializers.functions import GeneralMixin
from rest_framework import serializers



class HomeHeaderSR(ModelSerializer, GeneralMixin):
    title = SerializerMethodField()
    description = SerializerMethodField()
    minititle = SerializerMethodField()
    about_title = SerializerMethodField()
    about_description = SerializerMethodField()
    image1_title = SerializerMethodField()
    image1_description = SerializerMethodField()
    image2_title = SerializerMethodField()
    image2_description = SerializerMethodField()
    image3_title = SerializerMethodField()
    image3_description = SerializerMethodField()
    image4_title = SerializerMethodField()
    image4_description = SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, "title")

    def get_description(self, obj):
        return self.get_translated_field(obj, "description")

    def get_minititle(self, obj):
        return self.get_translated_field(obj, "minititle")

    def get_about_title(self, obj):
        return self.get_translated_field(obj, "about_title")

    def get_about_description(self, obj):
        return self.get_translated_field(obj, "about_description")

    def get_image1_title(self, obj):
        return self.get_translated_field(obj, "image1_title")

    def get_image1_description(self, obj):
        return self.get_translated_field(obj, "image1_description")

    def get_image2_title(self, obj):
        return self.get_translated_field(obj, "image2_title")

    def get_image2_description(self, obj):
        return self.get_translated_field(obj, "image2_description")

    def get_image3_title(self, obj):
        return self.get_translated_field(obj, "image3_title")

    def get_image3_description(self, obj):
        return self.get_translated_field(obj, "image3_description")

    def get_image4_title(self, obj):
        return self.get_translated_field(obj, "image4_title")

    def get_image4_description(self, obj):
        return self.get_translated_field(obj, "image4_description")

    class Meta:
        model = models.HomePG
        fields = [
            "title", "description", "minititle", "image",
            "color_image_1", "color_image_2", "about_title", "about_description",
            "image1_title", "image1_description", "image1",
            "image2_title", "image2_description", "image2",
            "image3_title", "image3_description", "image3",
            "image4_title", "image4_description", "image4",
        ]



