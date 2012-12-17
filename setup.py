from setuptools import setup, find_packages
import os

version = '1.0.2'

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
        "Programming Language :: Python",
    ],
    keywords='',
    author='',
    author_email='',
    url='http://svn.plone.org/svn/collective/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.intid',
        'zope.app.intid',
        'zope.lifecycleevent',
        'five.intid>=1.0',
        'Products.CMFCore',
        # -*- Extra requirements: -*-
    ],
    extras_require={
        'test': ['plone.app.testing'],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
