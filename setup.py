from setuptools import setup, find_packages

setup(
        name = "scriptutils",
        version = "0.1.0",
        description = "Utility functions for creating scripts.",
        author = "Martin Norbury",
        author_email = "martin.norbury@gmail.com",
        packages = find_packages('src'),
        package_dir = {'':'src'},
        test_suite="nose.collector",
        install_requires = []
     )
