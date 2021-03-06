import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yaaade",
    version="0.0.1",
    author="Thomas Parry",
    description="A collection of analogue design tools",
    url="https://github.com/yrrapt/yaaade",
    project_urls={
        "Bug Tracker": "https://github.com/yrrapt/yaaade/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)