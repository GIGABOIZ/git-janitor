from setuptools import setup

setup(
    name='git-janitor',
    version='1.0.0',
    description='A smart CLI tool to sweep away stale and merged git branches.',
    author='Your GitHub Username',
    py_modules=['janitor'], 
    entry_points={
        'console_scripts': [
            'git-janitor=janitor:main', 
        ],
    },
)
