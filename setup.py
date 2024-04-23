from setuptools import setup, find_packages

setup(
    name = "UA2C",
    version = "0.8",
    packages = find_packages(),
    install_requires = ["beautifulsoup4", "deprecated", "matplotlib", "mysql-connector-python", "numpy", "pandas",
                        "Pillow", "python-telegram-bot","requests", "scikit-learn", "selenium", "statsmodels",
                        "tensorflow==2.16.1", "tf-keras", "transformers", "tqdm"
        ],
    package_data = {"UA2C": ["fonts/DejaVuSerifCondensed-Italic.ttf"]},
    author = "Lekker",
    author_email = "NoneType@NotCallable.com",
    description = "General use functions used in UA2C project."
)
