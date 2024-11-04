from setuptools import find_packages, setup

setup(
    name="stlite-chat",
    packages=find_packages(
        include=[
            "src",
            "src.*",
        ]
    ),
)
