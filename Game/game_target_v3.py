"""Code principal : modelisation d'une grille, d'un robot et d'un objet game
 pour lancer une partie"""
# -*- coding: cp1252 -*-
import random

class Grid:
    """Classe modelisant la grille"""

    def __init__(self, width, height):
        """Constructeur de la classe
        @param widht et height, les dimensions de la grille
        @return /
        """
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def display(self):
        """Affiche la grille
        @param /
        @return / 
        """
        for row in self.grid:
            print(' | '.join(row))
            print('-' * (4 * self.width - 1))

    def clear(self):
        """ Remplie la grille par des caracteres vides 
        en vue d'un eventuel remplissage
        @param /
        @return / 
        """
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def mov (self,ry,rx,ty,tx):
        """Insere les caracteres R et x aux positions respectives
        du robot et de la cible
        @param ry et rx, les coordonees du robot
        ty et tx les coordonees de la cible
        @return /
        """
        self.grid[ry][rx] = 'R'
        self.grid[ty][tx] = 'X'

class Robot:
    """Classe modelisant le robot charge de trouver la cible"""

    def __init__(self, x, y):
        """Consructeur de la classe
        @param x et y, les coordonnees du robot au depart
        @return /
        """
        self.x = x
        self.y = y

    def move_up(self):
        """Permet au robot de se deplacer vers le haut
        @param /
        @return /
        """
        if self.y > 0:
            self.y -= 1

    def move_down(self, grid_height):
        """Permet au robot de se deplacer vers le bas
        @param grid_height, la hauteur de la grille
        @return /
        """
        if self.y < grid_height - 1:
            self.y += 1

    def move_left(self):
        """Permet au robot de se deplacer vers la gauche
        @param /
        @return /
        """
        if self.x > 0:
            self.x -= 1

    def move_right(self, grid_width):
        """Permet au robot de se deplacer vers la droite
        @param grid_width, la largeur de la grille
        @return /
        """
        if self.x < grid_width - 1:
            self.x += 1

    def check_pos_robot (self,g):
        """
        @param une grille g
        @return /
        """
        if (self.x > (g.width-1)) or (self.y > (g.height-1)) :
            self.x = 1
            self.y = 1

class Game:
    """Classe modelisant un objet game (la partie en cours)"""

    def __init__(self, g, r, max_steps=1000, show_grid=False):
        """Constrcuteur de la classe
        @param une grille grid, un robot robot, max_steps le nombre maximal
        de tour a jouer et show_grid un booleen permettant d'afficherla grille
        @return /
        """
        self.grid = g
        self.robot = r
        self.show_grid = show_grid
        self.max_steps = max_steps
        self.steps = 0  # Nombre d'�tapes pour atteindre la cible
        self.place_target()
        self.target_reached = False

    def place_target(self):
        """Determine la position de la cible pour la partie
        @param /
        @return /
        """
        self.target_x = random.randint(0, self.grid.width - 1)
        self.target_y = random.randint(0, self.grid.height - 1)
        self.grid.grid[self.target_y][self.target_x] = 'X'  # Marquer la cible dans la grille

    def check_collision(self):
        """Verifie si le robot et la cible sont superposes
        @param /
        @return True ou False selon que le robot et la cible sont au meme*
        endroit ou non
        """
        if self.robot.x == self.target_x and self.robot.y == self.target_y:
            return True
        return False

    def run_turn(self):
        """Deroulement d'un tour
        @param /
        @return True ou False selon que la cible a ete atteinte ou non
        """
        # V�rifier si la cible a d�j� �t� atteinte
        if self.target_reached:
            return True

        # V�rifier si le nombre d'�tapes a d�pass� la limite
        if self.steps >= self.max_steps:
            return False

        # D�placement du robot
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            self.robot.move_up()
        elif direction == 'down':
            self.robot.move_down(self.grid.height)
        elif direction == 'left':
            self.robot.move_left()
        elif direction == 'right':
            self.robot.move_right(self.grid.width)

        # Affichage de la grille apr�s le d�placement du robot
        if self.show_grid:
            self.grid.clear()
            self.grid.mov(self.robot.y,self.robot.x,self.target_y,self.target_x)
            self.grid.display()

        # V�rification si le robot touche la cible
        self.steps += 1
        if self.check_collision():
            self.target_reached = True
            return True
        return False

if __name__ == "__main__":

    # Cr�ation de la grille et du robot
    grid = Grid(5, 5)
    robot = Robot(10, 10)
    robot.check_pos_robot(grid)

    # Cr�ation du jeu avec l'option d'affichage de la grille et une limite d'�tapes
    game = Game(grid, robot, max_steps=1000, show_grid = True)

    # Execution des tours de jeu jusqu'e ce que le robot touche la cible
    # ou que la limite d'etapes soit depassee
    while not game.run_turn():
        pass

    # Verification si le robot a atteint la cible ou non et affichage du message approprie
    if game.target_reached:
        print("Felicitations ! Le robot a atteint la cible en {} etapes.".format(game.steps))
    else:
        print("Le robot n'a pas reussi a atteindre la cible dans le nombre maximum d'etapes.")
