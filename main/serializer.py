from rest_framework import serializers
from .models import *


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['logo']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Banner
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = About
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioGallery
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        exclude = ['logo']