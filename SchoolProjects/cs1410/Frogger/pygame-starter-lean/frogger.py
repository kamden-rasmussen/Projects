import pygame
import froggerlib


class Frogger:

    def __init__(self, width, height):
        self._road1Cars = []
        self._road2Cars = []
        self._road3Cars = []
        self._road4Cars = []
        self._road5Cars = []
        self._water1Floats = []
        self._water2Floats = []
        self._water3Floats = []
        self._water4Floats = []
        self._water5Floats = []
        self._homes = []

        self.mWidth = width
        self.mHeight = height
        self._laneSize = 90
        self._gameOver = False

        # Colors
        self._baseColor = (102, 51, 0)
        self._frogColor = (100, 255, 0)
        self._roadColor = (0, 0, 0)
        self._waterColor = (0, 158, 255)
        self._rCarColor = (255, 0, 0)
        self._carColor = (204, 204, 0)
        self._truckColor = (160, 160, 160)
        self._logColor = (204, 104, 0)
        self._turtleColor = (0, 102, 0)
        self._grassColor = (102, 0, 0)
        self._homeColor = (0, 255, 255)

        # What is frog?
        w = .4 * self._laneSize
        h = .4 * self._laneSize
        x = self.mWidth/2 - w/2
        y = self._laneSize * 12.5 - h/2
        dX = x
        dY = y
        s = self._laneSize/4
        hG = self._laneSize
        vG = self._laneSize
        self._frog = froggerlib.Frog(x, y, w, h, dX, dY, s, hG, vG)

        # Roads
        x = 0
        y = 7 * self._laneSize
        w = self.mWidth
        h = self._laneSize * 5
        self._roads = froggerlib.Road(x, y, w, h)

        # Waterway
        x = 0
        y = 1 * self._laneSize
        w = self.mWidth
        h = self._laneSize * 5
        self._waterWay = froggerlib.Water(x, y, w, h)

        # Grass
        x = 0
        y = 0
        w = self.mWidth
        h = self._laneSize
        self._grass = froggerlib.Grass(x, y, w, h)

        # Homes
        for i in range(3):
            x = self.mWidth * (.225 * (i + 1))
            y = 0
            w = self.mWidth * .10
            h = self._laneSize
            home = froggerlib.Home(x, y, w, h)
            self._homes.append(home)

        # Road 1 Race Car
        for i in range(1):
            x = 1 * self.mWidth / .33
            y = 11 * self._laneSize
            w = self.mWidth * .06
            h = self._laneSize * .8
            dX = self.mWidth
            dY = y
            maxS = self._laneSize/2
            minS = self._laneSize/6
            self._rCar1 = froggerlib.RaceCar(x, y, w, h, dX, dY, minS, maxS)
            self._road1Cars.append(self._rCar1)

        # Road 2 Cars
        for i in range(3):
            x = 1 * self.mWidth * (.33 * (i + 1))
            y = 10 * self._laneSize
            w = self.mWidth * .08
            h = self._laneSize * .8
            dX = - w
            dY = y
            S = self._laneSize / 6
            car = froggerlib.Car(x, y, w, h, dX, dY, S)
            self._road2Cars.append(car)

        # Road 3 Trucks
        for i in range(2):
            # creating a car
            x = 1 * self.mWidth * (.40 * (i + 1))
            y = 9 * self._laneSize
            w = self.mWidth * .12
            h = self._laneSize * .9
            dX = - w
            dY = y
            S = self._laneSize / 10
            truck = froggerlib.Car(x, y, w, h, dX, dY, S)
            self._road3Cars.append(truck)

        # Road 4 Race Car
        for i in range(1):
            x = 1 * self.mWidth / .66
            y = 8 * self._laneSize
            w = self.mWidth * .06
            h = self._laneSize * .8
            dX = self.mWidth
            dY = y
            maxS = self._laneSize/3
            minS = self._laneSize/5
            rCar = froggerlib.RaceCar(x, y, w, h, dX, dY, minS, maxS)
            self._road4Cars.append(rCar)

        # Road 5 Cars
        for i in range(3):
            # creating a car
            x = 1 * self.mWidth * (.27 * (i + 1))
            y = 7 * self._laneSize
            w = self.mWidth * .08
            h = self._laneSize * .8
            dX = self.mWidth
            dY = y
            S = self._laneSize / 6
            car = froggerlib.Car(x, y, w, h, dX, dY, S)
            self._road5Cars.append(car)

        # Water 1 Logs
        for i in range(4):
            x = 1 * self.mWidth * (.28 * (i + 1))
            y = 5 * self._laneSize
            w = self.mWidth * .12
            h = self._laneSize * .9
            dX = - w
            dY = y
            S = self._laneSize / 8
            log = froggerlib.Log(x, y, w, h, dX, dY, S)
            self._water1Floats.append(log)

        # Water 2 Turtles
        for i in range(3):
            x = 1 * self.mWidth * (.10 * (i + 1))
            y = 4 * self._laneSize
            w = self.mWidth * .08
            h = self._laneSize * .9
            dX = self.mWidth
            dY = y
            S = self._laneSize / 10
            turtle = froggerlib.Turtle(x, y, w, h, dX, dY, S)
            self._water2Floats.append(turtle)

        # Water 3 Logs
        for i in range(1):
            x = 1 * self.mWidth * (.28 * (i + 1))
            y = 3 * self._laneSize
            w = self.mWidth * .30
            h = self._laneSize * .9
            dX = - w
            dY = y
            S = self._laneSize / 20
            log = froggerlib.Log(x, y, w, h, dX, dY, S)
            self._water3Floats.append(log)

        # Water 4 Turtles
        for i in range(3):
            x = 1 * self.mWidth * (.20 * (i + 1))
            y = 2 * self._laneSize
            w = self.mWidth * .08
            h = self._laneSize * .9
            dX = self.mWidth
            dY = y
            S = self._laneSize / 7
            turtle = froggerlib.Turtle(x, y, w, h, dX, dY, S)
            self._water4Floats.append(turtle)

        # Water 5 Logs
        for i in range(1):
            x = 1 * self.mWidth * (.28 * (i + 1))
            y = 1 * self._laneSize
            w = self.mWidth * .40
            h = self._laneSize * .9
            dX = - w
            dY = y
            S = self._laneSize / 15
            log = froggerlib.Log(x, y, w, h, dX, dY, S)
            self._water5Floats.append(log)

        return

    def actOnPressUP(self):
        self._frog.up()
        return

    def actOnPressLeft(self):
        self._frog.left()
        return

    def actOnPressRight(self):
        self._frog.right()
        return

    def actOnPressDown(self):
        self._frog.down()
        return

    def evolve(self, dt):
        if self._gameOver:
            return
        self._frog.move()
        if self._frog.outOfBounds(self.mWidth, self.mHeight):
            self._gameOver = True
        for log in self._water1Floats:
            log.supports(self._frog)

        for turtle in self._water2Floats:
            turtle.supports(self._frog)

        for log in self._water3Floats:
            log.supports(self._frog)

        for turtle in self._water4Floats:
            turtle.supports(self._frog)

        for log in self._water5Floats:
            log.supports(self._frog)

        if self._waterWay.hits(self._frog):
            self._gameOver = True

        if self._grass.hits(self._frog):
            self._gameOver = True

        for home in self._homes:
            if home.hits(self._frog):
                self._gameOver = True

        # Road 1
        for car in self._road1Cars:
            car.move()
            if car.atDesiredLocation():
                x = - car.getX()
                car.setX(x)
            if car.hits(self._frog):
                self._gameOver = True

        # Road 2
        for car in self._road2Cars:
            car.move()
            if car.atDesiredLocation():
                x = self.mWidth
                car.setX(x)
            if car.hits(self._frog):
                self._gameOver = True

        # Road 3
        for truck in self._road3Cars:
            truck.move()
            if truck.atDesiredLocation():
                x = self.mWidth
                truck.setX(x)
            if truck.hits(self._frog):
                self._gameOver = True

        # Road 4
        for car in self._road4Cars:
            car.move()
            if car.atDesiredLocation():
                x = - car.getX()
                car.setX(x)
            if car.hits(self._frog):
                self._gameOver = True

        # Road 5
        for car in self._road5Cars:
            car.move()
            if car.atDesiredLocation():
                x = 0 - car.getWidth()
                car.setX(x)
            if car.hits(self._frog):
                self._gameOver = True

        # Water 1
        for log in self._water1Floats:
            log.move()
            if log.atDesiredLocation():
                x = self.mWidth
                log.setX(x)

        # Water 2
        for turtle in self._water2Floats:
            turtle.move()
            if turtle.atDesiredLocation():
                x = 0 - turtle.getWidth()
                turtle.setX(x)

        # Water 3
        for log in self._water3Floats:
            log.move()
            if log.atDesiredLocation():
                x = self.mWidth
                log.setX(x)

        # Water 4
        for turtle in self._water4Floats:
            turtle.move()
            if turtle.atDesiredLocation():
                x = 0 - turtle.getWidth()
                turtle.setX(x)

        # Water 3
        for log in self._water5Floats:
            log.move()
            if log.atDesiredLocation():
                x = self.mWidth
                log.setX(x)

        return

    # draws the current state of the system
    def draw(self, surface):
        
        # rectangle to fill the background
        rect = pygame.Rect(int(0), int(0), int(self.mWidth), int(self.mHeight))
        pygame.draw.rect(surface, self._baseColor, rect, 0)

        # Roads Draw
        roadRect = pygame.Rect(int(self._roads.getX()), int(self._roads.getY()), int(self._roads.getWidth()),
                               int(self._roads.getHeight()))
        pygame.draw.rect(surface, self._roadColor, roadRect, 0)

        # Waterway Draw
        waterRect = pygame.Rect(int(self._waterWay.getX()), int(self._waterWay.getY()), int(self._waterWay.getWidth()),
                           int(self._waterWay.getHeight()))
        pygame.draw.rect(surface, self._waterColor, waterRect, 0)

        # Grass Draw
        grassRect = pygame.Rect(int(self._grass.getX()), int(self._grass.getY()), int(self._grass.getWidth()),
                           int(self._grass.getHeight()))
        pygame.draw.rect(surface, self._grassColor, grassRect, 0)

        # Home Draw
        for home in self._homes:
            homeRect = pygame.Rect(int(home.getX()), int(home.getY()), int(home.getWidth()),
                               int(home.getHeight()))
            pygame.draw.rect(surface, self._homeColor, homeRect, 0)

        # Road 1 Race Cars draw
        for car in self._road1Cars:
            rCarRect = pygame.Rect(int(car.getX()), int(car.getY()), int(car.getWidth()), int(car.getHeight()))
            pygame.draw.rect(surface, self._rCarColor, rCarRect, 0)

        # Road 2 Cars draw
        for car in self._road2Cars:
            carRect = pygame.Rect(int(car.getX()), int(car.getY()), int(car.getWidth()), int(car.getHeight()))
            pygame.draw.rect(surface, self._carColor, carRect, 0)

        # Road 3 Trucks Draw
        for truck in self._road3Cars:
            carRect = pygame.Rect(int(truck.getX()), int(truck.getY()), int(truck.getWidth()), int(truck.getHeight()))
            pygame.draw.rect(surface, self._truckColor, carRect, 0)

        # Road 4 Race Cars Draw
        for car in self._road4Cars:
            rCarRect = pygame.Rect(int(car.getX()), int(car.getY()), int(car.getWidth()), int(car.getHeight()))
            pygame.draw.rect(surface, self._rCarColor, rCarRect, 0)

        # Road 5 Cars draw
        for car in self._road5Cars:
            carRect = pygame.Rect(int(car.getX()), int(car.getY()), int(car.getWidth()), int(car.getHeight()))
            pygame.draw.rect(surface, self._carColor, carRect, 0)

        # Water 1 Logs draw
        for log in self._water1Floats:
            carRect = pygame.Rect(int(log.getX()), int(log.getY()), int(log.getWidth()), int(log.getHeight()))
            pygame.draw.rect(surface, self._logColor, carRect, 0)

        # Water 2 Turtle draw
        for turtle in self._water2Floats:
            carRect = pygame.Rect(int(turtle.getX()), int(turtle.getY()), int(turtle.getWidth()), int(turtle.getHeight()))
            pygame.draw.rect(surface, self._turtleColor, carRect, 0)

        # Water 3 Log draw
        for log in self._water3Floats:
            carRect = pygame.Rect(int(log.getX()), int(log.getY()), int(log.getWidth()), int(log.getHeight()))
            pygame.draw.rect(surface, self._logColor, carRect, 0)

        # Water 4 Turtle draw
        for turtle in self._water4Floats:
            carRect = pygame.Rect(int(turtle.getX()), int(turtle.getY()), int(turtle.getWidth()), int(turtle.getHeight()))
            pygame.draw.rect(surface, self._turtleColor, carRect, 0)

        # Water 5 Log draw
        for log in self._water5Floats:
            carRect = pygame.Rect(int(log.getX()), int(log.getY()), int(log.getWidth()), int(log.getHeight()))
            pygame.draw.rect(surface, self._logColor, carRect, 0)

        # Frog draw
        frogRect = pygame.Rect(int(self._frog.getX()), int(self._frog.getY()), int(self._frog.getWidth()),
                               int(self._frog.getHeight()))
        pygame.draw.rect(surface, self._frogColor, frogRect, 0)

        return
