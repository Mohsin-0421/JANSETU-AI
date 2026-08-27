from rest_framework import serializers
from .models import Challenge, ProblemDNA, University, Industry

class ProblemDNASerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemDNA
        fields = '__all__'

class ChallengeSerializer(serializers.ModelSerializer):
    problem_dna = ProblemDNASerializer(read_only=True)

    class Meta:
        model = Challenge
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'