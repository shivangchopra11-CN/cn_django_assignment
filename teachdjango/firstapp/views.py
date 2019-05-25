import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from requests import Response
from rest_framework import schemas
from rest_framework.decorators import renderer_classes, api_view
from rest_framework_swagger import renderers
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from .models import User, Project, ProjectUser


@csrf_exempt
@require_http_methods(['POST'])
@api_view(['POST'])
def createUser(request):
    """
        post:
            summary: Add a new user to the database.
            consumes:
                - application/json
            parameters:
                - in: query
                name: name
                type: string
                description: Name of the new user.
            responses:
                200:
                    description: OK
    """
    # print(request.body)
    data = json.loads(request.body.decode('utf-8'))
    name = data.get('name')
    u = User(name=name)
    u.save()
    # queryset = User.bjects.all()
    # serializer_class = UserSerializer
    return HttpResponse('202')


@csrf_exempt
@require_http_methods(['POST'])
@api_view(['POST'])
def createProject(request):
    """
        post:
        Add new project to the database.
    """
    # print(request.body)
    data = json.loads(request.body.decode('utf-8'))
    name = data.get('name')
    p = Project(name=name)
    p.save()
    return HttpResponse('202')


@csrf_exempt
@require_http_methods(['POST'])
@api_view(['POST'])
def assignProject(request):
    """
        post:
        Assign a project to user/users.
    """
    # print(request.body)
    data = json.loads(request.body.decode('utf-8'))
    users = data.get('ids')
    proj_id = data.get('proj_id')
    project = Project.objects.get(id=proj_id)
    for u in users:
        user_object = User.objects.get(id=u)
        pu = ProjectUser(user=user_object, project=project)
        pu.save()
    return HttpResponse('202')


@csrf_exempt
@require_http_methods(['POST'])
@api_view(['POST'])
def assignMentor(request):
    """
        post:
        Assign mentor to a project.
    """
    # print(request.body)
    data = json.loads(request.body.decode('utf-8'))
    user = data.get('user_id')
    user_object = User.objects.get(id=user)
    proj_id = data.get('proj_id')
    project = Project.objects.get(id=proj_id)
    pu = ProjectUser(user=user_object, project=project, is_mentor=True)
    pu.save()
    return HttpResponse('202')


@csrf_exempt
@require_http_methods(['GET'])
@api_view(['GET'])
def getProjects(request, user_id):
    """
        get:
        Get all the projects of a user.
    """
    # print(request.body)
    user_object = User.objects.get(id=user_id)
    projectUsers = ProjectUser.objects.filter(user=user_object, is_mentor=True).values_list('project_id', flat=True)
    projects = []
    for pu in projectUsers:
        projects.append(pu)
    response = {
        'result': projects,
        'message': "Projects Fetched",
        'status_code': '202'

    }
    return HttpResponse(json.dumps(response), content_type='application/json')


@csrf_exempt
@require_http_methods(['GET'])
@api_view(['GET'])
def getMentees(request, user_id):
    """
        get:
        Get all the mentees of a user.
    """
    # print(request.body)
    user_object = User.objects.get(id=user_id)
    projectUsers = ProjectUser.objects.filter(user=user_object, is_mentor=True).values_list('project_id', flat=True)
    projects = []
    for pu in projectUsers:
        projects.append(pu)
    users = []
    for proj in projects:
        cur_proj = Project.objects.get(id=proj)
        cur_usrs = ProjectUser.objects.filter(project=cur_proj, is_mentor=False).values_list('user_id', flat=True)
        for usr in cur_usrs:
            users.append(usr)
    users = list(set(users))
    response = {
        'result': users,
        'message': "Mentees Fetched",
        'status_code': '202'
    }
    return HttpResponse(json.dumps(response), content_type='application/json')


@csrf_exempt
@require_http_methods(['GET'])
@api_view(['GET'])
def getUserMentor(request, proj_id):
    """
        get:
        Get users and mentors of a project.
    """
    print(request, proj_id)
    proj_object = Project.objects.get(id=proj_id)
    pUsers = ProjectUser.objects.filter(project=proj_object, is_mentor=False).values_list('user_id', flat=True)
    projectMentor = ProjectUser.objects.get(project=proj_object, is_mentor=True).user_id
    users = []
    for pu in pUsers:
        users.append(pu)
    print(users, projectMentor)
    response = {
        'result': {'users': users, 'mentor': projectMentor},
        'message': "Mentors and Users Fetched",
        'status_code': '202'
    }
    return HttpResponse(json.dumps(response), content_type='application/json')
