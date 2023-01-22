from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Jobs
from .serializers import JobSerializer
from api_connect.permissions import IsOwnerOrReadOnly


class JobList(APIView):
    serializer_class = JobSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        jobs = Jobs.objects.all()
        serializer = JobSerializer(
            jobs, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(
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


class JobDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = JobSerializer

    def get_object(self, pk):
        try:
            job = Jobs.objects.get(pk=pk)
            self.check_object_permissions(self.request, job)
            return job
        except Jobs.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        job = self.get_object(pk)
        serializer = JobSerializer(
            job, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        job = self.get_object(pk)
        serializer = JobSerializer(
            job, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        job = self.get_object(pk)
        job.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
