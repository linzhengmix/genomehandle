from setuptools import setup, find_packages

setup(
    name="handle_genome",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    entry_points={
        'console_scripts': [
            'process_archaea=handle_genome.handle_archaea:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A package to handle genome data processing.",
    url="https://github.com/yourusername/handle_genome",
)
