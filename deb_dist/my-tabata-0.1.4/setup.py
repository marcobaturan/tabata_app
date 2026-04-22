from setuptools import setup, find_packages

setup(
    name="my-tabata",  # Sugiero añadir "Timer" para evitar conflictos de nombres comunes
    version="0.1.4",
    packages=find_packages(),
    include_package_data=True,
    # Asegúrate de que los nombres coincidan exactamente con como aparecen en PyPI
    install_requires=[
        "text-unidecode",
        "ttkbootstrap",
        "typing-extensions", # Corregido de typing_extensions
        "tzdata",
        "urllib3",
        "uvicorn",
        "uvloop; platform_system != 'Windows'", # uvloop no funciona en Windows, mejor prevenir
        "watchdog",
        "watchfiles",
        "websockets",
        "just_playback"
    ],
    entry_points={
        'console_scripts': [
            # Formato: 'comando-a-ejecutar=carpeta_codigo.archivo:funcion'
            'my-tabata=my_tabata.app:main_func',
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
    python_requires='>=3.9',
    setup_requires=['stdeb'],
)