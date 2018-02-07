from setuptools import setup

version = '0.2.1'

requirements = [
    'requests',
    'monotable',
    'PyYAML==3.12'
]

test_requirements = requirements + [
    'flake8',
    'mypy',
]

setup(
    name='cryptoportfolio',
    version=version,
    packages=[
        'cryptoportfolio',
        'cryptoportfolio.interfaces',
        'cryptoportfolio.interfaces.miningpools',
        'cryptoportfolio.interfaces.wallets',
        'cryptoportfolio.cli',
        'cryptoportfolio.lib',
        'cryptoportfolio.utils',
    ],
    url='https://github.com/a1fred/cryptoportfolio',
    entry_points={
        'console_scripts': ['cryptoportfolio=cryptoportfolio.main:cli'],
    },
    license='MIT',
    author='a1fred',
    author_email='demalf@gmail.com',
    description='Show your coins portfolio',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
    ],
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite="tests",
)
