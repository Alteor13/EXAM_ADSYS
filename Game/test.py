"""Fichier de test de game_target_v3.py"""

import game_target_v3 as ga # Erreur signalée mais sans consequence...

grid = ga.Grid(5, 5)
robot = ga.Robot(1, 1)
game = ga.Game(grid, robot, max_steps=1000, show_grid=True)

def test_grid():
    """Batterie de test sur la grille"""
    print ("test de grid.display (affichage de la grille)")
    grid.display()

    print ("test de grid.clear")
    grid.clear()

def test_robot():
    """Batterie de test sur le robot et sa position"""
    print ("test de robot.move_down")
    print ("avant mouvement : ")
    print (robot.y)
    robot.move_down(grid.height)
    print ("apres mouvement : ")
    print (robot.y)

    print ("test de robot.move_up")
    print ("avant mouvement : ")
    print (robot.y)
    robot.move_up(grid.height)
    print ("apres mouvement : ")
    print (robot.y)

    print ("test de robot.move_right")
    print ("avant mouvement : ")
    print (robot.x)
    robot.move_right(grid.height)
    print ("apres mouvement : ")
    print (robot.x)

    print ("test de robot.move_left")
    print ("avant mouvement : ")
    print (robot.x)
    robot.move_left()
    print ("apres mouvement : ")
    print (robot.x)

def test_game():
    """Batterie de test sur l'objet game'"""
    game.place_target()

    print ("Verifie si le robot et la cible se trouvent sur la meme case")
    game.check_collision()

    print ("Verifie que la cible a ete atteinte ou non")
    game.run_turn()

test_robot()
test_grid()
test_game()
