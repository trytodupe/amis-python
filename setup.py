from setuptools import setup, find_packages

setup(
    name="amis-python",
    version="1.0.9",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "amis": ["templates/*.jinja2"],
    },
    install_requires=[
        "pydantic>=2.0.0,<3.0.0",
        "jinja2>=3.1.2,<4.0.0"
    ],
)
