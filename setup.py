from setuptools import setup, find_packages

setup(
    name = "UA2C",
    version = "0.2",
    packages = find_packages(),
    install_requires = ["matplotlib", "numpy", "pandas", "scikit-learn", "statsmodels", "mysql-connector-python",
                        "Pillow", "selenium", "python-telegram-bot"],
    author = "Lekker",
    author_email = "NoneType@NotCallable.com",
    description = "General use functions used in UA2C project."
)
