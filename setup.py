from setuptools import find_packages, setup

setup(
    name='graphenize',
    version='0.1.0',

    description='Auto-generation Graphene models from json.',

    url='https://github.com/abawchen/graphenize',

    author='Abaw Chen',
    author_email='abaw.chen@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    keywords='graphql json rest api graphene schema graphenize',

    packages=find_packages(exclude=['tests']),

    install_requires=[
        'Click',
        'genson',
        'graphene >=2.0',
        'textblob'
    ],
    entry_points='''
        [console_scripts]
        graphenize=graphenize.cli:cli
    ''',
    python_requires='>=2.7',
    zip_safe=True,
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest>=3.3.2',
    ],
    test_suite="tests",

)

