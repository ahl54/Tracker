from setuptools import setup

setup(name='data_tracker',
      version='1.0',
      description="An application for tracking data requests",
      long_description="",
      author='Anna Lu',
      author_email='lua1@email.chop.edu',
      license='MIT License',
      packages=['data_tracker'],
      zip_safe=False,
      install_requires=[
          'Django',
          'Sphinx',
          # requirements to be added
          ],
      )
