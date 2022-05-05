from setuptools import setup

setup(
    name='CreaTeBME',
    version='0.1',
    description='Python Package for interfacing the bluetooth IMU module for CreaTe M8 BME.',
    url='https://github.com/CreaTe-M8-BME/CreaTeBME',
    author='Jonathan Matarazzi',
    author_email='dev@jonathanm.nl',
    license='MIT',
    packages=['CreaTeBME'],
    install_requires=[
        'scipy',
        'numpy',
        'serial',
        'pybluez',
        'prompt_toolkit',
    ],
    zip_safe=False,
)
