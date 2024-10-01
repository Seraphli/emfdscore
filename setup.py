from setuptools import setup

setup(
    name="emfdscore",
    version="0.0.1",
    description="Extended Moral Foundation Dictionary Scoring for Python",
    url="https://github.com/medianeuroscience/emfdscore",
    author="Anonymized.",
    author_email="fhopp@ucsb.edu",
    license="MIT",
    packages=["emfdscore"],
    scripts=["bin/emfdscore"],
    include_package_data=True,
    install_requires=[
        "spacy==3.7.5",
        "pandas==2.2.3",
        "progressbar2",
        "nltk==3.9.1",
        "numpy==1.26.4",
        "scikit-learn==1.5.2",
    ],
    zip_safe=False,
)
