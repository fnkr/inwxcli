from setuptools import setup

setup(name='inwxcli',
      version='1.1',
      description='Command line interface for inwx.com.',
      url='https://github.com/fnkr/inwxcli',
      author='Florian Kaiser',
      author_email='florian.kaiser@fnkr.net',
      license='MIT',
      packages=['inwxcli'],
      entry_points = {
          'console_scripts': [
              'inwxcli = inwxcli.inwxcli:main',
          ],              
      },
      zip_safe=False)

