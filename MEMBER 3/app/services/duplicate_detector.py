from sentence_transformers import SentenceTransformer
import numpy as np


# Load the embedding model once
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def calculate_similarity(
    challenge_a: str,
    challenge_b: str
) -> float:
    """
    Calculate semantic similarity between
    two challenge descriptions.
    """

    embeddings = model.encode(
        [challenge_a, challenge_b],
        normalize_embeddings=True
    )

    similarity = float(
        np.dot(
            embeddings[0],
            embeddings[1]
        )
    )

    # Convert decimal to percentage
    similarity_percentage = round(
        similarity * 100,
        2
    )

    return similarity_percentage


def detect_duplicate(
    challenge_a: str,
    challenge_b: str
) -> dict:

    similarity = calculate_similarity(
        challenge_a,
        challenge_b
    )

    # Duplicate decision threshold
    is_duplicate = similarity >= 75

    if similarity >= 90:
        recommendation = (
            "Very high similarity. "
            "Recommended to merge into a master challenge."
        )

    elif similarity >= 75:
        recommendation = (
            "Potential duplicate. "
            "Manual review recommended."
        )

    else:
        recommendation = (
            "Challenges appear sufficiently different."
        )

    return {
        "challenge_a": challenge_a,
        "challenge_b": challenge_b,
        "similarity": similarity,
        "is_duplicate": is_duplicate,
        "recommendation": recommendation
    }