from django.db import models

class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="pending_ai_analysis")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
class ProblemDNA(models.Model):
    challenge = models.OneToOneField(Challenge, on_delete=models.CASCADE, related_name="problem_dna")
    domain = models.CharField(max_length=100)
    urgency_score = models.IntegerField(default=50)
    skills_required = models.JSONField(default=list) 
    estimated_cost = models.CharField(max_length=50)
    
    def __str__(self):
        return f"DNA for {self.challenge.title}"