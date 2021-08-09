from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="create-flask-api-app",
    version="0.0.2",
    description="Creates python flask API application template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ElvisRodriguez/create-flask-api-app",
    author="Elvis Rodriguez",
    author_email="elvisrodriguez1992@gmail.com",
    license="MIT",
    project_urls={
        "Bug Tracker": "https://github.com/ElvisRodriguez.create-flask-api-app/issues",
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Code Generators",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
    install_requires=[
        "flask",
        "flask_restful",
        "SQLAlchemy"
    ],
)