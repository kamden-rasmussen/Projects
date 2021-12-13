import circle


class Bullet(circle.Circle):

    def __init__(self, mX, mY, mDx, mDy, mRotation, mWorldWidth, mWorldHeight):

        circle.Circle.__init__(self, mX, mY, mDx, mDy, mRotation, 3, mWorldWidth, mWorldHeight)
        self.mAge = 0
        self.accelerate(100.0)
        self.move(0.1)

        return

    def getAge(self):
        return self.mAge

    def setAge(self, age):
        self.mAge = age
        return

    def evolve(self, dt):
        self.setAge(self.mAge + dt)
        if self.mAge >= 6:
            self.mActive = False
            # print('bullet dies')
        self.move(dt)
