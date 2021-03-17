import pygame
import sys

WIDTH = 800
ROWS = 40
WIN = pygame.display.set_mode((WIDTH,WIDTH))

pygame.display.set_caption("Game of Life")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.color = WHITE
        self.occpied = None

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, WIDTH/8, WIDTH/8))

def make_grid(rows, width):
    grid = []
    gap = WIDTH // rows
    print(gap)
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)

    return grid

def draw_grid(win, rows, width):
    gap = width // ROWS
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j*gap, 0), (j*gap, width))

def update_display(win, grid, rows, width):
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def Find_Node(pos, WIDTH):
    interval = WIDTH / ROWS
    y, x = pos
    rows = y // interval
    columns = x // interval
    return  int(rows), int(columns)

def neighbor(tile):
    col, row = tile.row, tile.col

    neighbors = [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
                  [row, col - 1], [row, col + 1],
                  [row + 1, col - 1], [row + 1, col], [row + 1, col + 1], ]
    actual = []
    for i in neighbors:
        row, col = i
        if 0 <= row <= (ROWS - 1) and 0 <= col <= (ROWS - 1):
            actual.append(i)
    return actual

def update_grid(grid):
    newgrid = []
    for row in grid:
        for tile in row:
            neighbors = neighbor(tile)
            count = 0
            for i in neighbors:
                row, col = i
                if grid[row][col].color == BLACK:
                    count += 1
            if tile.color == BLACK:
                if count == 2 or count == 3:
                    newgrid.append(BLACK)
                else:
                    newgrid.append(WHITE)
            else:
                if count == 3:
                    newgrid.append(BLACK)
                else:
                    newgrid.append(WHITE)
    return newgrid

def main(WIN, WIDTH):
    run = None
    grid = make_grid(ROWS, WIDTH)
    while True:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = Find_Node(pos, WIDTH)
                if grid[col][row].color == WHITE:
                    grid[col][row].color = BLACK
                elif grid[col][row].color == BLACK:
                    grid[col][row].color = WHITE

            while run:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        run = False
                newcolors = update_grid(grid)
                count = 0
                for i in range(0, len(grid)):
                    for j in range(0, len(grid)):
                        grid[i][j].color = newcolors[count]
                        count += 1
                update_display(WIN, grid, ROWS, WIDTH)

            update_display(WIN, grid, ROWS, WIDTH)

main(WIN, WIDTH)