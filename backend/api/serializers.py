from rest_framework import serializers
from .models import Challenge, ProblemDNA

class ProblemDNASerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemDNA
        fields = '__all__'

class ChallengeSerializer(serializers.ModelSerializer):
    problem_dna = ProblemDNASerializer(read_only=True)

    class Meta:
        model = Challenge
        fields = '__all__'