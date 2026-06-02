from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube(x, y, z, texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glPushMatrix()
    glTranslatef(x, y, z)

    glBegin(GL_QUADS)

    # Top face
    glTexCoord2f(0, 0)
    glVertex3f(-0.5,  0.5, -0.5)
    glTexCoord2f(1, 0)
    glVertex3f(0.5,  0.5, -0.5)
    glTexCoord2f(1, 1)
    glVertex3f(0.5,  0.5,  0.5)
    glTexCoord2f(0, 1)
    glVertex3f(-0.5,  0.5,  0.5)

    glEnd()
    glPopMatrix()

def draw_textured_plane(x, y, z, width, depth, texture, uv_scale=4):
    glBindTexture(GL_TEXTURE_2D, texture)  # Activează textura
    
    glBegin(GL_QUADS)  # Începem desenarea unui pătrat mare
    
    glTexCoord2f(0, 0)
    glVertex3f(x, y, z)  # Stânga-jos
    
    glTexCoord2f(uv_scale, 0)
    glVertex3f(x + width, y, z)  # Dreapta-jos
    
    glTexCoord2f(uv_scale, uv_scale)
    glVertex3f(x + width, y, z + depth)  # Dreapta-sus
    
    glTexCoord2f(0, uv_scale)
    glVertex3f(x, y, z + depth)  # Stânga-sus
    
    glEnd()  # Terminăm desenarea

def draw_platform(texture):
    # Desenează un singur pătrat mare în loc de multe cuburi
    draw_textured_plane(-20, 0, -20, 40, 40, texture, uv_scale=4)

def draw_road(x_start, x_end, z_start, z_end, texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(x_start, 0.01, z_start)
    glTexCoord2f(1, 0)
    glVertex3f(x_end, 0.01, z_start)
    glTexCoord2f(1, 1)
    glVertex3f(x_end, 0.01, z_end)
    glTexCoord2f(0, 1)
    glVertex3f(x_start, 0.01, z_end)
    glEnd()

def draw_sidewalk(x_start, x_end, z_start, z_end, texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)

    glTexCoord2f(0, 0)
    glVertex3f(x_start, 0.01, z_start)
    glTexCoord2f(1, 0)
    glVertex3f(x_end, 0.01, z_start)
    glTexCoord2f(1, 1)
    glVertex3f(x_end, 0.01, z_end)
    glTexCoord2f(0, 1)
    glVertex3f(x_start, 0.01, z_end)

    glEnd()

def draw_skybox(texture):
    size = 20
    glBindTexture(GL_TEXTURE_2D, texture)

    glBegin(GL_QUADS)

    # Fața față
    glTexCoord2f(0, 0)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, -size, -size)
    glTexCoord2f(1, 1)
    glVertex3f(size, size, -size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, size, -size)

    # Fața spate
    glTexCoord2f(0, 0)
    glVertex3f(size, -size, size)
    glTexCoord2f(1, 0)
    glVertex3f(-size, -size, size)
    glTexCoord2f(1, 1)
    glVertex3f(-size, size, size)
    glTexCoord2f(0, 1)
    glVertex3f(size, size, size)

    # Fața stânga
    glTexCoord2f(0, 0)
    glVertex3f(-size, -size, size)
    glTexCoord2f(1, 0)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 1)
    glVertex3f(-size, size, -size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, size, size)

    # Fața dreapta
    glTexCoord2f(0, 0)
    glVertex3f(size, -size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, -size, size)
    glTexCoord2f(1, 1)
    glVertex3f(size, size, size)
    glTexCoord2f(0, 1)
    glVertex3f(size, size, -size)

    # Fața sus
    glTexCoord2f(0, 0)
    glVertex3f(-size, size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, size, -size)
    glTexCoord2f(1, 1)
    glVertex3f(size, size, size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, size, size)

    # Fața jos
    glTexCoord2f(0, 0)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, -size, -size)
    glTexCoord2f(1, 1)
    glVertex3f(size, -size, size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, -size, size)

    glEnd()

def draw_house(x, z, texture_wall, texture_roof, texture_door):
    glPushMatrix()
    glTranslatef(x, 0, z)

    width = 1.5  # Lățimea casei
    height = 3.5  # Înălțimea casei
    roof_height = height + 2.0  # Mai înalt cu 2 unități
    roof_extension = 0.5  # Extensia acoperișului (prispa)

    # Desenăm pereții casei
    glBindTexture(GL_TEXTURE_2D, texture_wall)
    glBegin(GL_QUADS)

    # Față (cu ușă în centru)
    glTexCoord2f(0, 0); glVertex3f(-width, 0, -width)
    glTexCoord2f(1, 0); glVertex3f(width, 0, -width)
    glTexCoord2f(1, 1); glVertex3f(width, height, -width)
    glTexCoord2f(0, 1); glVertex3f(-width, height, -width)

    # Spate
    glTexCoord2f(0, 0); glVertex3f(width, 0, width)
    glTexCoord2f(1, 0); glVertex3f(-width, 0, width)
    glTexCoord2f(1, 1); glVertex3f(-width, height, width)
    glTexCoord2f(0, 1); glVertex3f(width, height, width)

    # Stânga
    glTexCoord2f(0, 0); glVertex3f(-width, 0, width)
    glTexCoord2f(1, 0); glVertex3f(-width, 0, -width)
    glTexCoord2f(1, 1); glVertex3f(-width, height, -width)
    glTexCoord2f(0, 1); glVertex3f(-width, height, width)

    # Dreapta
    glTexCoord2f(0, 0); glVertex3f(width, 0, -width)
    glTexCoord2f(1, 0); glVertex3f(width, 0, width)
    glTexCoord2f(1, 1); glVertex3f(width, height, width)
    glTexCoord2f(0, 1); glVertex3f(width, height, -width)

    glEnd()

    # Ușă (plasată în centru și orientată corect pentru case paralele)
    glBindTexture(GL_TEXTURE_2D, texture_door)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-0.5, 0, -width - 0.01)
    glTexCoord2f(1, 0); glVertex3f(0.5, 0, -width - 0.01)
    glTexCoord2f(1, 1); glVertex3f(0.5, 2, -width - 0.01)
    glTexCoord2f(0, 1); glVertex3f(-0.5, 2, -width - 0.01)
    glEnd()

    # Acoperiș complet cu toate laturile și extensie
    glBindTexture(GL_TEXTURE_2D, texture_roof)
    glBegin(GL_TRIANGLES)

    # Față a acoperișului
    glTexCoord2f(0.5, 1); glVertex3f(0, roof_height, 0)
    glTexCoord2f(0, 0); glVertex3f(-width - roof_extension, height, -width)
    glTexCoord2f(1, 0); glVertex3f(width + roof_extension, height, -width)

    # Spate a acoperișului
    glTexCoord2f(0.5, 1); glVertex3f(0, roof_height, 0)
    glTexCoord2f(0, 0); glVertex3f(-width - roof_extension, height, width)
    glTexCoord2f(1, 0); glVertex3f(width + roof_extension, height, width)

    glEnd()

    # Laturi laterale ale acoperișului
    glBegin(GL_TRIANGLES)

    # Stânga laterală a acoperișului
    glTexCoord2f(0.5, 1); glVertex3f(0, roof_height, 0)
    glTexCoord2f(0, 0); glVertex3f(-width - roof_extension, height, -width)
    glTexCoord2f(1, 0); glVertex3f(-width - roof_extension, height, width)

    # Dreapta laterală a acoperișului
    glTexCoord2f(0.5, 1); glVertex3f(0, roof_height, 0)
    glTexCoord2f(0, 0); glVertex3f(width + roof_extension, height, -width)
    glTexCoord2f(1, 0); glVertex3f(width + roof_extension, height, width)
    glEnd()

    # Podea acoperișului
    glBindTexture(GL_TEXTURE_2D, texture_roof)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-width - roof_extension, height, -width)
    glTexCoord2f(1, 0); glVertex3f(width + roof_extension, height, -width)
    glTexCoord2f(1, 1); glVertex3f(width + roof_extension, height, width)
    glTexCoord2f(0, 1); glVertex3f(-width - roof_extension, height, width)
    glEnd()

    glPopMatrix()

def draw_road_and_sidewalks(road_texture, sidewalk_texture, wall_texture, roof_texture, door_texture, cristi_texture, raul_texture):


    # Desenăm asfaltul principal
    draw_sidewalk(-10, -8.5, -10, 10, sidewalk_texture)  # Stânga
    draw_sidewalk(-8.5, 10, 8.5, 10, sidewalk_texture)  # Sus
    draw_sidewalk(10, 8.5, -10, 8.5, sidewalk_texture)  # Dreapta
    draw_sidewalk(8.5, -8.5, -10, -8.5, sidewalk_texture)  # Jos (corectat)
    


    # Desenăm trotuarele pe marginea drumului
    draw_road(-13, -10, -13, 13, road_texture)  # Stânga
    draw_road(10, 13, -13, 13, road_texture)  # Dreapta
    draw_road(-10, 10, -13, -10, road_texture)  # Jos
    draw_road(-10, 10, 10, 13, road_texture)  # Sus

    # Adăugăm trotuarele exterioare (păstrăm lățimea de 1.5 unități)
    draw_sidewalk(-14.5, -13, -14.5, 14.5, sidewalk_texture)  # Stânga
    draw_sidewalk(13, 14.5, -14.5, 14.5, sidewalk_texture)  # Dreapta
    draw_sidewalk(-13, 13, -14.5, -13, sidewalk_texture)  # Jos
    draw_sidewalk(-13, 13, 13, 14.5, sidewalk_texture)  # Sus

    # Desenăm trotuarele care împart platforma în 4 parcele egale
    draw_sidewalk(-1.5, 1.5, -8.5, -1.5, sidewalk_texture)  # Stânga-jos
    draw_sidewalk(-1.5, 1.5, 1.5, 8.5, sidewalk_texture)   # Stânga-sus
    draw_sidewalk(1.5, 8.5, -1.5, 1.5, sidewalk_texture)   # Dreapta-sus
    draw_sidewalk(1.5, -8.5, 1.5, -1.5, sidewalk_texture)  # Dreapta-jos (poziționat corect)

    draw_house(-5, -5, wall_texture, roof_texture, door_texture)
    draw_house(-5, 5, wall_texture, roof_texture, door_texture)
    draw_house(5, -5, wall_texture, roof_texture, door_texture)
    draw_house(5, 5, wall_texture, roof_texture, door_texture)

    draw_box(-5, 2.55, -6.52, 1, 1, 0.05, cristi_texture)
    draw_box(5, 2.55, -6.52, 1, 1, 0.05, raul_texture)

    # Desenăm iarba în afara trotuarelor
    draw_platform(road_texture)

def draw_box(x, y, z, width, height, depth, texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glPushMatrix()
    glTranslatef(x, y, z)
    
    w = width / 2
    h = height / 2
    d = depth / 2

    glBegin(GL_QUADS)

    # Fața de sus
    glTexCoord2f(0, 0); glVertex3f(-w,  h, -d)
    glTexCoord2f(1, 0); glVertex3f( w,  h, -d)
    glTexCoord2f(1, 1); glVertex3f( w,  h,  d)
    glTexCoord2f(0, 1); glVertex3f(-w,  h,  d)

    # Fața de jos
    glTexCoord2f(0, 0); glVertex3f(-w, -h, -d)
    glTexCoord2f(1, 0); glVertex3f( w, -h, -d)
    glTexCoord2f(1, 1); glVertex3f( w, -h,  d)
    glTexCoord2f(0, 1); glVertex3f(-w, -h,  d)

    # Fața frontală
    glTexCoord2f(0, 0); glVertex3f(-w, -h,  d)
    glTexCoord2f(1, 0); glVertex3f( w, -h,  d)
    glTexCoord2f(1, 1); glVertex3f( w,  h,  d)
    glTexCoord2f(0, 1); glVertex3f(-w,  h,  d)

    # Fața spate
    glTexCoord2f(0, 0); glVertex3f( w, -h, -d)
    glTexCoord2f(1, 0); glVertex3f(-w, -h, -d)
    glTexCoord2f(1, 1); glVertex3f(-w,  h, -d)
    glTexCoord2f(0, 1); glVertex3f( w,  h, -d)

    # Fața stângă
    glTexCoord2f(0, 0); glVertex3f(-w, -h, -d)
    glTexCoord2f(1, 0); glVertex3f(-w, -h,  d)
    glTexCoord2f(1, 1); glVertex3f(-w,  h,  d)
    glTexCoord2f(0, 1); glVertex3f(-w,  h, -d)

    # Fața dreaptă
    glTexCoord2f(0, 0); glVertex3f( w, -h,  d)
    glTexCoord2f(1, 0); glVertex3f( w, -h, -d)
    glTexCoord2f(1, 1); glVertex3f( w,  h, -d)
    glTexCoord2f(0, 1); glVertex3f( w,  h,  d)

    glEnd()
    
    glPopMatrix()

def draw_bench(x, y, z, bench_texture, angle=0):
    glPushMatrix()

    # Aplică rotația doar dacă e necesar
    if (angle !=0 ):
        glTranslatef(x, y, z)
        glRotatef(angle, 0, 1, 0)
        glTranslatef(-x, -y, -z)

    # Scaunul băncii
    glBindTexture(GL_TEXTURE_2D, bench_texture)
    draw_box(x, y, z, 3.0, 0.2, 0.8, bench_texture)

    # Spătarul băncii
    glBindTexture(GL_TEXTURE_2D, bench_texture)
    draw_box(x, y + 0.4, z - 0.3, 3.0, 0.6, 0.2, bench_texture)

    # Picioarele băncii (negre) - fără textură
    glColor3f(0, 0, 0)  # Negru
    draw_box(x - 1.25, y - 0.6, z, 0.15, 1.2, 0.15, 0)
    draw_box(x + 1.25, y - 0.6, z, 0.15, 1.2, 0.15, 0)

    # Resetare culoare la alb pentru alte obiecte
    glColor3f(1, 1, 1)

    glPopMatrix()        
    
def draw_benches(bench_texture):
    draw_bench(  2, 0.5, -6, bench_texture, 270)  # În fața casei din dreapta-jos  
    draw_bench(  -2, 0.5, 6, bench_texture, 90)  # În fața casei din dreapta-jos 
    draw_bench(  -2, 0.5, -6, bench_texture, 90)  # În fața casei din dreapta-jos 
    draw_bench(  2, 0.5, 6, bench_texture, 270)  # În fața casei din dreapta-jos 
   
    

def draw_trash_can(x, y, z, can_texture):
    # Coșul de gunoi (cilindru)
    glBindTexture(GL_TEXTURE_2D, can_texture)
    glPushMatrix()
    glTranslatef(x, y, z)  # Lăsăm cilindrul direct pe sol
    glRotatef(-90, 1, 0, 0)  # Rotește cilindrul pentru a sta vertical

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluCylinder(quadric, 0.25, 0.25, 1.2, 20, 20)  # Cilindru de bază
    gluDeleteQuadric(quadric)

    glPopMatrix()

def draw_shadow(x, y, z):
    glPushMatrix()
    
    glTranslatef(x, y - 0.01, z)  # Poziționează umbra sub obiect (ajustează -0.01 pentru a nu fi exact pe sol)
    glScalef(1.2, 0.01, 1.2)  # Așezăm umbra pe sol și o scalăm pentru efect
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(0.0, 0.0, 0.0, 0.4)  # negru transparent

    # Desenează pătratul umbră
    glBegin(GL_QUADS)
    glVertex3f(-0.3, 0.0, -0.3)
    glVertex3f( 0.3, 0.0, -0.3)
    glVertex3f( 0.3, 0.0,  0.3)
    glVertex3f(-0.3, 0.0,  0.3)
    glEnd()
    glDisable(GL_BLEND)
    glColor4f(1.0, 1.0, 1.0, 1.0)  # resetăm culoarea
    
    glPopMatrix()
