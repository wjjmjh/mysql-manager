from setuptools import setup, find_packages

setup(
    name="mysql-manager",
    version="0.0",
    description="Manage MySQL database.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mysql-connector-python",
    ],
    extras_require={"dev": [
        "pytest",
        "tox",
        "black",
        "isort",
    ]},
)
