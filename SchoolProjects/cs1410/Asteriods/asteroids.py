import pygame
import ship, rock, star, random, bullet, sys

class Asteroids:

    def __init__( self, width, height ):
        self.mWorldWidth = width
        self.mWorldHeight = height

        self.mShip = ship.Ship(500, 500, self.mWorldWidth, self.mWorldHeight)
        self.mBullets = []
        self.mRocks = []
        self.mStars = []

        for i in range(10):
            x = random.randrange(0, self.mWorldWidth)
            y = random.randrange(0, self.mWorldHeight)
            tempRock = rock.Rock(x, y, self.mWorldHeight, self.mWorldHeight )
            self.mRocks.append(tempRock)

        for i in range(20):
            tempX = random.randrange(0, self.mWorldWidth)
            tempY = random.randrange(0, self.mWorldHeight)
            tempStar = star.Star(tempX, tempY, self.mWorldWidth, self.mWorldHeight)
            self.mStars.append(tempStar)

        self.mObjects = [self.mShip] + self.mRocks + self.mBullets + self.mStars

        self._gameOver = False

        return

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getShip(self):
        return self.mShip

    def getRocks(self):
        return self.mRocks

    def getObjects(self):
        return self.mObjects

    def getStars(self):
        return self.mStars

    def getBullets(self):
        return self.mBullets

    def turnShipLeft(self, dt):
        self.mShip.rotate(-dt)
        return

    def turnShipRight(self, dt):
        self.mShip.rotate(dt)
        return

    def accelerateShip(self, dt):
        self.mShip.accelerate(dt)
        return

    def fire(self):
        count = 0

        for bull in self.mBullets:
            if bull.getActive == True:
                count += 1

        if len(self.mBullets) < 3:
            newBull = self.mShip.fire()
            self.mObjects.append(newBull)
            self.mBullets.append(newBull)



    def collideShipAndBullets(self):
        for bull in self.mBullets:
            if self.mShip.hits(bull):
                self._gameOver = True

    def collideShipAndRocks(self):
        for rock in self.mRocks:
            if self.mShip.hits(rock):
                self._gameOver = True

    def collideRocksAndBullets(self):
        for bull in self.mBullets:
            for rock in self.mRocks:
                if bull.hits(rock):
                    bull.setActive(False)
                    rock.setActive(False)

    def removeInactiveObjects(self):
        for obj in self.mObjects:
            if not obj.getActive():
                self.mObjects.remove(obj)

        for rock in self.mRocks:
            if not rock.getActive():
                self.mRocks.remove(rock)

        for bull in self.mBullets:
            if not bull.getActive():
                self.mBullets.remove(bull)

    def evolveAllObjects(self, dt):
        for obj in self.mObjects:
            obj.evolve(dt)

    def evolve(self, dt):
        self.evolveAllObjects(dt)
        self.collideShipAndRocks()
        self.collideShipAndBullets()
        self.collideRocksAndBullets()
        self.removeInactiveObjects()
        for o in self.mObjects:
            o.evolve(dt)

        if len(self.mRocks) == 0:
            print("Congrats!")
            sys.exit()

        if self._gameOver == True:
            print("Mission Failed")
            sys.exit()
        return


    def draw( self, surface ):
        surface.fill((0,0,0))
        
        for o in self.mObjects:
            o.draw(surface)

        return
