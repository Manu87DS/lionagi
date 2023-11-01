import setuptools
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the code version
version = {}
with open(os.path.join(here, "lionagi/version.py")) as fp:
    exec(fp.read(), version)
__version__ = version["__version__"]

install_requires = [
    "aiohttp",
    "python-dotenv",
    "tiktoken"
]


setuptools.setup(
    name="lionagi",
    version=__version__,
    author="LionAGI",
    author_email="ocean@lionagi.ai",
    description="Powerful intelligent workflow automation.",
    packages=setuptools.find_packages(include=["lionagi*"]),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.10",
)
