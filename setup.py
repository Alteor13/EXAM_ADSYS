"""Installation du module avec ses dependances"""

from setuptools import setup, find_packages

setup(
    name='Game',
    version='1.0.0',
    packages=find_packages(),
    author='Martin_CHARONDIERE',
    author_email='martin.charrondiere@cpe.fr',
    install_requires=[
        'random',
        # Ajoutez ici toutes les dépendances nécessaires pour votre package
    ],
)
