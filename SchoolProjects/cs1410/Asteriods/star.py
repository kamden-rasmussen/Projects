import circle, random, operator

class Star(circle.Circle):

    def __init__(self, mX, mY, mWorldWidth, mWorldHeight):

        circle.Circle.__init__(self, mX, mY, 0, 0, 0, 2, mWorldWidth, mWorldHeight)
        self.mBrightness = random.randrange(0,255)

        return

    def getBrightness(self):
        return self.mBrightness

    def setBrightness(self, nBright):

        if 255 >= nBright >= 0:
            self.mBrightness = nBright
            self.mColor = (nBright, nBright, nBright)

        return

    def evolve(self, dt):
        tens = (10, 10, 10)
        roll = random.randrange(0,2)
        if roll == 0 and self.mBrightness <=245:
            nBright = self.mBrightness + 10
            self.setBrightness(nBright)
            self.setColor((self.mBrightness, self.mBrightness, self.mBrightness))
            # self.mColor = (self.mColor[0] + tens[0], self.mColor[1] + tens[1], self.mColor[2] + tens[2])
        elif roll == 1 and self.mBrightness >= 10:
            nBright = self.mBrightness - 10
            self.setBrightness(nBright)
            self.setColor((self.mBrightness, self.mBrightness, self.mBrightness))
            # self.mColor = (self.mColor[0] - tens[0], self.mColor[1] - tens[1], self.mColor[2] - tens[2])
        return







