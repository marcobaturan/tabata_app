from setuptools import setup, find_packages

setup(
    name="Py-tabata",
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Lista aquí tus dependencias de PyPI, ej:
        # "PyQt6", "pygame",
    ],
    entry_points={
        'console_scripts': [
            # this builds the command "my-tabata" in /usr/bin/ automatic
            'my-tabata=my_tabata.main:main_func',
        ],
    },
    data_files=[
        ('share/applications', ['my_tabata.desktop']),
        ('share/icons/hicolor/scalable/apps', ['icon.svg']),
    ],
    author="Marco Baturan",
    description="Timer Tabata for XFCE in Debian",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/marcobaturan/tabata_app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)