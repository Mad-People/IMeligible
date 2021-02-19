from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CandidateDetails
from .serializers import CandidateDetailsSerializer

class CandidateDetailsView(ModelViewSet):
    queryset = CandidateDetails.objects.all()
    serializer_class = CandidateDetailsSerializer