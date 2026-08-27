from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Challenge, ProblemDNA, University, Industry
from .serializers import ChallengeSerializer, UniversitySerializer, IndustrySerializer
import random

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all().order_by('-created_at')
    serializer_class = ChallengeSerializer

    def create(self, request, *args, **kwargs):
        # Save the Challenge
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        challenge = serializer.save()

        # Generate Problem DNA
        ProblemDNA.objects.create(
            challenge=challenge,
            domain=request.data.get("category", "Infrastructure"),
            urgency_score=random.randint(70, 95),
            skills_required=["Civil Engineering", "Data Science", "IoT"],
            estimated_cost="₹1.2L - ₹3.5L"
        )
        
        challenge.status = "ai_analyzed"
        challenge.save()

        headers = self.get_success_headers(serializer.data)
        return Response(ChallengeSerializer(challenge).data, status=status.HTTP_201_CREATED, headers=headers)

    # 🚀 THE NEW MATCHMAKER ENDPOINT
    @action(detail=True, methods=['get'])
    def matches(self, request, pk=None):
        challenge = self.get_object()
        
        # In a real scenario, AI compares DNA to University departments here
        universities = University.objects.all()[:3] # Grab top 3 for demo
        industries = Industry.objects.all()[:3]     # Grab top 3 for demo
        
        return Response({
            "challenge_title": challenge.title,
            "status": "Matches Found",
            "recommended_universities": UniversitySerializer(universities, many=True).data,
            "recommended_industries": IndustrySerializer(industries, many=True).data,
            "system_confidence": f"{random.randint(88, 98)}%"
        })

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer