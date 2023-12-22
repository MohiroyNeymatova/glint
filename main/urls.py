from django.urls import path
from .views import *

urlpatterns = [
    path('get_logo/', get_logo),
    path('get_banner/', get_banner),
    path('get_services/', get_services),
    path('get_about/', get_about),
    path('get_team/', get_team),
    path('get_projects/', get_projects),
    path('get_reviews/', get_reviews),
    path('get_studio_gallery/', get_studio_gallery),
    path('contact/', contact),
    path('get_info/', get_info),
]