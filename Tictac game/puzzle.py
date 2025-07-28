import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
FPS = 30
FONT = pygame.font.Font(None, 72)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sliding Puzzle Game")

# Generate a shuffled puzzle board
def create_board():
    numbers = list(range(1, GRID_SIZE * GRID_SIZE)) + [0]
    random.shuffle(numbers)
    board = [numbers[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]
    return board

# Draw the board
def draw_board(board):
    screen.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            tile = board[row][col]
            if tile != 0:
                pygame.draw.rect(screen, GRAY, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                text = FONT.render(str(tile), True, BLACK)
                text_rect = text.get_rect(center=(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)
    pygame.display.flip()

# Find the empty tile (0)
def find_empty(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 0:
                return row, col

# Swap two tiles
def swap_tiles(board, row1, col1, row2, col2):
    board[row1][col1], board[row2][col2] = board[row2][col2], board[row1][col1]

# Check if the player has won
def is_solved(board):
    correct = list(range(1, GRID_SIZE * GRID_SIZE)) + [0]
    current = [tile for row in board for tile in row]
    return current == correct

# Main game loop
def main():
    board = create_board()
    clock = pygame.time.Clock()
    running = True

    while running:
        draw_board(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                row, col = find_empty(board)
                if event.key == pygame.K_UP and row < GRID_SIZE - 1:
                    swap_tiles(board, row, col, row + 1, col)
                elif event.key == pygame.K_DOWN and row > 0:
                    swap_tiles(board, row, col, row - 1, col)
                elif event.key == pygame.K_LEFT and col < GRID_SIZE - 1:
                    swap_tiles(board, row, col, row, col + 1)
                elif event.key == pygame.K_RIGHT and col > 0:
                    swap_tiles(board, row, col, row, col - 1)
        
        if is_solved(board):
            print("Congratulations! You solved the puzzle!")
            running = False

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
