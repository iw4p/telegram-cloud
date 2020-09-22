# import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

# setuptools.setup(
#     name="telegram-cloud-IW4P",
#     version="1.0.0",
#     author="Nima Akbarzade",
#     author_email="Nimakbarzade@yahoo.com",
#     description="Download and upload files via telegram CLI, Maximum 1.5GB",
#     long_description_content_type="text/markdown",
#     url="https://github.com/iw4p/telegram-cloud",
#     packages=setuptools.find_packages(),
#     scripts=[bin],
#     entrypoints={
#     'console_scripts': [
#       'telegram-cloud = main:main',
#     ]},
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     license='LICENSE',
#     install_requires=[
#        "telethon",
#    ],
#     python_requires='>=3.6',
# )

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="telegram_cloud",
    version="1.0.11",
    description="Download and upload files via telegram CLI, Maximum 1.5GB",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/iw4p/telegram-cloud",
    author="Nima Akbarzade",
    author_email="Nimakbarzade@yahoo.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["telethon"],
    packages=["telegram_cloud",],
    entry_points={
        "console_scripts": [
            "tgcloud = telegram_cloud.__main__:main",
        ]
    },
)