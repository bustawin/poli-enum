from pathlib import Path

from setuptools import find_packages, setup

test_requires = ['pytest']

setup(
    name='poli-enum',
    version='1.0',
    url='https://github.com/bustawin/poli-enum',
    project_urls={
        'Documentation': 'https://github.com/bustawin/poli-enum',
        'Code': 'https://github.com/bustawin/poli-enum',
        'Issue tracker': 'https://github.com/bustawin/poli-enum/issues'
    },
    license='AGPLV3',
    author='Xavier Bustamante Talavera',
    author_email='xavier@bustawin.com',
    description='Political enums: continent, country (ISO 3166-1), subdivision (ISO 3166-2), '
                'currency (ISO 4217) and keyboard layouts (debian).',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    long_description=Path('README.rst').read_text('utf8'),
    extras_require={
        'test': test_requires
    },
    tests_require=test_requires,
    setup_requires=[
        'pytest-runner'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
