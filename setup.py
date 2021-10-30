import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BunnyUtils",
    version="1.3.4",
    author="Senpai",
    description="BunnyUtils is a very useful library made to be used for senpai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/senpai-development/BunnyUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.6",
    include_package_data=True,
    install_requires=["senpai"],
    extras_require={"voice": ["senpai[voice]", "youtube-dl"]}
)
