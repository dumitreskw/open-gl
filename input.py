import glfw

previous_x, previous_y = 400, 300  # poziția inițială a mouse-ului

def setup_input(window, camera, player):
    glfw.set_key_callback(window, lambda w, k, s, a, m: key_callback(w, k, s, a, m, camera, player))
    glfw.set_cursor_pos_callback(window, lambda w, x, y: mouse_callback(w, x, y, camera))
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

def key_callback(window, key, scancode, action, mods, camera, player):
    if key in camera.movement:
        if action == glfw.PRESS:
            camera.movement[key] = True
        elif action == glfw.RELEASE:
            camera.movement[key] = False

    if key in player.movement:
        if action == glfw.PRESS:
            player.movement[key] = True
        elif action == glfw.RELEASE:
            player.movement[key] = False

def mouse_callback(window, xpos, ypos, camera):
    global previous_x, previous_y
    dx = xpos - previous_x
    dy = previous_y - ypos  # inversăm pentru pitch
    previous_x, previous_y = xpos, ypos

    camera.yaw += dx * 0.05
    camera.pitch += dy * 0.05

    # Limităm pitch-ul
    camera.pitch = max(-89, min(89, camera.pitch))
