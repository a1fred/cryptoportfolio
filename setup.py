from setuptools import setup
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip


pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)

setup(
    name='cryptoportfolio',
    version='0.1',
    packages=['cryptoportfolio', ],
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
