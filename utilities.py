# -*- coding: utf-8 -*-

import sys

class ProgressBar():
    DEFAULT_BAR_LENGTH = float(65)

    def __init__(self, end, start=0):
        self.end    = end
        self.start  = start
        self._barLength = ProgressBar.DEFAULT_BAR_LENGTH

        self.setLevel(self.start)
        self._plotted = False

    def setLevel(self, level, initial=False):
        self._level = level
        if level < self.start:  self._level = self.start
        if level > self.end:    self._level = self.end

        self._ratio = float(self._level - self.start) / float(self.end - self.start)
        self._levelChars = int(self._ratio * self._barLength)

    def plotProgress(self):
        sys.stdout.write("\r  %3i%% [%s%s]" %(
            int(self._ratio * 100.0),
            '=' * int(self._levelChars),
            ' ' * int(self._barLength - self._levelChars),
        ))
        self._plotted = True

    def setAndPlot(self, level):
        oldChars = self._levelChars
        self.setLevel(level)
        if (not self._plotted) or (oldChars != self._levelChars):
            self.plotProgress()

    def __del__(self):
        sys.stdout.write("\n")

if __name__ == "__main__":
    import time
    count = 5
    print "starting things:"

    pb = ProgressBar(count)

    curProgress = 0
    #pb.plotProgress()
    while curProgress <= count:
        pb.setAndPlot(curProgress)
        curProgress += 1
        time.sleep(1)
    del pb

    print "done"
