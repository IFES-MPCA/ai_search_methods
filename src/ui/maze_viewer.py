from typing import Iterable, Tuple

import cv2
import numpy as np
from numpy import ndarray

from src.models.maze.hashable_2d_maze import Hashable2DMaze
from src.models.problem.maze_2d.cell import Cell, CellType


class MazeBlockColors:
    START_COLOR = (0, 255, 0)
    GOAL_COLOR = (255, 0, 0)
    EXPANDED_COLOR = (0, 255, 255)
    GENERATED_COLOR = (0, 0, 255)
    PATH_COLOR = (128, 0, 255)


class MazeViewer:

    def __init__(self, start: Cell, goal: Cell, maze: Hashable2DMaze, zoom=50, step_time_milliseconds=-1):
        self.__start__ = start
        self.__goal__ = goal
        self.__maze__ = maze
        self.__zoom__ = zoom
        self.__delay__ = step_time_milliseconds
        self.__generate_maze_image__()

    def __generate_maze_image__(self):
        lines = self.__maze__.lines
        columns = self.__maze__.columns
        maze_img = np.array(lines * [columns * [0]]).astype(np.uint8) * 255

        # invert black and white pixels so that obstacles are black and free areas are white.
        maze_img = 255 - maze_img
        maze_img = cv2.cvtColor(maze_img, cv2.COLOR_GRAY2BGR)

        for position in self.__maze__.maze:
            cell = self.__maze__.maze.get(position)

            if cell.type == CellType.OBSTACLE:
                maze_img[position[1], position[0]] = (0, 0, 0)

        self.__maze_img__: ndarray = maze_img

    def update(self, generated=None, expanded=None, path=None):
        if path is None:
            path = []

        if expanded is None:
            expanded = []

        if generated is None:
            generated = []

        maze_img = self.__maze_img__.copy()

        self.__draw_cells__(maze_img, path, MazeBlockColors.PATH_COLOR)
        self.__draw_cells__(maze_img, generated, MazeBlockColors.GENERATED_COLOR)
        self.__draw_cells__(maze_img, expanded, MazeBlockColors.EXPANDED_COLOR)

        maze_img[self.__start__.y, self.__start__.x] = MazeBlockColors.START_COLOR
        maze_img[self.__goal__.y, self.__goal__.x] = MazeBlockColors.GOAL_COLOR

        maze_img = self.__apply_zoom__(maze_img, zoom=self.__zoom__)
        self.__draw_grid__(maze_img, self.__zoom__)

        cv2.imshow("view", maze_img)
        cv2.waitKey(self.__delay__)

    @staticmethod
    def pause() -> None:
        cv2.waitKey(-1)

    @staticmethod
    def __apply_zoom__(maze_img: ndarray, zoom: int = 10) -> ndarray:
        lines, columns, _ = maze_img.shape
        big_img = np.zeros((lines * zoom, columns * zoom, 3))

        for i in range(lines):
            for j in range(columns):
                r_st = zoom * i
                r_end = zoom * (i + 1)
                c_st = zoom * j
                c_end = zoom * (j + 1)
                big_img[r_st: r_end, c_st: c_end] = maze_img[i, j]

        return big_img

    @staticmethod
    def __draw_grid__(maze_img: ndarray, zoom: int):
        lines, columns, _ = maze_img.shape
        black = (0, 0, 0)

        for i in range(0, columns, zoom):
            cv2.line(maze_img, (i, 0), (i, lines), color=black, thickness=1)

        for j in range(0, lines, zoom):
            cv2.line(maze_img, (0, j), (columns, j), color=black, thickness=1)

    @staticmethod
    def __draw_cells__(maze_img: ndarray, cells: Iterable[Cell], color: Tuple[int, int, int]):
        for cell in cells:
            maze_img[cell.y, cell.x] = color
