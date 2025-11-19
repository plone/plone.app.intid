from pathlib import Path
from setuptools import setup


version = "3.0.0a1.dev0"

long_description = (
    f"{Path('README.rst').read_text()}\n{Path('CHANGES.rst').read_text()}"
)

setup(
    name="plone.app.intid",
    version=version,
    description="Installation and migration support for five.intid within " "Plone/CMF",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Core",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="plone zope five intid",
    author="Alec Mitchell",
    author_email="apm13@columbia.edu",
    url="https://github.com/plone/plone.app.intid",
    license="GPL",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "five.intid>=1.0",
        "Products.CMFCore",
        "Products.GenericSetup",
        "zope.component",
        "zope.intid",
        "zope.lifecycleevent",
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
