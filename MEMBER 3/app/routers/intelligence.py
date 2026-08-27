from fastapi import APIRouter

from app.schemas.challenge import (
    ChallengeInput,
    ProblemClassification,
    ProblemDNA,
    DuplicateDetectionInput,
    UniversityMatchInput,
    IndustryMatchInput,
    SolutionReuseInput,
    InnovationCollisionInput,
    AnalyzeChallengeInput,
)

from app.services.classifier import classify_problem
from app.services.problem_dna import generate_problem_dna
from app.services.duplicate_detector import detect_duplicate
from app.services.university_matcher import match_universities
from app.services.industry_matcher import match_industries
from app.services.solution_reuse import find_reusable_solutions
from app.services.innovation_collision import analyze_innovation_collision

router = APIRouter()


@router.get("/intelligence/status")
def intelligence_status():
    return {
        "engine": "JANSETU Intelligence Engine",
        "status": "ready",
        "modules": {
            "problem_classification": "active",
            "problem_dna": "active",
            "duplicate_detection": "active",
            "university_matching": "active",
            "industry_matching": "active",
            "solution_reuse": "active",
            "innovation_collision": "active"
        }
    }


@router.post(
    "/classify-problem",
    response_model=ProblemClassification
)
def classify_challenge(challenge: ChallengeInput):

    return classify_problem(
        challenge.description
    )


@router.post(
    "/generate-problem-dna",
    response_model=ProblemDNA
)
def generate_dna(challenge: ChallengeInput):

    classification = classify_problem(
        challenge.description
    )

    return generate_problem_dna(
        description=challenge.description,
        domain=classification["domain"]
    )


@router.post("/detect-duplicate")
def check_duplicate(
    data: DuplicateDetectionInput
):

    return detect_duplicate(
        challenge_a=data.challenge_a,
        challenge_b=data.challenge_b
    )


@router.post("/match-universities")
def university_matching(
    data: UniversityMatchInput
):

    classification = classify_problem(
        data.description
    )

    dna = generate_problem_dna(
        description=data.description,
        domain=classification["domain"]
    )

    matches = match_universities(
        required_skills=dna["skills"],
        required_technologies=dna["technologies"]
    )

    return {
        "challenge": data.description,
        "classification": classification,
        "problem_dna": dna,
        "university_matches": matches
    }


@router.post("/match-industries")
def industry_matching(
    data: IndustryMatchInput
):

    classification = classify_problem(
        data.description
    )

    dna = generate_problem_dna(
        description=data.description,
        domain=classification["domain"]
    )

    matches = match_industries(
        required_skills=dna["skills"],
        required_technologies=dna["technologies"]
    )

    return {
        "challenge": data.description,
        "classification": classification,
        "problem_dna": dna,
        "industry_matches": matches
    }

@router.post("/find-reusable-solutions")
def solution_reuse(
    data: SolutionReuseInput
):

    solutions = find_reusable_solutions(
        challenge_description=data.description
    )

    return {
        "challenge": data.description,
        "reusable_solutions": solutions
    }

@router.post("/innovation-collision")
def innovation_collision(
    data: InnovationCollisionInput
):

    return analyze_innovation_collision(
        challenge_a=data.challenge_a,
        challenge_b=data.challenge_b
    )

@router.post("/analyze-challenge")
def analyze_challenge(
    data: AnalyzeChallengeInput
):

    # STEP 1: Classify the problem
    classification = classify_problem(
        data.description
    )

    # STEP 2: Generate Problem DNA
    dna = generate_problem_dna(
        description=data.description,
        domain=classification["domain"]
    )

    # STEP 3: Match universities
    university_matches = match_universities(
        required_skills=dna["skills"],
        required_technologies=dna["technologies"]
    )

    # STEP 4: Match industries
    industry_matches = match_industries(
        required_skills=dna["skills"],
        required_technologies=dna["technologies"]
    )

    # STEP 5: Search reusable solutions
    reusable_solutions = find_reusable_solutions(
        challenge_description=data.description
    )

    # Final JANSETU Intelligence Report
    return {
        "challenge": data.description,

        "classification": classification,

        "problem_dna": dna,

        "university_matches": university_matches,

        "industry_matches": industry_matches,

        "reusable_solutions": reusable_solutions
    }