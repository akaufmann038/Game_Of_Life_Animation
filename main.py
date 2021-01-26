import pygame
import math

# setup display
pygame.init()
WIDTH, HEIGHT = 500, 600
# Initialize a window or screen for display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game of Life!')

# grid variables
RECT_WIDTH = 20
startx = 0
starty = 0
grid = [] # x location, y location, boolean representing alive or dead, tuple with location of cell (row, col) format
# x and y location of buttons
buttons = {}
# creating list with grid objects
grid_size = int(WIDTH / RECT_WIDTH)
for i in range(grid_size):
    row = []
    for j in range(grid_size):
        row.append([RECT_WIDTH * j, RECT_WIDTH * i, False, (i, j)])
    grid.append(row)


def reset_start_grid():
    global grid
    grid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append([RECT_WIDTH * j, RECT_WIDTH * i, False, (i, j)])
        grid.append(row)


# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# setup game loop
FPS = 3
clock = pygame.time.Clock()
run = True
screen = 'start'

# draw selection screen
def draw_start_screen():
    win.fill(WHITE)

    text_welcome1 = LETTER_FONT.render('Welcome to the Game of Life!', 1, BLACK)
    text_welcome2 = LETTER_FONT.render('Choose an animation!', 1, BLACK)

    text_blinker = LETTER_FONT.render('Blinker', 1, BLACK)
    text_toad = LETTER_FONT.render('Toad', 1, BLACK)
    text_beacon = LETTER_FONT.render('Beacon', 1, BLACK)
    text_pulsar = LETTER_FONT.render('Pulsar', 1, BLACK)
    text_penta_decathlon = LETTER_FONT.render('Penta-decathion', 1, BLACK)
    text_choose_your_own = LETTER_FONT.render('Choose your own start state!', 1, BLACK)

    # can assign one variable to this because all button texts have the same height
    button_text_height = text_blinker.get_height()

    # draw welcome text
    len_down = 50
    win.blit(text_welcome1, (WIDTH / 2 - text_welcome1.get_width() / 2, len_down))
    len_down += 5 * text_welcome1.get_height() / 2
    win.blit(text_welcome2, (WIDTH / 2 - text_welcome2.get_width() / 2, len_down))
    len_down += 10 * text_welcome1.get_height() / 2

    # draw buttons and button text
    # adding to buttons: name of button, x location, y location, and width of button
    win.blit(text_blinker, (WIDTH / 2 - text_blinker.get_width() / 2, len_down))
    pygame.draw.rect(win, BLACK, (WIDTH / 2 - text_blinker.get_width() / 2 + text_blinker.get_width() + 5, len_down, button_text_height, button_text_height), 0)
    buttons['blinker_button'] = [WIDTH / 2 - text_blinker.get_width() / 2 + text_blinker.get_width() + 5, len_down, button_text_height]

    len_down += 5 * text_welcome1.get_height() / 2
    win.blit(text_toad, (WIDTH / 2 - text_toad.get_width() / 2, len_down))
    pygame.draw.rect(win, BLACK, (WIDTH / 2 - text_toad.get_width() / 2 + text_toad.get_width() + 5, len_down, button_text_height, button_text_height), 0)
    buttons['toad_button'] = [WIDTH / 2 - text_toad.get_width() / 2 + text_toad.get_width() + 5, len_down, button_text_height]


    len_down += 5 * text_welcome1.get_height() / 2
    win.blit(text_beacon, (WIDTH / 2 - text_beacon.get_width() / 2, len_down))
    pygame.draw.rect(win, BLACK, (WIDTH / 2 - text_beacon.get_width() / 2 + text_beacon.get_width() + 5, len_down, button_text_height, button_text_height), 0)
    buttons['beacon_button'] = [WIDTH / 2 - text_beacon.get_width() / 2 + text_beacon.get_width() + 5, len_down, button_text_height]


    len_down += 5 * text_welcome1.get_height() / 2
    win.blit(text_pulsar, (WIDTH / 2 - text_pulsar.get_width() / 2, len_down))
    pygame.draw.rect(win, BLACK, (WIDTH / 2 - text_pulsar.get_width() / 2 + text_pulsar.get_width() + 5, len_down, button_text_height, button_text_height), 0)
    buttons['pulsar_button'] = [WIDTH / 2 - text_pulsar.get_width() / 2 + text_pulsar.get_width() + 5, len_down, button_text_height]


    len_down += 5 * text_welcome1.get_height() / 2
    win.blit(text_penta_decathlon, (WIDTH / 2 - text_penta_decathlon.get_width() / 2, len_down))
    pygame.draw.rect(win, BLACK, (WIDTH / 2 - text_penta_decathlon.get_width() / 2 + text_penta_decathlon.get_width() + 5, len_down, button_text_height, button_text_height), 0)
    buttons['penta_decathlon_button'] = [WIDTH / 2 - text_penta_decathlon.get_width() / 2 + text_penta_decathlon.get_width() + 5, len_down, button_text_height]

    len_down += 5 * text_welcome1.get_height() / 2
    win.blit(text_choose_your_own, (WIDTH / 2 - text_choose_your_own.get_width() / 2, len_down))
    pygame.draw.rect(win, BLACK, (WIDTH / 2 - text_choose_your_own.get_width() / 2 + text_choose_your_own.get_width() + 5, len_down, button_text_height, button_text_height), 0)
    buttons['choose_your_own'] = [WIDTH / 2 - text_choose_your_own.get_width() / 2 + text_choose_your_own.get_width() + 5, len_down, button_text_height]

    # update game display
    pygame.display.update()

# draw game board

def draw_animation(type):
    win.fill(WHITE)

    # draw grid
    for row in grid:
        for cell in row:
            # unpack variables for current cell
            x_loc, y_loc, is_alive, loc = cell
            if is_alive:
                pygame.draw.rect(win, BLACK, (x_loc, y_loc, RECT_WIDTH, RECT_WIDTH), 0)
            else :
                pygame.draw.rect(win, BLACK, (x_loc, y_loc, RECT_WIDTH, RECT_WIDTH), 1)

    # draw button button below animation
    pygame.draw.rect(win, BLACK, (0, 500, WIDTH, 100), 3)
    if type == 'animate':
        back_button_text = LETTER_FONT.render('Click for Back To Home Screen', 1, BLACK)
    elif type == 'select':
        back_button_text = LETTER_FONT.render('Start animation!', 1, BLACK)

    win.blit(back_button_text, (250 - back_button_text.get_width() / 2, 550 - back_button_text.get_height() / 2))



    pygame.display.update()


def num_alive_neighbors(grid, loc):
    #global grid_size
    row = loc[0]
    col = loc[1]
    # get neighboring cell locations
    neighbors = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                 (row, col - 1), (row, col + 1),
                 (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    # only includes cells that are within the grid
    inbound_neighbors = [x for x in neighbors if ((x[0] >= 0 and x[0] < grid_size) and
                                                    (x[1] >= 0 and x[1] < grid_size))]
    count = 0
    # count how many neighboring cells are alive
    for cell in inbound_neighbors:
        if grid[cell[0]][cell[1]][2]:
            count+=1
    return count


def changeCells():

    to_change = []
    for row in grid:
        for cell in row:
            # unpack variables for current cell
            loc = cell[3]
            is_alive = cell[2]
            alive_neighbors = num_alive_neighbors(grid, loc)
            if is_alive:
                # alive and underpopulated, change state
                if alive_neighbors < 2:
                    to_change.append(loc)
                # alive and overpopulated, change state
                elif alive_neighbors > 3:
                    to_change.append(loc)
            else:
                # dead and 3 live neighbors, change state
                if alive_neighbors == 3:
                    to_change.append(loc)

    # change necessary cell states
    for loc in to_change:
        grid[loc[0]][loc[1]][2] = not grid[loc[0]][loc[1]][2]

# returns True if mouse click is within button and False if not
def in_range(m_x, m_y, button_x, button_y, button_width):
    x_within = m_x > button_x and m_x < (button_x + button_width)
    y_within = m_y > button_y and m_y < (button_y + button_width)

    return x_within and y_within

# sets the original state of the animation
def set_animation(animation):
    # reset the animation grid
    reset_start_grid()
    if animation == 'blinker_button':
        blinker_positions = [(11,11), (11,12), (11, 13)]
    elif animation == 'toad_button':
        blinker_positions = [(11,11), (11,10), (11,12), (10,11), (10,12), (10,13)]
    elif animation == 'beacon_button':
        blinker_positions = [(11,11), (10,11), (11,10), (10,10), (12,12),
                             (12,13), (13,12), (13,13)]
    elif animation == 'pulsar_button':
        blinker_positions = [(10, 11), (9, 11), (8, 11), (6, 10), (6, 9), (6, 8),
        (8, 6), (9, 6), (10, 6), (11, 8), (11, 9), (11, 10), (10, 13), (9, 13),
        (8, 13), (6, 14), (6, 15), (6, 16), (8, 18), (9, 18), (10, 18),
        (11, 14), (11, 15), (11, 16), (13, 10), (13, 9), (13, 8), (14, 6),
        (15, 6), (16, 6), (18, 8), (18, 9), (18, 10), (16, 11), (15, 11),
        (14, 11), (14, 13), (15, 13), (16, 13), (18, 14), (18, 15), (18, 16),
        (16, 18), (15, 18), (14, 18), (13, 16), (13, 15), (13, 14)]
    elif animation == 'penta_decathlon_button':
        blinker_positions = [(8, 10), (9, 10), (10, 10), (11, 10), (12, 10),
        (13, 10), (14, 10), (15, 10), (8, 11), (10, 11), (11, 11), (12, 11),
        (13, 11), (15, 11), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12),
         (13, 12), (14, 12), (15, 12)]
    elif animation == 'choose_your_own':
        blinker_positions = []


    for position in blinker_positions:
        row = position[0]
        col = position[1]
        grid[row][col] = [grid[row][col][0],grid[row][col][1],True,grid[row][col][3]]

# returns a tuple representing the cell that was clicked on based on the mouse location taken as an argument
def get_clicked_cell(x_loc, y_loc):
    for row in grid:
        for cell in row:
            loc = cell[3]
            x = cell[0]
            y = cell[1]
            # if mouse click lands within cell
            if (x_loc > x and x_loc < x + RECT_WIDTH) and (y_loc > y and y_loc < y + RECT_WIDTH):
                return loc


while run:
    clock.tick(FPS)

    # start screen
    if screen == 'start':
        # draw selection screen
        draw_start_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                # need locations of all buttons
                for button in buttons:
                    values = buttons[button]
                    # if button pressed, set start_screen to false, play selected animation
                    if in_range(m_x, m_y, values[0], values[1], values[2]):
                        # end start screen
                        set_animation(button)
                        # change the screen depending on what button is pressed
                        if button == 'choose_your_own':
                            screen = 'select'
                        else:
                            screen = 'animate'
                        # break out of buttons loop
                        break
    # selection screen
    elif screen == 'select':
        draw_animation(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                # if mouse clicked start animation button
                if m_x > 0 and m_y > 500:
                    screen = 'animate'
                else:
                    # if mouse clicked on a cell, turn on selected cell
                    clicked_cell = get_clicked_cell(m_x, m_y)
                    grid[clicked_cell[0]][clicked_cell[1]] = [grid[clicked_cell[0]][clicked_cell[1]][0],
                    grid[clicked_cell[0]][clicked_cell[1]][1],True,grid[clicked_cell[0]][clicked_cell[1]][3]]


    # animation screen
    elif screen == 'animate':
        # draw game board
        draw_animation(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                if m_x > 0 and m_y > 500:
                    screen = 'start'

        changeCells()






pygame.quit()
