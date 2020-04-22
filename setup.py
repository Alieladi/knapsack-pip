from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='knapsack-pip',
      version='0.1',
      description='Knapsack problem solver',
      long_description=long_description,
      url='https://github.com/Alieladi/knapsack-pip',
      author="Ali El Adi",
      author_email="alieladi@gmail.com",
      classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
        ],
      keywords='knapsack backpack',
      packages=['solvers'],
      python_requires='>=3'
      zip_safe=False)
