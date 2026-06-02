# player.py
import numpy as np
from OpenGL.GL import *
import glfw

class Player:
    def __init__(self, x=0, y=0.5, z=0):
        self.x, self.y, self.z = x, y, z
        self.speed = 0.1
        self.size = 0.5  # dimensiunea cubului
        self.movement = {
            glfw.KEY_UP: False,
            glfw.KEY_DOWN: False,
            glfw.KEY_LEFT: False,
            glfw.KEY_RIGHT: False
        }

    def update(self, collision_boxes):
        move = np.array([0.0, 0.0, 0.0])

        forward = np.array([0, 0, -1])  # înainte pe axa Z negativ
        right = np.array([1, 0, 0])      # dreapta pe axa X pozitiv

        if self.movement[glfw.KEY_UP]: move += forward
        if self.movement[glfw.KEY_DOWN]: move -= forward
        if self.movement[glfw.KEY_LEFT]: move -= right
        if self.movement[glfw.KEY_RIGHT]: move += right

        move = move * self.speed
        new_pos = np.array([self.x, self.y, self.z]) + move

        if not self.check_collision(new_pos, collision_boxes):
            self.x, self.y, self.z = new_pos

    def draw(self):
        glPushMatrix()
        glColor3f(1, 0, 0)  # culoare roșie
        glTranslatef(self.x, self.y, self.z)
        
        # Creăm un cub manual (fără GLUT)
        half_size = self.size / 2.0

        # 6 fețe ale cubului
        glBegin(GL_QUADS)

        # Fața din față (Z pozitiv)
        glNormal3f(0, 0, 1)
        glVertex3f(-half_size, -half_size, half_size)  # jos stânga
        glVertex3f(half_size, -half_size, half_size)   # jos dreapta
        glVertex3f(half_size, half_size, half_size)    # sus dreapta
        glVertex3f(-half_size, half_size, half_size)   # sus stânga

        # Fața din spate (Z negativ)
        glNormal3f(0, 0, -1)
        glVertex3f(-half_size, -half_size, -half_size)  # jos stânga
        glVertex3f(-half_size, half_size, -half_size)   # sus stânga
        glVertex3f(half_size, half_size, -half_size)    # sus dreapta
        glVertex3f(half_size, -half_size, -half_size)   # jos dreapta

        # Fața stângă (X negativ)
        glNormal3f(-1, 0, 0)
        glVertex3f(-half_size, -half_size, -half_size)  # jos stânga
        glVertex3f(-half_size, -half_size, half_size)   # jos dreapta
        glVertex3f(-half_size, half_size, half_size)    # sus dreapta
        glVertex3f(-half_size, half_size, -half_size)   # sus stânga

        # Fața dreaptă (X pozitiv)
        glNormal3f(1, 0, 0)
        glVertex3f(half_size, -half_size, -half_size)   # jos stânga
        glVertex3f(half_size, half_size, -half_size)    # sus stânga
        glVertex3f(half_size, half_size, half_size)     # sus dreapta
        glVertex3f(half_size, -half_size, half_size)    # jos dreapta

        # Fața de sus (Y pozitiv)
        glNormal3f(0, 1, 0)
        glVertex3f(-half_size, half_size, -half_size)   # stânga jos
        glVertex3f(half_size, half_size, -half_size)    # dreapta jos
        glVertex3f(half_size, half_size, half_size)     # dreapta sus
        glVertex3f(-half_size, half_size, half_size)    # stânga sus

        # Fața de jos (Y negativ)
        glNormal3f(0, -1, 0)
        glVertex3f(-half_size, -half_size, -half_size)  # stânga jos
        glVertex3f(-half_size, -half_size, half_size)   # stânga sus
        glVertex3f(half_size, -half_size, half_size)    # dreapta sus
        glVertex3f(half_size, -half_size, -half_size)   # dreapta jos

        glEnd()

        glPopMatrix()

    def check_collision(self, pos, collision_boxes):
        x, y, z = pos
        for box in collision_boxes:
            (min_x, min_y, min_z), (max_x, max_y, max_z) = box
            if (min_x <= x <= max_x) and (min_y <= y <= max_y) and (min_z <= z <= max_z):
                return True
        return False
