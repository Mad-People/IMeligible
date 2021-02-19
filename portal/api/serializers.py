from rest_framework import serializers
from .models import CandidateDetails

class CandidateDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateDetails
        fields = "__all__"
        read_only_fields = ('id',)