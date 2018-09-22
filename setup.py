from setuptools import setup

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
        'markdown',
    ],
    zip_safe=False
)
