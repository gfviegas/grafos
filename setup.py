from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='graph',
    version='1.0',
    description='TP de Grafos, UFV Florestal',
    url='http://github.com/gfviegas/graph',
    author='Gustavo Viegas, Lucas Duarte',
    author_email='gustavo.viegas@ufv.br lucas.duarte@ufv.br',
    license='Apache',
    packages=['graph', 'memoize'],
    install_requires=[
        'numpy',
        'pytest',
        'sphinx_rtd_theme',
        'sphinxcontrib-fulltoc'
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    include_package_data=True,
    zip_safe=False
)
