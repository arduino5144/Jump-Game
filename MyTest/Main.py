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
        self.bg_start = 0
        self.player_x = 8
        self.player_y = 64
        pyxel.run(self.update, self.draw)

    def update(self):
        self.update_player()   
        if self.bg_start > 12:
           self.bg_start = 12
        if self.bg_start < 0:
            self.bg_start = 0

    def update_player(self):
         if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 2, 0)
            if self.player_x <= 40:
               self.bg_start -= 1

         if pyxel.btn(pyxel.KEY_RIGHT):
             self.player_x = min(self.player_x + 2, pyxel.width - 16)
             if self.player_x > 40:
               self.bg_start += 1

    def draw(self):
        pyxel.cls(0)
        
        pyxel.bltm(0, # x
                   0, # y
                   0, # image
                   0, # tilemap
                   self.bg_start,  # tilemap start x position
                   0,  # tilemap start y
                   20, # tilemap width
                   15  # tilemap height
                   )

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
