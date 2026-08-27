def generate_problem_dna(description: str, domain: str) -> dict:

    text = description.lower()

    skills = []
    technologies = []

    # Infrastructure
    if domain == "Infrastructure":

        skills.extend([
            "Civil Engineering"
        ])

        if any(word in text for word in [
            "flood",
            "flooding",
            "waterlogging",
            "monsoon",
            "drainage",
            "drain"
        ]):
            skills.extend([
                "IoT",
                "GIS",
                "Data Science"
            ])

            technologies.extend([
                "Sensors",
                "GIS",
                "Predictive Analytics"
            ])

        if any(word in text for word in [
            "road",
            "pothole",
            "bridge"
        ]):
            technologies.extend([
                "GIS",
                "Drone Surveying"
            ])

    # Agriculture
    elif domain == "Agriculture":

        skills.extend([
            "Agricultural Engineering",
            "Data Science"
        ])

        if any(word in text for word in [
            "irrigation",
            "water",
            "soil"
        ]):
            skills.extend([
                "IoT"
            ])

            technologies.extend([
                "Soil Sensors",
                "IoT",
                "Smart Irrigation"
            ])

        if any(word in text for word in [
            "crop",
            "pest",
            "disease"
        ]):
            technologies.extend([
                "Computer Vision",
                "Machine Learning"
            ])

    # Healthcare
    elif domain == "Healthcare":

        skills.extend([
            "Healthcare Management",
            "Data Science"
        ])

        if any(word in text for word in [
            "hospital",
            "doctor",
            "patient",
            "clinic"
        ]):
            technologies.extend([
                "Telemedicine",
                "Cloud Computing"
            ])

        if any(word in text for word in [
            "disease",
            "infection",
            "outbreak"
        ]):
            skills.append("Epidemiology")

            technologies.extend([
                "Predictive Analytics",
                "Data Visualization"
            ])

    # Education
    elif domain == "Education":

        skills.extend([
            "Education Technology",
            "Software Development"
        ])

        if any(word in text for word in [
            "internet",
            "computer",
            "digital",
            "online"
        ]):
            technologies.extend([
                "Cloud Computing",
                "Learning Management Systems"
            ])

        if any(word in text for word in [
            "school",
            "classroom",
            "building"
        ]):
            skills.append("Civil Engineering")

    # Water & Sanitation
    elif domain == "Water & Sanitation":

        skills.extend([
            "Environmental Engineering",
            "Civil Engineering"
        ])

        technologies.extend([
            "Water Quality Sensors",
            "IoT"
        ])

        if any(word in text for word in [
            "contaminated",
            "pollution",
            "dirty"
        ]):
            skills.append("Data Science")

            technologies.append(
                "Water Quality Analytics"
            )

    # Environment
    elif domain == "Environment":

        skills.extend([
            "Environmental Science",
            "Data Science"
        ])

        if any(word in text for word in [
            "waste",
            "garbage",
            "trash"
        ]):
            technologies.extend([
                "Smart Waste Monitoring",
                "IoT"
            ])

        if any(word in text for word in [
            "pollution",
            "air quality"
        ]):
            technologies.extend([
                "Air Quality Sensors",
                "Data Analytics"
            ])

    # Default for unknown domains
    else:

        skills.extend([
            "Problem Analysis"
        ])

        technologies.extend([
            "Data Analytics"
        ])

    # Remove duplicates while preserving order
    skills = list(dict.fromkeys(skills))
    technologies = list(dict.fromkeys(technologies))

    # Estimate cost
    if any(word in text for word in [
        "sensor",
        "iot",
        "gis",
        "drone",
        "monitoring"
    ]):
        estimated_cost = "medium"

    elif any(word in text for word in [
        "bridge",
        "hospital",
        "building",
        "large"
    ]):
        estimated_cost = "high"

    else:
        estimated_cost = "low"

    # Calculate scalability
    scalability = 50

    scalable_words = [
        "village",
        "district",
        "multiple",
        "many",
        "region",
        "state",
        "community"
    ]

    for word in scalable_words:
        if word in text:
            scalability += 8

    if "iot" in technologies:
        scalability += 10

    if "data analytics" in [
        tech.lower()
        for tech in technologies
    ]:
        scalability += 5

    scalability = min(scalability, 100)

    return {
        "skills": skills,
        "technologies": technologies,
        "estimated_cost": estimated_cost,
        "scalability": scalability
    }