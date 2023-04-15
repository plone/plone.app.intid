from setuptools import find_packages
from setuptools import setup

import os


version = "2.0.1.dev0"

setup(
    name="plone.app.intid",
    version=version,
    description="Installation and migration support for five.intid within " "Plone/CMF",
    long_description="{}\n{}".format(
        open("README.rst").read(),
        open(os.path.join("CHANGES.rst")).read(),
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="plone zope five intid",
    author="Alec Mitchell",
    author_email="apm13@columbia.edu",
    url="https://github.com/plone/plone.app.intid",
    license="GPL",
    packages=find_packages(),
    namespace_packages=["plone", "plone.app"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "zope.intid",
        "zope.lifecycleevent",
        "five.intid>=1.0",
        "Products.CMFCore",
        "Products.GenericSetup",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.dexterity",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
