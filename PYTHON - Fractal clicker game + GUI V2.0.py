import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 255)
BUTTON_HOVER_COLOR = (50, 150, 200)
TEXT_COLOR = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fractal Clicker")

# Font setup
font = pygame.font.SysFont(None, 36)

# Function to draw a triangle
def draw_triangle(points, color):
    pygame.draw.polygon(screen, color, points)

# Function to get midpoint
def get_midpoint(p1, p2):
    return ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)

# Function to generate Sierpinski Triangle
def sierpinski_triangle(points, depth):
    if depth == 0:
        draw_triangle(points, WHITE)
    else:
        # Calculate the midpoints of each side
        midpoints = [get_midpoint(points[i], points[(i + 1) % 3]) for i in range(3)]
        
        # Draw the smaller triangles
        sierpinski_triangle([points[0], midpoints[0], midpoints[2]], depth - 1)
        sierpinski_triangle([points[1], midpoints[0], midpoints[1]], depth - 1)
        sierpinski_triangle([points[2], midpoints[1], midpoints[2]], depth - 1)

# Draw text on the screen
def draw_text(text, x, y, color=TEXT_COLOR):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Reset button
def draw_button(text, x, y, w, h, hover=False):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, w, h))
    draw_text(text, x + 10, y + 10)

# Initial triangle points and game variables
initial_points = [(400, 50), (150, 550), (650, 550)]
click_count = 0
reset_button_rect = pygame.Rect(650, 50, 120, 40)

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button_rect.collidepoint(mouse_pos):
                click_count = 0
            else:
                click_count += 1
    
    # Draw the fractal based on the number of clicks
    sierpinski_triangle(initial_points, click_count)
    
    # GUI Elements
    draw_text(f"Depth Level: {click_count}", 20, 20)
    draw_text("Click anywhere to increase depth", 20, 60)
    
    # Reset Button
    draw_button("Reset", 650, 50, 120, 40, hover=reset_button_rect.collidepoint(mouse_pos))
    
    # Update the display
    pygame.display.flip()

pygame.quit()
