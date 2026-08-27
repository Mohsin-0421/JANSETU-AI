import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    PROJECT_NAME = "JANSETU Intelligence Engine"

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )


settings = Settings()