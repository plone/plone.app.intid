from setuptools import setup, find_packages
import os

version = '1.1.4.dev0'

setup(
    name='plone.app.intid',
    version=version,
    description="Installation and migration support for five.intid within "
                "Plone/CMF",
    long_description='%s\n%s' % (
        open("README.rst").read(),
        open(os.path.join("CHANGES.rst")).read(),
    ),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='plone zope five intid',
    author='Alec Mitchell',
    author_email='apm13@columbia.edu',
    url='https://github.com/plone/plone.app.intid',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.intid',
        'zope.lifecycleevent',
        'five.intid>=1.0',
        'Products.CMFCore',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.dexterity',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
