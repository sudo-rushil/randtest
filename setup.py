from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'PREADME.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'randtest',         # How you named your package folder (MyLib)
  packages = ['randtest'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Quick and accurate determinations of the randomness of a sequence',   # Give a short description about your library
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Rushil Mallarapu',                   # Type in your name
  author_email = 'rushil.mallarapu@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/sudo-rushil/randtest',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sudo-rushil/randtest/archive/v0.3.tar.gz',    # I explain this later on
  keywords = ['random', 'sequence', 'algorithm', 'numpy', 'randomness', 'arrays', 'np', 'test', 'random test', 'randomness test', 'randtest'],
  include_package_data=True,
  install_requires=[            # I get to this in a second
          'numpy',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ])