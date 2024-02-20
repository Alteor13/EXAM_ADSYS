# Auteur : Martin CHARRONDIERE

Troisieme version de game_target

# Contenu du projet

Package Game : Contient l'essentiel du code, module instalable avec setup.py (voir README associe)
Dossier Images : Contient quelques images d'illustration

setup.py : Permet l'instalation du package Game en local.

# Principe

Le programme principal game_target_v3.py permet de modeliser une interraction entre un robot et une cible.
Au debut du jeu, une cible est placee aleatoirement sur une grille de 5 par 5, et le robot va evoluer sur cette meme grille jusqu'a arriver sur la case occupee par la cible. S'il y parvient en moins de 1000 tours, le robot gagne !

# Fonctionnement

Le robot parvient systematiquement à trouver la cible, mais l'affichage ne permet pas vraiment de comprendre le principe du jeu sans en avoir lu le code prealablement. De meme, l'utilisateur n'est pas guide du tout.

# Illustrations

Affichage de la grille lorsque le robot a trouve la cible (une case est alors simultanement occupee par les deux entites)
(Images/Reussi.png)

Affichage de la grille lorsque le robot et la cible sont sur deux cases differentes
(Images/Rate.png)

# Usage (eventuel) de venv

Pas d'utilisation d'environnement virtuel dans ce ca là.

# Organisation du module

Package Game créé, contenant le programme principal game_target_v3.py ainsi que le programme test.py permettant d'effectuer une batterie de test sur le premier programme.

# Tests & gestion des erreurs

Mise en place des tests dans le programme test.py, du package Game.
Aucune erreur detectee dans les tests depuis le debut.

# Modifications apportees par rapport a la version precedente

Correction du code game_target_v3 :

    - Le robot ne peux desormais plus etre place à l'exterieur de la grille
    
    - Modification du contenu de la grille depend d'une nouvelle fonction mov
    permettant de securiser le processus d'edition

    - La modification de la grille n'est plus dependante de son affichage

    - Correction du code conformement a la norme pep8 (addition de docstrings sur toutes les fonctions et classes, nettoyage et epuration de la structure du code, suppressio de normes inutiles, etc...)

# Installation du package Game : 

Dans le terminal, sous une distribution linux, entrer la commande : 

```bash
pip install /chemin/vers/votre/package/dist/nom_de_votre_package-1.0.0.tar.gz
```
Pour Windows :

```bash
pip install C:\chemin\vers\votre\package\dist\nom_de_votre_package-1.0.0.tar.gz
```

# Automatisation des phases de test

Non implementee pour le moment.

# Structure de l'arborescence

Choix fait de créer une branche develop pour ne pas poluer la branche main lors de la création de l'arborescence nécessaire à la création d'un package et de l'implémentation de nouveaux éléments (images d'illustration, batterie de test, etc...).