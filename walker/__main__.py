from game.services.procedure_generator import ProcedureGenerator
from game.models.maze import Maze

def main():
    maze = Maze(6,6)
    maze.populate_grid()
    maze.add_path()
    maze._path.find_start()
    pg = ProcedureGenerator(maze)
    pg.generate_path()


if __name__ == "__main__":
    main()