from setuptools import setup, find_packages

setup(
    name='calculator',
    version='1.0',
    description='Utility for performing simple mathematical operations',
    author='Ilya Kuzmin',
    author_email='saharokbro@mail.ru',
    url='https://github.com/Posolot/calculator',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calculator = calculator:main',
        ],
    },
    python_requires='>=3.6',
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)

