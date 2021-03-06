from ast import If
from cgi import test
from multiprocessing import parent_process
from pyexpat import model
from subprocess import HIGH_PRIORITY_CLASS
from turtle import position
from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3 (45,45,45),
        )

class Test_button(Button):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.blue,
            Texture = 'brick',
            parent = scene,
            highlight_color = color.red,
            pressed_color = color.lime,
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('button pressed')

def update():
    if held_keys['a']:
        test_square.x -= 4 * time.dt

app=Ursina()

test_square = Entity( model ='quad',color = color.red, scale = (1,4), position = (5,4) )

sans_Texture = load_texture ('assets/Sans.png')
sans = Entity(model ='quad',texture = sans_Texture)

# Test_cube = Test_cube()
Test_cube = Test_button()


app.run()