from setuptools import setup, find_packages

setup(
    name = 'TarjanPlanner',
    version = '1.0',
    author='YoungbinLim',
    author_email='0429lyb@gmail.com',
    packages=find_packages(),
    description="",
    entry_points={'console_scripts':['tarjan-planner=main:main']}
)