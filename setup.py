import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="telegram-cloud",
    version="1.3.4",
    description="Download and upload files via telegram up to 1.5GB, CLI",
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
    install_requires=["telethon","cryptg"],
    packages=["telegramcloud","telegramcloud.scripts", "telegramcloud.utils"],
    entry_points={
        "console_scripts": [
            "tgcloud = telegramcloud.__main__:cli",
            "tglogin = telegramcloud.add_session:cli",
            "tginfo = telegramcloud.scripts.tginfo:cli",
            "tgsend = telegramcloud.scripts.tgsend:cli",
        ]
    },
)