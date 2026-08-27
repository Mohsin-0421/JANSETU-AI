import json
import os


DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "universities.json"
)


def load_universities():
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def calculate_match_score(
    required_skills: list,
    required_technologies: list,
    university_expertise: list
) -> float:

    requirements = (
        required_skills +
        required_technologies
    )

    if not requirements:
        return 0.0

    requirements = [
        item.lower()
        for item in requirements
    ]

    expertise = [
        item.lower()
        for item in university_expertise
    ]

    matched = 0

    for requirement in requirements:
        if requirement in expertise:
            matched += 1

    score = (
        matched / len(requirements)
    ) * 100

    return round(score, 2)


def match_universities(
    required_skills: list,
    required_technologies: list
) -> list:

    universities = load_universities()

    results = []

    for university in universities:

        score = calculate_match_score(
            required_skills=required_skills,
            required_technologies=required_technologies,
            university_expertise=university["expertise"]
        )

        results.append({
            "id": university["id"],
            "name": university["name"],
            "match_score": score,
            "matched_expertise": list(
                dict.fromkeys(
                    [
                        item
                        for item in (
                            required_skills +
                            required_technologies
                        )
                        if item.lower() in [
                            expertise.lower()
                            for expertise in university["expertise"]
                        ]
                    ]
                )
            )
        })

    results.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return results