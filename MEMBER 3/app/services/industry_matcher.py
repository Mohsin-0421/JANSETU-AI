import json
import os


DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "industries.json"
)


def load_industries():
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def calculate_industry_match_score(
    required_skills: list,
    required_technologies: list,
    company_capabilities: list
) -> float:

    requirements = (
        required_skills +
        required_technologies
    )

    if not requirements:
        return 0.0

    requirements_lower = [
        item.lower()
        for item in requirements
    ]

    capabilities_lower = [
        item.lower()
        for item in company_capabilities
    ]

    matched = sum(
        1
        for requirement in requirements_lower
        if requirement in capabilities_lower
    )

    score = (
        matched / len(requirements_lower)
    ) * 100

    return round(score, 2)


def match_industries(
    required_skills: list,
    required_technologies: list
) -> list:

    industries = load_industries()

    results = []

    for company in industries:

        matched_capabilities = [
            requirement
            for requirement in (
                required_skills +
                required_technologies
            )
            if requirement.lower() in [
                capability.lower()
                for capability in company["capabilities"]
            ]
        ]

        matched_capabilities = list(
            dict.fromkeys(
                matched_capabilities
            )
        )

        score = calculate_industry_match_score(
            required_skills=required_skills,
            required_technologies=required_technologies,
            company_capabilities=company["capabilities"]
        )

        results.append({
            "id": company["id"],
            "name": company["name"],
            "match_score": score,
            "matched_capabilities": matched_capabilities
        })

    results.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return results