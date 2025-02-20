from setuptools import setup, find_packages

setup(
    name="Cognitive_Activity_Recommendation_System",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "sqlalchemy",
        "pandas",
        "psycopg2",
        "requests",
        "pickle"
    ],
)
