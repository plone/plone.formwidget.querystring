from setuptools import setup, find_packages

version = '1.1.0'

long_description = open("README.rst").read() + "\n" + \
    open("CHANGES.rst").read()

setup(
    name='plone.formwidget.querystring',
    version=version,
    description="A widget for composing a Query string/search.",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/plone.formwidget.querystring',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone', 'plone.formwidget'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.querystring',
    ],
    entry_points="""
    # -*- Entry points: -*-
        [z3c.autoinclude.plugin]
        target = plone
    """,
)
