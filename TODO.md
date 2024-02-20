## Propositions pour la v3

# Algorithmes de rechercher pour le robot :

- Aleatoire pur (methode actuellement implementee)

Strategie tres simple a implementer mais particulierement inefficace, le robot ratant parfois la cible a de nombreuses reprises...

- Recherche en spirale : Le robot se positionne sur l'un des quatre coins de la grille, puis en longe les bordures. S'il ne trouve rien a la fin de son premier tour, il recommence sur la bordure concentrique de rayon n-1, et ainsi de suite.

Cette methode garantie que le robot trouve la cible en un nombre de coup suffisamment permissif, en l'occurence, si le nombre de coup est superieur au nombre de cases sur la grille.

Exemple pour une grille de taille 3 : 1 2 3
                                      8 9 4
                                      7 6 5

- Recherche par colonne (ou equivalent par ligne) : Le robot parcourt chaque colonne/ligne dans un sens puis la suivante dans le sens inverse, jusqu'a avoir parcouru l'integralite de la grille.

A nouveau, cette methode garantie que le robot trouve la cible en un nombre de coup suffisamment permissif, en l'occurence, si le nombre de coup est superieur au nombre de cases sur la grille.


Exemple par ligne pour une grille de taille 3 : 1 2 3
                                                6 5 4
                                                7 8 9

Exemple par colonne pour une grille de taille 3 : 1 6 7
                                                  2 5 8
                                                  3 4 9

Malheureusement, comme le placement de la cible est rigoureusement aleatoire, il est impossible de creer des algorithmes plus pousses pour ameliorer les performances du robot, car ce dernier ne peut donc pas avoir de strategie a proprement parler.

# Ameliorations du programme

- On pourrait veiller à ce que le robot et la cible ne soient pas positionnes d'emblee au meme endroit (la partie manque alors cruellement d'interet...)

- De meme, on peut envisager qu'une IA se charge de reperer les motifs recurrents dans le mouvement du robot (pour peu qu'il utilise un algorithme de recherche non aleatoire comme evoque plus haut) et adapte la position de la cible pour qu'elle soit trouvee le plus tard possible.