import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fractal Clicker")

# Function to draw a triangle
def draw_triangle(points, color):
    pygame.draw.polygon(screen, color, points)

# Function to get mid point
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

# Initial triangle points
initial_points = [(400, 50), (150, 550), (650, 550)]
click_count = 0

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_count += 1
    
    # Draw the fractal based on the number of clicks
    sierpinski_triangle(initial_points, click_count)
    
    # Update the display
    pygame.display.flip()

pygame.quit()
