import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="FoodApi",
    version="1.0.0",
    url="https://github.com/dleng2242/food_api",
    license="MIT",
    maintainer="Duncan Leng",
    description="The basic blog app built in the Flask tutorial.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask", "flask_restful"],
    extras_require={"test": ["pytest", "coverage"]},
)