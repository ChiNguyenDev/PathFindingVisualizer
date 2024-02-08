import pygame
import Colors

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.orig_color = color  # Keep track of the original color
        # Ensure that no component goes above 255
        self.hover_color = Colors.LIGHT_GREY
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Draw outline if specified
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))

        current_color = self.hover_color if self.is_over(pygame.mouse.get_pos()) else self.color
        pygame.draw.rect(win, current_color, (self.x, self.y, self.width, self.height))

        if self.text != '':
            font = pygame.font.SysFont('josefin', 40)
            text = font.render(self.text, True, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False
