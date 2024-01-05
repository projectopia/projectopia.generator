from setuptools import find_packages, setup

setup(
    name="backend",
    packages=find_packages(exclude=["backend_tests"]),
    install_requires=[
        "Flask==3.0.0",
        "uvicorn",
    ],
    extras_require={"dev": []},
)
