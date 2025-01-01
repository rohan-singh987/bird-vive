from setuptools import setup, find_packages

setup(
    name="BirdVive",
    version="0.0.1",
    author="Rohan",
    description="A bird sound classification project",
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'tqdm',
        'notebook',
        'python-box==6.0.2',
        'pyyaml',
        'types-PyYAML',
        'Flask',
        'Flask-Cors',
        'dvc',
        'joblib',
        'scipy',
        'ensure==1.0.2'
    ]
)
