from setuptools import setup

requirements = [
    'requests',
]

test_requirements = requirements + [
    'flake8',
    'mypy',
]

setup(
    name='cryptoportfolio',
    version='0.1',
    packages=[
        'cryptoportfolio',
        'cryptoportfolio.lib',
        'cryptoportfolio.utils',
        'cryptoportfolio.wallets',
        'cryptoportfolio.miningpools',
    ],
    url='',
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
