from rest_framework.serializers import ModelSerializer

from main.models import ServicePGHeader, Consultations1, Consultations2, Consultations3, ServicePGClients, \
    ServicePGClientsTitle
from main.serializers.functions import GeneralMixin
from rest_framework import serializers


class ServiceHeaderSR(ModelSerializer, GeneralMixin):
    title = serializers.SerializerMethodField()
    body1_text = serializers.SerializerMethodField()
    body1_description = serializers.SerializerMethodField()
    body2_text = serializers.SerializerMethodField()
    body2_description = serializers.SerializerMethodField()

    class Meta:
        model = ServicePGHeader
        fields = [
            'image',
            'title',
            'body1_text',
            'body1_description',
            'body2_text',
            'body2_description',
            'body2_image', ]

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')

    def get_body1_text(self, obj):
        return self.get_translated_field(obj, 'body1_text')

    def get_body1_description(self, obj):
        return self.get_translated_field(obj, 'body1_description')

    def get_body2_text(self, obj):
        return self.get_translated_field(obj, 'body2_text')

    def get_body2_description(self, obj):
        return self.get_translated_field(obj, 'body2_description')


class Consultations1SR(GeneralMixin, ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Consultations1
        fields = ['id', 'title', 'description', 'image']

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')

    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')


class Consultations2SR(GeneralMixin, ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    class Meta:
        model = Consultations2
        fields = ['id', 'title', 'description', 'text', 'image', 'color', 'link']

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')

    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')

    def get_text(self, obj):
        return self.get_translated_field(obj, 'text')


class Consultations3SR(GeneralMixin, ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Consultations3
        fields = ['id', 'title', 'description', 'image']


class ServicePGClientsSR(serializers.ModelSerializer):
    class Meta:
        model = ServicePGClients
        fields = ['id', 'image']


class ServicePGClientsTitleSR(serializers.ModelSerializer, GeneralMixin):
    text = serializers.SerializerMethodField()
    client_images = serializers.SerializerMethodField()

    class Meta:
        model = ServicePGClientsTitle
        fields = ['id', 'text', 'client_images']

    def get_text(self, obj):
        return self.get_translated_field(obj, 'text')

    def get_client_images(self, obj):
        clients = ServicePGClients.objects.filter()[:3]
        return ServicePGClientsSR(clients, many=True).data
