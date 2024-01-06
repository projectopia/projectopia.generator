from setuptools import find_packages, setup

setup(
    name="backend",
    packages=find_packages(exclude=["backend_tests"]),
    install_requires=[
        "Flask==3.0.0",
        "multiprocessing",
        "gunicorn", # for deployment
        "flask-restx", # Modern version of flask-restful
    ],
    extras_require={"dev": []},
)
