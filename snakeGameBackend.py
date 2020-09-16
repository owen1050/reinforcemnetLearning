import random

class SnakeGame:
    def __init__(self):
        self.snake = [[0,0]]
        self.snakeDirection = 1
        self.gameOver = False
        self.WIDTH = 20
        self.HEIGHT = 30
        self.fruitPos = (int(self.WIDTH/2), int(self.HEIGHT/2))
        self.score = 0

    def setSnake(self, snake):
        self.snake = snake

    def setSnakeDirection(self, snakeD):
        self.snakeDirection = snakeD

    def setGameOver(self, go):
        self.gameOver = go

    def setWidth(self, w):
        self.WIDTH = w

    def setWidth(self, h):
        self.HEIGHT = h


    def incSnake(self):
        curr = self.snake[0]
            
        if self.snakeDirection == 0:
            new = (curr[0] + 0, curr[1] - 1)

        if self.snakeDirection == 1:
            new = (curr[0] + 1, curr[1] + 0)

        if self.snakeDirection == 2:
            new = (curr[0] + 0, curr[1] + 1)

        if self.snakeDirection == 3:
            new = (curr[0] - 1, curr[1] + 0)

        if new[0] > self.WIDTH - 1 or new[0] < 0 or new[1] > self.HEIGHT - 1 or new[1] < 0 or new in self.snake:
            self.gameOver = True

        if new == self.fruitPos:
            nfx = random.randint(0, self.WIDTH-1)
            nfy = random.randint(0, self.HEIGHT-1)
            self.fruitPos = (nfx, nfy)
            newSnake = self.snake[:]
            self.score = self.score + 1
        else:
            newSnake = self.snake[:-1]

        newSnake.insert(0,new)
        self.snake = newSnake
