#!/usr/bin/env python
import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with io.open("requirements.txt") as f:
    required = f.read().splitlines()

with io.open("Readme.md", encoding="utf-8") as f:
    long_description = f.read()

def main():
    setup(
        name='jira_ithillel_pageobject',
        version='1.0',
        description='My Package Description',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/IshchukI/Lesson26DZ',
        author='Iaroslav Ishchuk',
        author_email='contact@demo.com',
        packages=['src_pages',
                  'src_pages.pages'],
        install_requires=required,
        include_package_data=True,
        keywords="mypackage for product test",

    )


if __name__ == '__main__':
    main()
