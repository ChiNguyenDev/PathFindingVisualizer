import pygame
import Button
import Colors
import AStar

pygame.init()
MENU_WIDTH = 200
GRID_SIZE = 800
WINDOW_WIDTH = GRID_SIZE + MENU_WIDTH
WINDOW_HEIGHT = GRID_SIZE

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Path Finding Visualizer")
image = pygame.image.load('resources/logo.png')

# declare Buttons
astar_button = Button.Button(Colors.WHITE, 40, 400, 310, 80, 'A* Search')
dijkstra_button = Button.Button(Colors.WHITE, 450, 400, 310, 80, 'Dijkstra')
bfs_button = Button.Button(Colors.WHITE, 40, 550, 310, 80, 'Breadth-First Search')
dfs_button = Button.Button(Colors.WHITE, 450, 550, 310, 80, 'Deep-First-Search')


def main():
    run = True
    while run:
        screen.fill(Colors.BLACK)  # Fill the background first
        screen.blit(image, (250, 60))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if astar_button.is_over(pos):
                    AStar.main(screen, WINDOW_HEIGHT)  # Call your algorithm function here

        # Draw buttons after filling the background
        astar_button.draw(screen)
        dijkstra_button.draw(screen)
        bfs_button.draw(screen)
        dfs_button.draw(screen)

        # Update text position and draw it after the background has been filled
        font = pygame.font.SysFont('josefin', 30)
        text_surface = font.render('Developed by Chi Cuong Nguyen', True, Colors.WHITE)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 30))  # Center horizontally, place near the bottom
        screen.blit(text_surface, text_rect)

        pygame.display.update()

    pygame.quit()


def draw_window():
    screen.fill(Colors.BLACK)
    astar_button.draw(screen)
    # Draw other buttons
    dijkstra_button.draw(screen)
    bfs_button.draw(screen)
    dfs_button.draw(screen)
    pygame.display.update()


if __name__ == "__main__":
    main()
