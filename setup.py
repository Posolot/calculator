from setuptools import setup, find_packages

setup(
    name='calculator',
    version='1.0.1',
    description='Utility for performing simple mathematical operations',
    long_description='https://github.com/Posolot/calculator',
    author='Ilya Kuzmin',
    author_email='saharokbro@mail.ru',
    url='https://github.com/Posolot/calculator',
    packages=find_packages(),
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
    python_requires='>=3.6',
)

