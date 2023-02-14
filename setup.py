import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aicloudx",
    version="0.0.3",
    author="cui dong",
    author_email="cuidong008@126.com",
    description="用于配合云平台进行模型训练",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cuidong008/aicloud",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)