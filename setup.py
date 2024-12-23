from setuptools import setup, find_packages

setup(
    name="flet_mobile_preview",
    version="1.0.1",
    packages=find_packages(include=["flet_mobile_preview", "flet_mobile_preview.*"]),
    description="A simple phone preview for Flet applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Victoire Kitenge",
    author_email="yumakitenge243@gmail.com",
    url="https://github.com/Victoire243/flet-phone-preview.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["flet"],
    package_data={
        "flet_mobile_preview": ["assets/*", "assets/*/*", "assets/*/*/*"],
    },
)
