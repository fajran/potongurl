from setuptools import setup, find_packages

setup(
    name = "potongurl",
    version = "1.0",
    url = 'http://github.com/fajran/potongurl/',
    license = 'BSD',
    description = 'Pemendek URL',
    author = 'Fajran Iman Rusadi',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)

