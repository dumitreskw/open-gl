import numpy as np
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    def __init__(self):
        self.x, self.y, self.z = 0, 1.5, 10
        self.yaw, self.pitch, self.roll = 0, 0, 0
        self.speed = 0.07

        self.movement = {
            # Mișcare
            glfw.KEY_W: False, glfw.KEY_S: False,
            glfw.KEY_A: False, glfw.KEY_D: False,
            glfw.KEY_SPACE: False, glfw.KEY_LEFT_SHIFT: False,
            # Rotație Roll
            glfw.KEY_Q: False, glfw.KEY_E: False
        }

    def update(self):
        glLoadIdentity()

        # Direcția camerei
        dir_x = np.cos(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))
        dir_y = np.sin(np.radians(self.pitch))
        dir_z = np.sin(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))
        direction = np.array([dir_x, dir_y, dir_z])
        direction = direction / np.linalg.norm(direction)

        # Vectorul Up (cu Roll aplicat)
        up_x = np.sin(np.radians(self.roll))
        up_y = np.cos(np.radians(self.roll))
        up = np.array([up_x, up_y, 0.0])
        up = up / np.linalg.norm(up)

        # Target pentru gluLookAt
        target = np.array([self.x, self.y, self.z]) + direction
        gluLookAt(self.x, self.y, self.z, *target, *up)

        # Vectore pentru mișcare
        forward = np.array([np.cos(np.radians(self.yaw)), 0, np.sin(np.radians(self.yaw))])
        right = np.array([np.cos(np.radians(self.yaw - 90)), 0, np.sin(np.radians(self.yaw - 90))])
        up_dir = np.array([0, 1, 0])

        move = np.zeros(3)
        if self.movement[glfw.KEY_W]: move += forward
        if self.movement[glfw.KEY_S]: move -= forward
        if self.movement[glfw.KEY_A]: move += right
        if self.movement[glfw.KEY_D]: move -= right
        if self.movement[glfw.KEY_SPACE]: move += up_dir
        if self.movement[glfw.KEY_LEFT_SHIFT]: move -= up_dir

        move *= self.speed
        new_pos = np.array([self.x, self.y, self.z]) + move
        limit = 50  # spațiu mai mare

        if all(-limit < c < limit for c in new_pos):
            self.x, self.y, self.z = new_pos

        # Control Roll
        if self.movement[glfw.KEY_Q]: self.roll += 1
        if self.movement[glfw.KEY_E]: self.roll -= 1
        self.roll = self.roll % 360
