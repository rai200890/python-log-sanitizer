from setuptools import setup

__VERSION__ = "0.0.1"

setup(
    name="python_log_sanitizer",
    version=__VERSION__,
    description="Log Sanitizer",
    url="http://github.com/rai200890/python_log_sanitizer",
    author="Raissa Ferreira",
    author_email="rai200890@gmail.com",
    license="MIT",
    packages=["python_log_sanitizer"],
    python_requires=">=3.4.*",
    install_requires=[],
    classifiers=[
        "Environment :: Web Environment", "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English", "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Logging"
    ],
    zip_safe=False)
