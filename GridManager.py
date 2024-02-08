import Colors
import pygame
import Spot

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, Colors.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, Colors.GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(Colors.WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()



def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot.Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid
