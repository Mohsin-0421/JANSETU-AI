from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Challenge, ProblemDNA
from .serializers import ChallengeSerializer
import random

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all().order_by('-created_at')
    serializer_class = ChallengeSerializer

    def create(self, request, *args, **kwargs):
        # Save the Challenge
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        challenge = serializer.save()

        # Generate Fake Problem DNA (Member 3 will replace this later)
        ProblemDNA.objects.create(
            challenge=challenge,
            domain=request.data.get("category", "Infrastructure"),
            urgency_score=random.randint(70, 95),
            skills_required=["Civil Engineering", "Data Science", "IoT"],
            estimated_cost="₹1.2L - ₹3.5L"
        )
        
        challenge.status = "ai_analyzed"
        challenge.save()

        # Return full data
        headers = self.get_success_headers(serializer.data)
        return Response(ChallengeSerializer(challenge).data, status=status.HTTP_201_CREATED, headers=headers)