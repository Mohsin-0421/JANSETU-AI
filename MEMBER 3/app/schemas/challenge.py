from typing import List, Optional

from pydantic import BaseModel, Field


class ChallengeInput(BaseModel):
    title: Optional[str] = None

    description: str = Field(
        ...,
        min_length=10,
        description="Description of the problem or challenge"
    )


class ProblemClassification(BaseModel):
    domain: str
    subcategory: str

    urgency: int = Field(
        ...,
        ge=0,
        le=100
    )

    affected_population: int = Field(
        ...,
        ge=0
    )


class ProblemDNA(BaseModel):
    skills: List[str]
    technologies: List[str]
    estimated_cost: str

    scalability: int = Field(
        ...,
        ge=0,
        le=100
    )


class ChallengeAnalysis(BaseModel):
    challenge_id: Optional[str] = None
    classification: ProblemClassification
    problem_dna: ProblemDNA

class DuplicateDetectionInput(BaseModel):
    challenge_a: str = Field(
        ...,
        min_length=5
    )

    challenge_b: str = Field(
        ...,
        min_length=5
    )

class UniversityMatchInput(BaseModel):
    description: str = Field(
        ...,
        min_length=10
    )

class IndustryMatchInput(BaseModel):
    description: str = Field(
        ...,
        min_length=10
    )

class SolutionReuseInput(BaseModel):
    description: str = Field(
        ...,
        min_length=10
    )

class InnovationCollisionInput(BaseModel):
    challenge_a: str = Field(
        ...,
        min_length=10
    )

    challenge_b: str = Field(
        ...,
        min_length=10
    )

class AnalyzeChallengeInput(BaseModel):
    description: str = Field(
        ...,
        min_length=10
    )