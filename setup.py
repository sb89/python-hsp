from setuptools import setup, find_packages

setup(
    name='hsp',
    version='0.1.0',
    packages=find_packages(),
    license='MIT',
    zip_safe=False,
    install_requires=[
        'requests >= 2.0'
    ],
    tests_require=[
        'responses ~= 0.10.5'
    ]
)
