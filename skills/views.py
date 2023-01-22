from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Skills
from .serializers import SkillsSerializer
from api_connect.permissions import IsOwnerOrReadOnly


class SkillList(APIView):
    serializer_class = SkillsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        skills = Skills.objects.all()
        serializer = SkillsSerializer(
            skills, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillsSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class SkillsDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SkillsSerializer

    def get_object(self, pk):
        try:
            skill = Skills.objects.get(pk=pk)
            self.check_object_permissions(self.request, skill)
            return skill
        except Skills.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        skill = self.get_object(pk)
        serializer = SkillsSerializer(
            skill, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        skill = self.get_object(pk)
        serializer = SkillsSerializer(
            skill, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        skill = self.get_object(pk)
        skill.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
