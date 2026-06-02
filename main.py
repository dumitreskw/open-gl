from OpenGL.GLUT import *
glutInit()
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

from camera import Camera
from graphics import draw_platform, draw_skybox, draw_road_and_sidewalks, draw_benches, draw_trash_can
from textures import load_texture
from input import setup_input
from player import Player

# Inițializare GLFW
if not glfw.init():
    raise Exception("GLFW nu a putut fi inițializat!")

window = glfw.create_window(1920, 1080, "Skyblock World", None, None)
if not window:
    glfw.terminate()
    raise Exception("Fereastra nu a putut fi creată!")

glfw.make_context_current(window)
glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

# Setări OpenGL
glEnable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D)
glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
glClearColor(0.5, 0.7, 1.0, 1.0)  # cerul albastru deschis

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(60, 1920 / 1080, 0.1, 100)
glMatrixMode(GL_MODELVIEW)

# Activăm iluminarea
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

# Lumina principală - apus
glEnable(GL_LIGHT0)
light0_pos = [-10.0, 10.0, 10.0, 0.0]  # 0.0 = directional light ca soarele
glLightfv(GL_LIGHT0, GL_POSITION, light0_pos)
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 0.8, 0.6, 1.0])  # Galben cald de apus
glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 0.9, 0.8, 1.0])  # Specular aproape alb



# Ambient global
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.1, 0.05, 1.0])

# Reflexii materiale
glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 0.8, 0.4, 1.0])
glMaterialf(GL_FRONT, GL_SHININESS, 64.0)  # Luciu

# Cameră și texturi
camera = Camera()
player = Player()

# Încarcă texturile
grass_texture = load_texture("grass.jpg")
sky_texture = load_texture("sky.jpeg")
road_texture = load_texture("road_texture.jpg")
sidewalk_texture = load_texture("sidewalk.jpg")
platform_texture = load_texture("grass.jpg")
wall_texture = load_texture("wall.jpg")
roof_texture = load_texture("roof.jpg")
door_texture = load_texture("door.jpg")
bench_texture = load_texture("bench.png")
trash_texture = load_texture("trash.jpg")
grey_metal_texture = load_texture("grey_metal.jpg")
light_texture = load_texture("light.jpg")
cristi_texture = load_texture("cristi_texture.jpg")
raul_texture = load_texture("raul_texture.jpg")

# Input
setup_input(window, camera, player)

# Cutii de coliziune
collision_boxes = [
    # Case
    [(-6.5, 0.0, -6.5), (-3.5, 3.5, -3.5)],  # Casa la (-5, -5)
    [(-6.5, 0.0, 3.5), (-3.5, 3.5, 6.5)],    # Casa la (-5, 5)
    [(3.5, 0.0, -6.5), (6.5, 3.5, -3.5)],    # Casa la (5, -5)
    [(3.5, 0.0, 3.5), (6.5, 3.5, 6.5)],      # Casa la (5, 5)

    # Bănci
    [(1.6, 0.0, -7.5), (2.4, 1.0, -4.5)],    # Bancă la (2, -6) rotită 270°
    [(-2.4, 0.0, 4.5), (-1.5, 1.0, 7.5)],    # Bancă la (-2, 6) rotită 90°
    [(-2.4, 0.0, -7.5), (-1.5, 1.0, -4.5)],  # Bancă la (-2, -6) rotită 90°
    [(1.6, 0.0, 4.5), (2.4, 1.0, 7.5)],      # Bancă la (2, 6) rotită 270°

    [(1.75, 0.0, -3.45), (2.25, 1.2, -2.95)],  # Coș la (2.0, -3.2)
    [(-2.25, 0.0, 2.95), (-1.75, 1.2, 3.45)],  # Coș la (-2.0, 3.2)
    [(1.75, 0.0, 2.95), (2.25, 1.2, 3.45)],    # Coș la (2.0, 3.2)
    [(-2.25, 0.0, -3.45), (-1.75, 1.2, -2.95)], # Coș la (-2.0, -3.2)
    
    [(-20.0, -20.0, -20.0), (-19.0, 20.0, 20.0)],  # Perete la X = -20
    [(19.0, -20.0, -20.0), (20.0, 20.0, 20.0)],    # Perete la X = 20
    [(-20.0, -20.0, -20.0), (20.0, 20.0, -19.0)],  # Perete la Z = -20
    [(-20.0, -20.0, 19.0), (20.0, 20.0, 20.0)]    # Perete la Z = 20.

]

# === LOOP PRINCIPAL ===
while not glfw.window_should_close(window):

        # Frame start
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera.update()

    glEnable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glColor3f(1.0, 1.0, 1.0)  # White pentru a păstra textura originală

    # Material pentru obiecte normale (doar reflexie)
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 16.0)

    # === DESENARE PLATFORMĂ, CASE, DRUMURI, BĂNCI ===
    draw_platform(grass_texture)
    draw_road_and_sidewalks(road_texture, sidewalk_texture, wall_texture, roof_texture, door_texture, cristi_texture, raul_texture)
    draw_skybox(sky_texture)
    draw_benches(bench_texture)

    # === PLAYER ===
    glColor3f(1.0, 1.0, 1.0)
    player.update(collision_boxes)
    player.draw()

    # === MATERIAL METALIC COSURI DE GUNOI ===
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    glColor3f(1.0, 1.0, 1.0)
    draw_trash_can(2.0, 0, -3.2, trash_texture)
    draw_trash_can(-2.0, 0, 3.2, trash_texture)
    draw_trash_can(2.0, 0, 3.2, trash_texture)
    draw_trash_can(-2.0, 0, -3.2, trash_texture)

    # Swap
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
