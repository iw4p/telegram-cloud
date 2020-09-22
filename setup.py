import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="telegram-cloud-IW4P", # Replace with your own username
    version="1.0.0",
    author="Nima Akbarzade",
    author_email="Nimakbarzade@yahoo.com",
    description="Download and upload files via telegram CLI, Maximum 1.5GB",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iw4p/telegram-cloud",
    packages=setuptools.find_packages(),
      entrypoints={
    'console_scripts': [
      'telegram-cloud = main:main',
    ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='README.md',
    install_requires=[
       "telethon",
   ],
    python_requires='>=3.6',
)