# MyProject App URLs
from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    url(r'^users/createUser/', createUser),
    url(r'^project/createProject/', createProject),
    url(r'^users/assignProject/', assignProject),
    path('project/assignMentor/', assignMentor),
    path('users/<str:user_id>/getProjects/', getProjects),
    path('users/<str:user_id>/getMentees/', getMentees),
    path('project/<str:proj_id>/getUserMentor/', getUserMentor)
]