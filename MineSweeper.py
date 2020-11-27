from random import randint
import pygame
pygame.init()

def mine(n, bombs):
    table = make_table(n)
    table = add_bombs(table, bombs)
    table = change_table(table)
    return table

def make_table(n):
    return [[0] * n for i in range(n)]

def add_bombs(table, bombs):
    for i in range(bombs):
        is_bomb = False
        while not is_bomb:
            x = randint(0 ,len(table) - 1)
            y = randint(0 ,len(table) - 1)
            if table[x][y] != 9:
                table[x][y] = 9
                is_bomb = True
    return table


def change_table(table):
    for x in range(len(table)):
        for y in range(len(table[x])):
                       if table[x][y] == 9:
                           table = check_down_left(table, x, y)
                           table = check_down_right(table, x, y)
                           table = check_down(table, x, y)
                           table = check_up_left(table, x, y)
                           table = check_up_right(table, x, y)
                           table = check_up(table, x, y)
                           table = check_left(table, x, y)
                           table = check_right(table, x, y)
    return table

def check_down_left(table, x, y):
    if x + 1 < len(table[x]) and y - 1 >= 0:
        if table[x + 1][y - 1] != 9:
            table[x + 1][y - 1] += 1
    return table


def check_down_right(table, x, y):
    if x + 1 < len(table[0]) and y + 1 < len(table):
        if table[x + 1][y - 1] != 9:
            table[x + 1][y - 1] += 1
    return table


def check_down(table, x, y):
    if x + 1 < len(table[0]) and y - 1 >= 0:
        if table[x + 1][y - 1] != 9:
            table[x + 1][y - 1] += 1
    return table
    

def check_up_left(table, x, y):
    if x + 1 >= 0 and y - 1 >= 0:
        if table[x + 1][y - 1] != 9:
            table[x + 1][y - 1] += 1
    return table

def check_up_right(table, x, y):
    if x - 1 >= 0 and y + 1 < len(table):
        if table[x - 1][y + 1] != 9:
            table[x - 1][y + 1] += 1
    return table

def check_up(table, x, y):
    if x - 1 >= 0:
        if table[x + 1][y - 1] != 9:
            table[x + 1][y - 1] += 1
    return table

def check_left(table, x, y):
    if y - 1 >= 0:
        if table[x][y - 1] != 9:
            table[x][y - 1] += 1
    return table


def check_right(table, x, y):
    if y + 1 < len(table):
        if table[x][y + 1] != 9:
            table[x][y + 1] += 1
    return table


def pr(table):
    for i in table:
        print(i)



class Board:
    def __init__(self, board):
        self.board = board
    def __repr__(self):
        pr(self.board)
        return "is your table"

class Sqaure:
    def __init__(self, x, y, w, h, board, ij):
        self.rect = pygame.rect.Rect(x, y, w, h)
        i, j= ij
        self.val = board[i][j]
        self.x = x
        self.y = y
        self.visible = False
        self.flag = False

def restart(size, bombs):
    game(size, bombs)

def open_game(lst, sqaure):
    square.visible = True
    i, j = square.x // 40, square.y // 40
    if i + 1 < len(lst):
        if lst[i+1][j].visible == False and lst[i+1][j].flag == False:
            lst[i+1][j].visible == True
            if lst[i+1][j].val == 0:
                open_game(lst, lst[i+1][j])

    if j + 1 < len(lst):
        if lst[i+1][j +1].visible == False and lst[i+1][j+1].flag == False:
            lst[i+1][j+1].visible == True
            if lst[i+1][j+1].val == 0:
                open_game(lst, lst[i+1][j+1])

    if j - 1 >= 0:
        if lst[i + 1][j +1].visible == False and lst[i +1][j +1].flag == False:
            lst[i + 1][j +1].visible == True
            if lst[i + 1][j +1].val == 0:
                open_game(lst, lst[i + 1][j+1])





    if i - 1 >= 0:
        if lst[i-1][j ].visible == False and lst[i-1][j].flag == False:
            lst[i-1][j].visible == True
            if lst[i-1][j].val == 0:
                open_game(lst, lst[i-1][j])


    if j + 1 < len(lst):
        if lst[i-1][j +1].visible == False and lst[i-1][j+1].flag == False:
            lst[i-1][j+1].visible == True
            if lst[i-1][j+1].val == 0:
                open_game(lst, lst[i-1][j+1])


    if j - 1 >= 0:
        if lst[i - 1][j -1].visible == False and lst[i - 1][j -1].flag == False:
            lst[i - 1][j -1].visible == True
            if lst[i - 1][j -1].val == 0:
                open_game(lst, lst[i - 1][j -1])



    if j - 1 >= 0:
        if lst[i][j -1].visible == False and lst[i][j-1].flag == False:
            lst[i][j-1].visible == True
            if lst[i][j-1].val == 0:
                open_game(lst, lst[i][j-1])


    if j + 1 < len(lst):
        if lst[i][j +1].visible == False and lst[i][j+1].flag == False:
            lst[i][j+1].visible == True
            if lst[i][j+1].val == 0:
                open_game(lst, lst[i][j+1])
                


    

def game(size, bombs):
    grey = pygame.image.load("grey.jpg")
    white = pygame.image.load("white.jpg")

    zero = pygame.image.load("zero.jpg")
    one = pygame.image.load("one.gif")
    two = pygame.image.load("two.gif")
    three = pygame.image.load("three.gif")
    four = pygame.image.load("four.gif")
    five = pygame.image.load("five.gif")
    six = pygame.image.load("six.gif")
    seven = pygame.image.load("seven.gif")
    eight = pygame.image.load("eight.jpg")
    nine = pygame.image.load("nine.png")
    flag = pygame.image.load("flag.png")


    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

    c = Board(mine(size, bombs))
    w = h - len(c.board) * 40
    screen = pygame.display.set_mode((w, h))

    lst = [[] for i in range(size)]
    for i in range(0, size * 40, 40):
        for j in range(0, size * 40, 40):
            lst[i//40] += [Square(i, j, 40, 40, c.board, (i//40, j//40))]
            screen.blit(grey, (i, j))

    run = True
    while run:
        for event in pygame.event.et():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run = False
                    restart(size, bombs)
            elif event.type == pygame.MOUSEBUTTONDOWN and even.button == 1:
                for i in lst:
                    for j in i:
                        r = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))
                        if j.rect.colliderect(r):
                            if j.flag == False:
                                if j.val == 9:
                                    print("Game Over")
                                    run = False
                                j.visible = True
                                if j.val == 0:
                                    j.visible = open_game(lst, j)
                                    j.visible = True
            elif event.type == pygame.MOUSEBUTTONDOWN and even.button == 3:
                for i in lst:
                    for j in i:
                        r = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))
                        if j.rect.colliderect(r):
                            if j.visible == False:
                                if j.flag == False:
                                    j.flag = True
                                elif j.flag == True:
                                    j.flag = False
        for i in lst:
            for j in i:
                if j.visible == True:
                    screen.blit(white, (j.x, j.y))
                    screen.blit(numbers[j.val], (j.x + 10, j.y + 10))
                if j.flag == True:
                    screen.blit(flag, (j.x + 10, j.y + 10))
                if j.flag == False and j.visible == False:
                    screen.blit(grey, (j.x, j.y))

        cat = 0
        for i in lst:
            for j in i:
                if j.visible == True and j.val != 9:
                    cat += 1
            if cat == size * size - bombs:
                run = False
                print("you win")
        pygame.display.update()

        for i in lst:
            for j in i:
                if j.val == 9:
                    screen.blit(nine, (j.x + 10, j.y + 10))
        pygame.display.update()
        
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        run = False
                        restart(size, bomb)


print("press 'r' for restart")
print("we will be asking for entering the size of the table, the table will be N by N sqaures so you")
size = int(input("please enter the size of the table: "))
bombs = (size * size) // 7
game(size, bombs)


