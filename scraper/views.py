from django.shortcuts import render
import uuid
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StartScrapingSerializer, ScrapingStatusSerializer
from .tasks import scrape_coins
from .models import ScrapingJob

class StartScrapingView(APIView):
    def post(self, request):
        serializer = StartScrapingSerializer(data=request.data)
        if serializer.is_valid():
            job_id = uuid.uuid4()
            scrape_coins.delay(job_id, serializer.validated_data['coins'])
            ScrapingJob.objects.create(job_id=job_id)
            return Response({'job_id': job_id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        job = get_object_or_404(ScrapingJob, job_id=job_id)
        return Response({
            'job_id': job_id,
            'tasks': job.results
        })
