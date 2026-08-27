import json
import os

import numpy as np

from sentence_transformers import SentenceTransformer


DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "solutions.json"
)


# Load embedding model once
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def load_solutions():
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def create_solution_text(solution: dict) -> str:
    """
    Combine important solution information
    into one text representation.
    """

    return (
        solution["problem"]
        + " "
        + solution["solution_description"]
        + " "
        + " ".join(solution["technologies"])
    )


def find_reusable_solutions(
    challenge_description: str
) -> list:

    solutions = load_solutions()

    solution_texts = [
        create_solution_text(solution)
        for solution in solutions
    ]

    all_texts = [
        challenge_description
    ] + solution_texts

    embeddings = model.encode(
        all_texts,
        normalize_embeddings=True
    )

    challenge_embedding = embeddings[0]

    results = []

    for index, solution in enumerate(solutions):

        solution_embedding = embeddings[index + 1]

        similarity = float(
            np.dot(
                challenge_embedding,
                solution_embedding
            )
        )

        similarity_percentage = round(
            similarity * 100,
            2
        )

        if similarity_percentage >= 80:
            reuse_potential = "HIGH"

        elif similarity_percentage >= 60:
            reuse_potential = "MEDIUM"

        else:
            reuse_potential = "LOW"

        results.append({
            "id": solution["id"],
            "name": solution["name"],
            "similarity": similarity_percentage,
            "reuse_potential": reuse_potential,
            "deployed_at": solution["deployed_at"],
            "technologies": solution["technologies"]
        })

    results.sort(
        key=lambda x: x["similarity"],
        reverse=True
    )

    return results