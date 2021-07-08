import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="db_model",
    version="0.0.0",
    author="Darkborderman",
    author_email="reastw1234@gmail.com",
    description="DB model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/19gale.ai/tap-common-modules",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'sqlalchemy>=1.3.0',
    ],
    python_requires='>=3.8',
)
