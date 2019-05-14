from setuptools import setup

version = '0.3.7'

requirements = [
    'requests',
    'monotable',
    'pyyaml>=4.2b1',
]


setup(
    name='cryptoportfolio',
    version=version,
    packages=[
        'cryptoportfolio',
        'cryptoportfolio.interfaces',
        'cryptoportfolio.interfaces.miningpools',
        'cryptoportfolio.interfaces.wallets',
        'cryptoportfolio.interfaces.exchanges',
        'cryptoportfolio.cli',
        'cryptoportfolio.lib',
        'cryptoportfolio.lib.convert',
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
        'Topic :: Office/Business :: Financial',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=requirements,
    test_suite="tests",
)
