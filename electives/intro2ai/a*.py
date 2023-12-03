import pygame
import math
from queue import PriorityQueue

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIME = (191, 255, 0)
BLOOD = (136, 8, 8)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

WIDTH = 22
HEIGHT = 22
MARGIN = 3
TILE = WIDTH + MARGIN

class Field:

    def __init__(self, row, col, tile):
        self.x = col * tile
        self.y = row * tile
        self.color = GREY
        self.neighbor = [
            [row + 1, col],
            [row - 1, col],
            [row, col - 1],
            [row, col + 1],
        ]

    def draw_field(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, WIDTH, HEIGHT])

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def get_pos(self):
        return [self.x, self.y]
    
    def get_neighbours(self):
        return self.neighbor

class Grid:

    def __init__(self, rows, cols, tile):
        self.rows = rows
        self.cols = cols
        self.fields = []
        
        for row in range(rows):
            self.fields.append([])

            for column in range(cols):
                field = Field(row, column, tile)
                self.fields[row].append(field)

    def draw_grid(self, tile):
        for row in range(self.rows):
            for column in range(self.cols):
                self.fields[row][column].draw_field()

        for row in range(self.rows):
            pygame.draw.line(screen, BLACK, (0, row * tile), (tile * self.cols, row * tile))

        for column in range(self.cols):
            pygame.draw.line(screen, BLACK, (column * tile, 0), (column * tile, tile * self.rows))

    def get_field(self, row, col):
        return self.fields[row][col]
      
def heuristic_func(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def path(previous, end, grid):
    while end in previous:
        end = previous[end]
        end.set_color(PURPLE)
        grid.draw_grid(TILE)
        pygame.display.flip()
        pygame.time.wait(50)

def Astar(grid, start_node, goal_node):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start_node))
    came_from = {}

    g_score = {field: float("inf") for row in grid.fields for field in row}
    g_score[start_node] = 0

    f_score = {field: float("inf") for row in grid.fields for field in row}
    f_score[start_node] = heuristic_func(start_node.get_pos(), goal_node.get_pos())

    open_set_hash = {start_node}

    while not open_set.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == goal:
            path(came_from, goal_node, grid)
            start.set_color(PURPLE)
            goal.set_color(TURQUOISE)
            return True

        for node in current.get_neighbours():

            if 20 > node[0] >= 0 and 20 > node[1] >= 0 and grid.get_field(node[0], node[1]).get_color() != BLACK:
                neighbour = grid.get_field(node[0], node[1])
                temp_g_score = g_score[current] + TILE

                if temp_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = temp_g_score
                    f_score[neighbour] = temp_g_score + heuristic_func(neighbour.get_pos(), goal_node.get_pos())
                    if neighbour not in open_set_hash:  
                        count += 1
                        open_set.put((f_score[neighbour], count, neighbour))
                        open_set_hash.add(neighbour)
                        neighbour.set_color(BLOOD)

            grid.draw_grid(TILE)
            pygame.display.flip()

            if current != start:
                current.set_color(LIME)
    return False

MiGrid = Grid(20, 20, TILE)

start = MiGrid.get_field(19, 0)
goal = MiGrid.get_field(0, 19)

obstacles = [
    [0, 16], [1, 16],
    [2, 16], [3, 16],
    [4, 16], [5, 16],
    [6, 16], [7, 16],
    [8, 16], [9, 16],
    [10, 16], [10, 4],
    [10, 5], [10, 6],
    [10, 7], [10, 8],
    [10, 9], [11, 9],
    [12, 9], [13, 9],
    [14, 9], [15, 9],
    [16, 9], [17, 9],
    [18, 9], [19, 9],
]

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("A Star Game")

done = False

clock = pygame.time.Clock()

for obstacle in obstacles:
    MiGrid.get_field(obstacle[0], obstacle[1]).set_color(BLACK)

start.set_color(PURPLE)
goal.set_color(BLUE)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        screen.fill(BLACK)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Astar(MiGrid, start, goal)
        else:
            MiGrid.draw_grid(TILE)
            pygame.display.flip()

        clock.tick(60)

pygame.quit()
