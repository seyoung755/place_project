from setuptools import setup, find_packages

setup(
    name='Flask-CI-Example',
    packages=find_packages(),
    version='0.1',
    long_description=__doc__,
    zip_safe=False,
    test_suite='nose.collector',
    include_package_data=True,
    install_requires=[
        'certifi==2020.12.5',
        'chardet==4.0.0',
        'click==7.1.2',
        'Flask==1.1.2',
        'Flask-Cors==3.0.10',
        'idna==2.10',
        'itsdangerous==1.1.0',
        'Jinja2==2.11.3',
        'MarkupSafe==1.1.1',
        'requests==2.25.1',
        'six==1.15.0',
        'urllib3==1.26.3',
        'Werkzeug==1.0.1'

    ]
)