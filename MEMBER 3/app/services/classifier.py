import re


DOMAIN_KEYWORDS = {
    "Infrastructure": {
        "keywords": [
            "road",
            "bridge",
            "drainage",
            "drain",
            "street",
            "building",
            "infrastructure",
            "flood",
            "flooding",
            "pothole"
        ],
        "subcategories": {
            "Flood Management": [
                "flood",
                "flooding",
                "waterlogging",
                "water logging",
                "monsoon"
            ],
            "Road Infrastructure": [
                "road",
                "pothole",
                "street",
                "highway"
            ],
            "Drainage Management": [
                "drain",
                "drainage",
                "sewage",
                "waterlogging"
            ],
            "Public Infrastructure": [
                "building",
                "bridge",
                "street light"
            ]
        }
    },

    "Agriculture": {
        "keywords": [
            "farmer",
            "farm",
            "crop",
            "irrigation",
            "soil",
            "agriculture",
            "harvest",
            "pesticide"
        ],
        "subcategories": {
            "Irrigation": [
                "irrigation",
                "water supply",
                "water shortage"
            ],
            "Crop Management": [
                "crop",
                "harvest",
                "pest",
                "disease"
            ],
            "Soil Management": [
                "soil",
                "fertilizer"
            ]
        }
    },

    "Healthcare": {
        "keywords": [
            "hospital",
            "doctor",
            "health",
            "disease",
            "medicine",
            "patient",
            "clinic",
            "ambulance"
        ],
        "subcategories": {
            "Healthcare Access": [
                "hospital",
                "doctor",
                "clinic",
                "medicine"
            ],
            "Emergency Healthcare": [
                "ambulance",
                "emergency",
                "accident"
            ],
            "Disease Prevention": [
                "disease",
                "infection",
                "outbreak"
            ]
        }
    },

    "Education": {
        "keywords": [
            "school",
            "student",
            "teacher",
            "education",
            "college",
            "classroom",
            "children"
        ],
        "subcategories": {
            "School Infrastructure": [
                "school",
                "classroom",
                "building"
            ],
            "Digital Education": [
                "internet",
                "computer",
                "digital",
                "online"
            ],
            "Educational Access": [
                "student",
                "children",
                "teacher",
                "education"
            ]
        }
    },

    "Water & Sanitation": {
        "keywords": [
            "water",
            "drinking water",
            "sanitation",
            "toilet",
            "sewage",
            "contaminated"
        ],
        "subcategories": {
            "Drinking Water": [
                "drinking water",
                "clean water",
                "water shortage"
            ],
            "Sanitation": [
                "toilet",
                "sanitation",
                "hygiene"
            ],
            "Water Quality": [
                "contaminated",
                "pollution",
                "dirty water"
            ]
        }
    },

    "Environment": {
        "keywords": [
            "pollution",
            "waste",
            "garbage",
            "climate",
            "forest",
            "environment",
            "air quality"
        ],
        "subcategories": {
            "Waste Management": [
                "waste",
                "garbage",
                "trash"
            ],
            "Pollution Control": [
                "pollution",
                "air quality",
                "contamination"
            ],
            "Climate Resilience": [
                "climate",
                "heat",
                "drought"
            ]
        }
    }
}


def calculate_urgency(text: str) -> int:
    """
    Calculate urgency score from problem description.
    """

    text = text.lower()

    score = 40

    high_urgency_words = [
        "emergency",
        "danger",
        "critical",
        "immediately",
        "urgent",
        "death",
        "accident",
        "severe",
        "completely"
    ]

    medium_urgency_words = [
        "flood",
        "flooding",
        "unusable",
        "blocked",
        "shortage",
        "affecting"
    ]

    for word in high_urgency_words:
        if word in text:
            score += 10

    for word in medium_urgency_words:
        if word in text:
            score += 5

    return min(score, 100)


def extract_population(text: str) -> int:
    """
    Extract affected population from text.
    Example:
    'affecting 1200 people' -> 1200
    """

    text = text.lower()

    patterns = [
        r"(\d+)\s*(people|residents|villagers|citizens)",
        r"more than\s*(\d+)",
        r"over\s*(\d+)",
        r"around\s*(\d+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            return int(match.group(1))

    return 0


def classify_problem(description: str) -> dict:

    text = description.lower()

    domain_scores = {}

    for domain, data in DOMAIN_KEYWORDS.items():

        score = 0

        for keyword in data["keywords"]:

            if keyword in text:
                score += 1

        domain_scores[domain] = score


    domain = max(domain_scores, key=domain_scores.get)

    if domain_scores[domain] == 0:
        domain = "General"


    subcategory = "General"

    if domain != "General":

        subcategories = DOMAIN_KEYWORDS[domain]["subcategories"]

        subcategory_scores = {}

        for category, keywords in subcategories.items():

            score = 0

            for keyword in keywords:

                if keyword in text:
                    score += 1

            subcategory_scores[category] = score


        best_subcategory = max(
            subcategory_scores,
            key=subcategory_scores.get
        )

        if subcategory_scores[best_subcategory] > 0:
            subcategory = best_subcategory


    urgency = calculate_urgency(description)

    affected_population = extract_population(description)


    return {
        "domain": domain,
        "subcategory": subcategory,
        "urgency": urgency,
        "affected_population": affected_population
    }