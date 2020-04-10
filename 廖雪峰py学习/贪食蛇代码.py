import pygame
import random
import sys
# 定义颜色变量
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREEN = (0, 185, 0)
YELLOW = (255,255,0)
# 定义方向变量
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
# 定义窗口大小
windowsWidth = 800
windowsHeight = 600
# 定义地图大小
cellSize = 20                                #定义基础单位大小
mapWidth = int(windowsWidth / cellSize)      #地图的宽
mapHeight = int(windowsHeight / cellSize)    #地图的高
# 其他变量
HEAD = 0              #贪吃蛇头部下标
snakeSpeed = 7        #贪吃蛇的速度
# main()函数 是程序执行的入口
def main():           #入口函数，程序从这里开始运行
    pygame.init()     # 模块初始化
    screen = pygame.display.set_mode((windowsWidth, windowsHeight))
    pygame.display.set_caption("贪吃蛇")
    screen.fill(WHITE)
    snakeSpeedClock = pygame.time.Clock()
    startGame(screen)      #游戏开始
    while True:
            music=pygame.mixer.Sound("snake.wav")
            music.play(-1)
            runGame(screen, snakeSpeedClock)
            music.stop()
            gameOver(screen)   #游戏结束
# startGame()函数 这个函数负责控制我们的程序启动，它接收的参数是窗口的pygame.Surface对象
def startGame(screen):
    gameStart = pygame.image.load("gameStart.png")
    screen.blit(gameStart, (70, 30))
    font = pygame.font.SysFont("SimHei", 40)
    tip = font.render("按任意键开始游戏", True, (65, 105, 225))
    screen.blit(tip, (240, 550))
    pygame.display.update()

    while True:                                     #键盘监听事件
        for event in pygame.event.get():            #关闭窗口
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):  #按下ESC键
                    terminate()
                else:
                    return
# runGame()函数 这个函数控制着游戏程序运行，它接受的参数是窗口的pygame.Surface对象和Pygame的时钟对象
def runGame(screen,snakeSpeedClock):
    startX = random.randint(3, mapWidth - 8)
    startY = random.randint(3, mapHeight - 8)
    snakeCoords = [{"x": startX, "y": startY},
    {"x": startX - 1, "y": startY},
    {"x": startX - 2, "y": startY}]
    direction = RIGHT
    food = {"x": random.randint(0, mapWidth - 1), "y": random.randint(0, mapHeight - 1)}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT  and direction != LEFT:
                    direction = RIGHT
                elif event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_ESCAPE:
                    terminate()

        moveSnake(direction, snakeCoords)  #移动贪吃蛇

        isEattingFood(snakeCoords, food)   #判断贪吃蛇是否吃到食物

        ret = isAlive(snakeCoords)         #判断贪吃蛇是否还活着
        if not ret:
            break                          #贪吃蛇已经死了，游戏结束

        gameRun = pygame.image.load("background.png")
        screen.blit(gameRun, (0, 0))
        drawFood(screen, food)
        drawSnake(screen, snakeCoords)
        drawScore(screen, len(snakeCoords) - 3)

        pygame.display.update()
        snakeSpeedClock.tick(snakeSpeed)  #控制帧速率
# drawFood()函数 函数用来绘制食物，它接受的参数是窗口的pygame.Surface对象和表示坐标的字典对象
def drawFood(screen, food):
    x = food["x"] * cellSize
    y = food["y"] * cellSize
    pygame.draw.rect(screen, YELLOW, (x, y, cellSize, cellSize))
def drawSnake(screen, snakeCoords):
    for coord in snakeCoords:
        x = coord["x"] * cellSize
        y = coord["y"] * cellSize
        pygame.draw.rect(screen, DARKGREEN, (x, y, cellSize, cellSize))
        pygame.draw.rect(screen, GREEN,(x + 4, y + 4, cellSize - 8, cellSize - 8))
def drawScore(screen,score):
    font = pygame.font.SysFont("SimHei", 30)
    scoreSurf = font.render("得分: " + str(scoer), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (windowsWidth - 200, 50)
    screen.blit(scoreSurf, scoreRect)
# moveSnake()函数 moveSnake()函数用来移动贪吃蛇，它接受的参数是表示方向的变量和表示贪吃蛇的列表。
# moveSnake()函数会根据方向，来增加一个蛇头的元素到列表中
def moveSnake(direction, snakeCoords):
    if direction == UP:
        newHead = {"x": snakeCoords[HEAD][ "x"], "y": snakeCoords[HEAD][ "y"] - 1}
    elif direction == DOWN:
        newHead = {"x": snakeCoords[HEAD][ "x"], "y": snakeCoords[HEAD][ "y"] + 1}
    elif direction == LEFT:
        newHead = {"x": snakeCoords[HEAD][ "x"] - 1, "y": snakeCoords[HEAD][ "y"]}
    elif direction == RIGHT:
        newHead = {"x": snakeCoords[HEAD][ "x"] + 1, "y": snakeCoords[HEAD][ "y"]}

    snakeCoords.insert(0, newHead)
# isEattingFood()函数用来判断贪吃蛇是否吃到了食物
def isEattingFood(snakeCoords, food):
    if snakeCoords[HEAD]["x"] == food["x"] and snakeCoords[HEAD]["y"] == food["y"]:
        food["x"] = random.randint(0, mapWidth - 1)
        food["y"] = random.randint(0, mapHeight - 1)
    else:
        del snakeCoords[-1]
# isAive()函数用来判断贪吃蛇是否死亡
def isAlive(snakeCoords):
    tag = True
    if snakeCoords[HEAD]["x"] == -1 or snakeCoords[HEAD]["x"] == mapWidth or snakeCoords[HEAD]["y"] == -1 or snakeCoords[HEAD]["y"] == mapHeight:
        tag = False        # 贪吃蛇碰壁
    for snake_body in snakeCoords[1:]:
        if snake_body["x"] == snakeCoords[HEAD]["x"] and snake_body["y"] == snakeCoords[HEAD]["y"]:
            tag = False   # 贪吃蛇碰到自己身体
    return tag
# gameOver()函数控制整个程序的结束
def gameOver(screen):
#加载游戏结束图片
    screen.fill(WHITE)
    gameOver = pygame.image.load("gameover.png")
    screen.blit(gameOver, (0, 0))
    #加载游戏结束提示信息
    font = pygame.font.SysFont("SimHei", 36)
    tip = font.render("按Q或者ESC退出游戏, 按其他键重新开始游戏", True, (65, 105, 225))
    screen.blit(tip, (30, 500))
       #显示Surface对象上的内容
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    terminate()
                else:
                    return #结束此函数, 重新开始游戏
# terminate()函数
def terminate():
    pygame.quit()
    sys.exit()
# 运行入
main()