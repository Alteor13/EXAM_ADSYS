# -*- coding: cp1252 -*-
import random

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def display(self):
        for row in self.grid:
            print(' | '.join(row))
            print('-' * (4 * self.width - 1))

    def clear(self):
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, grid_height):
        if self.y > 0:
            self.y -= 1

    def move_down(self, grid_height):
        if self.y < grid_height - 1:
            self.y += 1

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self, grid_width):
        if self.x < grid_width - 1:
            self.x += 1

class Game:
    def __init__(self, grid, robot, max_steps=1000, show_grid=False):
        self.grid = grid
        self.robot = robot
        self.show_grid = show_grid
        self.max_steps = max_steps
        self.steps = 0  # Nombre d'�tapes pour atteindre la cible
        self.place_target()
        self.target_reached = False

    def place_target(self):
        self.target_x = random.randint(0, self.grid.width - 1)
        self.target_y = random.randint(0, self.grid.height - 1)
        self.grid.grid[self.target_y][self.target_x] = 'X'  # Marquer la cible dans la grille

    def check_collision(self):
        if self.robot.x == self.target_x and self.robot.y == self.target_y:
            return True
        return False

    def run_turn(self):
        # V�rifier si la cible a d�j� �t� atteinte
        if self.target_reached:
            return True

        # V�rifier si le nombre d'�tapes a d�pass� la limite
        if self.steps >= self.max_steps:
            return False

        # D�placement du robot
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            self.robot.move_up(self.grid.height)
        elif direction == 'down':
            self.robot.move_down(self.grid.height)
        elif direction == 'left':
            self.robot.move_left()
        elif direction == 'right':
            self.robot.move_right(self.grid.width)

        # Affichage de la grille apr�s le d�placement du robot
        if self.show_grid:
            self.grid.clear()
            self.grid.grid[self.robot.y][self.robot.x] = 'R'
            self.grid.grid[self.target_y][self.target_x] = 'X'  
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
    robot = Robot(1, 1)

    # Cr�ation du jeu avec l'option d'affichage de la grille et une limite d'�tapes
    game = Game(grid, robot, max_steps=1000, show_grid=True)

    # Ex�cution des tours de jeu jusqu'� ce que le robot touche la cible ou que la limite d'�tapes soit d�pass�e
    while not game.run_turn():
        pass

    # V�rification si le robot a atteint la cible ou non et affichage du message appropri�
    if game.target_reached:
        print("F�licitations ! Le robot a atteint la cible en {} �tapes.".format(game.steps))
    else:
        print("Le robot n'a pas r�ussi � atteindre la cible dans le nombre maximum d'�tapes.")
