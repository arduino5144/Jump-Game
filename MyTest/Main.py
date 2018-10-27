import os
import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        print(os.getcwd())
        pyxel.load('C:/Users/leona/source/repos/MyTest/MyTest/leo_pyx.pyxel')
        pyxel.play(0, 0, loop=True)
        self.tilemap = pyxel.tilemap(0)
        print(self.tilemap.width)
        print(self.tilemap.height)
        self.x = 0
        self.player_x = 10
        self.player_y = 100
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        # pyxel.cls(0)
        pyxel.rect(self.x, 0, self.x + 7, 7, 9)
        pyxel.bltm(10, 10, 0, 0, 0, 0, 256, 256)
        
        # draw player
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            0,
            40,
            8,
            8
        )
            

App()
