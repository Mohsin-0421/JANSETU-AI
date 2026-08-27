from app.services.classifier import classify_problem
from app.services.problem_dna import generate_problem_dna


TECHNOLOGY_FAMILIES = {
    "IoT & Smart Monitoring": [
        "iot",
        "smart irrigation",
        "smart waste monitoring",
        "water level sensors",
        "soil sensors",
        "water quality sensors",
        "air quality sensors"
    ],

    "Sensors & Monitoring": [
        "sensors",
        "soil sensors",
        "water level sensors",
        "water quality sensors",
        "air quality sensors"
    ],

    "Predictive & Intelligent Analytics": [
        "predictive analytics",
        "machine learning",
        "computer vision",
        "data analytics",
        "data science"
    ],

    "GIS & Spatial Intelligence": [
        "gis",
        "drone surveying"
    ],

    "Cloud & Digital Platforms": [
        "cloud computing",
        "learning management systems"
    ]
}


def find_common_items(list_a: list, list_b: list) -> list:

    list_b_lower = {
        item.lower()
        for item in list_b
    }

    common = []

    for item in list_a:
        if item.lower() in list_b_lower:
            common.append(item)

    return list(dict.fromkeys(common))


def find_technology_connections(
    technologies_a: list,
    technologies_b: list
) -> list:

    technologies_a_lower = {
        technology.lower()
        for technology in technologies_a
    }

    technologies_b_lower = {
        technology.lower()
        for technology in technologies_b
    }

    connections = []

    for family, technologies in TECHNOLOGY_FAMILIES.items():

        family_set = {
            technology.lower()
            for technology in technologies
        }

        a_matches = (
            technologies_a_lower &
            family_set
        )

        b_matches = (
            technologies_b_lower &
            family_set
        )

        if a_matches and b_matches:

            connections.append({
                "technology_family": family,
                "challenge_a_technologies": list(a_matches),
                "challenge_b_technologies": list(b_matches)
            })

    return connections


def calculate_collision_score(
    technology_connections: list,
    common_skills: list
) -> float:

    technology_score = (
        len(technology_connections) * 20
    )

    skill_score = (
        len(common_skills) * 10
    )

    score = technology_score + skill_score

    return round(
        min(score, 100),
        2
    )


def analyze_innovation_collision(
    challenge_a: str,
    challenge_b: str
) -> dict:

    # Analyze Challenge A
    classification_a = classify_problem(
        challenge_a
    )

    dna_a = generate_problem_dna(
        description=challenge_a,
        domain=classification_a["domain"]
    )

    # Analyze Challenge B
    classification_b = classify_problem(
        challenge_b
    )

    dna_b = generate_problem_dna(
        description=challenge_b,
        domain=classification_b["domain"]
    )

    # Exact common technologies
    common_technologies = find_common_items(
        dna_a["technologies"],
        dna_b["technologies"]
    )

    # Related technology families
    technology_connections = (
        find_technology_connections(
            dna_a["technologies"],
            dna_b["technologies"]
        )
    )

    # Common skills
    common_skills = find_common_items(
        dna_a["skills"],
        dna_b["skills"]
    )

    # Calculate collision score
    collision_score = calculate_collision_score(
        technology_connections=technology_connections,
        common_skills=common_skills
    )

    # Detect innovation
    different_domains = (
        classification_a["domain"]
        != classification_b["domain"]
    )

    if different_domains and collision_score >= 30:

        innovation_detected = True

        message = (
            "Potential cross-domain innovation detected. "
            "Although these challenges belong to different domains, "
            "they share related technologies and technical capabilities. "
            "A reusable or combined solution architecture may be possible."
        )

    elif collision_score >= 40:

        innovation_detected = True

        message = (
            "Strong technical overlap detected. "
            "A reusable solution architecture may be possible."
        )

    else:

        innovation_detected = False

        message = (
            "Limited technical overlap detected. "
            "Independent solutions may be more suitable."
        )

    return {
        "challenge_a": {
            "description": challenge_a,
            "classification": classification_a,
            "problem_dna": dna_a
        },

        "challenge_b": {
            "description": challenge_b,
            "classification": classification_b,
            "problem_dna": dna_b
        },

        "common_technologies": common_technologies,

        "common_skills": common_skills,

        "technology_connections": technology_connections,

        "collision_score": collision_score,

        "innovation_detected": innovation_detected,

        "message": message
    }