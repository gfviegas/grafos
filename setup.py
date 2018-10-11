from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='graph',
    version='0.1',
    description='The best graph library out there',
    url='http://github.com/gfviegas/graph',
    author='Gustavo Viegas, Lucas Duarte',
    author_email='gustavo.viegas@ufv.br lucas.duarte@ufv.br',
    license='Apache',
    packages=['graph'],
    install_requires=[
        'numpy',
        'pytest'
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    include_package_data=True,
    zip_safe=False
)
