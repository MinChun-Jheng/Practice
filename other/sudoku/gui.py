# gui
import pygame

# initial the pygame font
pygame.font.init()
ROWS = 9
COLS = 9
WIDTH = 540
HEIGHT = 540

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
# screen & title
screen = pygame.display.set_mode((WIDTH,HEIGHT + 100))
pygame.display.set_caption("SUDUKU GUI")

x = 0
y = 0
gap = WIDTH / 9
val = 0

# Default Board
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

# text font set
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

def get_cord(pos):
    global x
    x = pos[0] // gap
    global y
    y = pos[1] // gap

# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, RED, (x * gap-3, (y + i)*gap), (x * gap + gap + 3, (y + i)*gap), 7)
        pygame.draw.line(screen, RED, ((x + i)* gap, y * gap ), ((x+ i) * gap, y * gap + gap), 7)

# Draw grid
def draw():
    # Draw the line
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] != 0:
                # fill the color and texㄔ in board which already have number
                pygame.draw.rect(screen, (0, 153, 153), (i * gap, j * gap, gap + 1, gap + 1))

                text1= font1.render(str(board[i][j]), 1, BLACK)
                screen.blit(text1, (i * gap + 15, j * gap + 15))

    # Draw vertival & horizontal line
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, BLACK, (0, i * gap), (WIDTH, i * gap), thick)
        pygame.draw.line(screen, BLACK, (i * gap, 0), (i * gap, HEIGHT), thick)

# Fill value entered in cell
def draw_val(val):
    text1 = font1.render(str(val), 1, BLACK)
    screen.blit(text1, (x * gap + 15, y * gap + 15))

# Raise error
def raise_error1():
    text1= font1.render("WRONG !!!", 1, BLACK)
    screen.blit(text1, (20, 610))
def raise_error2():
    text1= font1.render("WRONG !!!Not a valid Key", 1, BLACK)
    screen.blit(text1, (20, 610))

# check valid
def valid(bo, row, col, val):
    for it in range(9):
        if bo[row][it] == val:
            return False
        if bo[it][col] == val:
            return False
    it = row // 3
    jt = col // 3
    for i in range(it*3, it*3+3):
        for j in range(jt*3, jt*3+3):
            if bo[i][j] == val:
                return False
    return True

# Solve
def solve(board, i, j):

    while board[i][j] != 0:
        if i<8:
            i += 1
        elif i == 8 and j<8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(board, i, j, it) == True:
            board[i][j] = it
            global x, y
            x = i
            y = j
            # fill white
            screen.fill(WHITE)
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(board, i , j) == 1:
                return True
            else:
                board[i][j] = 0

            screen.fill(WHITE)
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False

# Display instruction for the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 560))
    screen.blit(text2, (20, 580))

# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 610))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while run:
    screen.fill(WHITE)
    # loop event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                board =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                board =[
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
    if flag2 == 1:
        if solve(board, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0

    if val != 0:
        draw_val(val)
        if valid(board, int(x), int(y), val) == True:
            board[int(x)][int(y)] = val
            flag1 = 0
        else:
            board[int(x)][int(y)] = 0
            raise_error2()
        val = 0

    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    draw()
    if flag1 == 1:
        draw_box()
    instruction()

    pygame.display.update()

pygame.quit()
