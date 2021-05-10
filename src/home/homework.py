from django.http import JsonResponse
from .serializers import ProjectSerislizer
from .models import Project
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


def projects(request):
    project = Project.objects.all()

    serializer = ProjectSerislizer(project, many=True)
    return JsonResponse(serializer.data, safe=False)


def project(request, project_id):
    project = Project.objects.get(id = project_id)

    serializer = ProjectSerislizer(project, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def api_projects(request):
    if request.method == "GET":
        comments = Project.objects.filter()
        serializer = ProjectSerislizer(comments, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProjectSerislizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_comment_detail(request, pk):
    comment = Project.objects.get(pk=pk)
    if request.method == "GET":
        serializer = ProjectSerislizer(comment)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProjectSerislizer(comment, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class APIProject(APIView):
    def get(self, request):
        comments = Project.objects.filter()
        serializer = ProjectSerislizer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerislizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIProjectDetail(APIView):
    def get(self, request, pk):
        comment = Project.objects.get(pk=pk)
        serializer = ProjectSerislizer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = Project.objects.get(pk=pk)
        serializer = ProjectSerislizer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = Project.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


