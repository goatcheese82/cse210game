from game.services.procedure_generator import ProcedureGenerator
from game.models.maze import Maze

def main():
    maze = Maze(6,6)
    pg = ProcedureGenerator(maze)


if __name__ == "__main__":
    main()