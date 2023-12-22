from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['GET'])
def get_logo(request):
    data = LogoSerializer(Info.objects.last()).data
    return Response(data)


@api_view(['GET'])
def get_banner(request):
    data = BannerSerializer(Banner.objects.last()).data
    return Response(data)


@api_view(['GET'])
def get_services(request):
    data = ServiceSerializer(Service.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_about(request):
    data = AboutSerializer(About.objects.last()).data
    return Response(data)


@api_view(['GET'])
def get_team(request):
    data = TeamSerializer(Team.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_projects(request):
    data = ProjectSerializer(Project.objects.all().order_by('-id')[:3], many=True).data
    return Response(data)


@api_view(['GET'])
def get_reviews(request):
    data = ReviewSerializer(Review.objects.all().order_by('-id')[:4], many=True).data
    return Response(data)


@api_view(['GET'])
def get_studio_gallery(request):
    data = GallerySerializer(StudioGallery.objects.all().order_by('-id')[:11], many=True).data
    return Response(data)


@api_view(['POST'])
def contact(request):
    Contact.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        message=request.POST['message']
    )
    data = {
        "success": True
    }
    return Response(data)


@api_view(['GET'])
def get_info(request):
    data = InfoSerializer(Info.objects.last()).data
    return Response(data)