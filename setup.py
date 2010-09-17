from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='plone.formwidget.querystring',
      version=version,
      description="A widget for composing a Query string/search (used for " \
                  "the contentlisting tile)",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Kim Chee Leong, Ralph Jacobs, Jonas Baumann',
      author_email='leong@gw20e.com, ralph@fourdigits.nl, ' \
                   'j.baumann@4teamwork.ch',
      url='http://svn.plone.org/svn/plone/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.formwidget'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.collection',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
          [z3c.autoinclude.plugin]
          target = plone
      """,
      )
