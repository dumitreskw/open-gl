# Skyblock World – OpenGL

Un proiect 3D realizat în Python cu PyOpenGL și GLFW, care simulează o lume de tip „skyblock" cu case, drumuri, bănci și coșuri de gunoi.

---

## Cerințe

- Python 3.x
- PyOpenGL
- PyOpenGL_accelerate
- glfw
- Pillow
- numpy

Instalare rapidă:
```bash
pip install PyOpenGL PyOpenGL_accelerate glfw Pillow numpy
```

---

## Pornire

```bash
python main.py
```

---

## Controale

### Cameră (mod spectator)
| Tastă | Acțiune |
|-------|---------|
| `W` | Mergi înainte |
| `S` | Mergi înapoi |
| `A` | Mergi la stânga |
| `D` | Mergi la dreapta |
| `SPACE` | Urci în sus |
| `LEFT SHIFT` | Cobori în jos |
| `Q` | Rotești camera (roll stânga) |
| `E` | Rotești camera (roll dreapta) |
| Mouse | Rotești privirea (yaw + pitch) |

### Player (cubul roșu)
| Tastă | Acțiune |
|-------|---------|
| `↑` (săgeată sus) | Mergi înainte |
| `↓` (săgeată jos) | Mergi înapoi |
| `←` (săgeată stânga) | Mergi la stânga |
| `→` (săgeată dreapta) | Mergi la dreapta |

---

## Funcționalități

### Lume 3D
- Platformă mare acoperită cu textură de iarbă
- Skybox pe toate cele 6 fețe cu textură de cer
- Iluminare directională (lumină de apus, caldă)
- Iluminare ambientală globală

### Drumuri și trotuare
- Drum asfaltat care împrejmuiește zona centrală
- Trotuare interioare și exterioare
- Căi pietonale care împart platforma în 4 parcele

### Case
- 4 case dispuse în colțurile platformei
- Pereți cu textură de zidărie
- Acoperiș triunghiular cu prispe
- Ușă texturată pe fațada fiecărei case
- Tablouri/plăcuțe cu texturi personalizate (`cristi_texture`, `raul_texture`) pe două case

### Bănci
- 4 bănci amplasate în fața caselor
- Scaun și spătar cu textură de lemn
- Picioare negre (fără textură)
- Fiecare bancă este rotită corect față de casă

### Coșuri de gunoi
- 4 coșuri cilindrice metalice, câte unul lângă fiecare bancă
- Material metalic lucios (shininess ridicat)
- Textură aplicată pe suprafața cilindrului

### Player
- Cub roșu care se mișcă independent de cameră
- Sistem de coliziune cu casele, băncile, coșurile și pereții invizibili ai lumii
- Nu poate ieși din limitele hărții

### Cameră
- Mod spectator liber – poate zbura oriunde în scenă
- Controlul privirii prin mișcarea mouse-ului
- Suport pentru roll (rotație pe axa Z)
- Limitare pitch între -89° și +89° (nu se poate întoarce complet)

---

## Structura fișierelor

| Fișier | Rol |
|--------|-----|
| `main.py` | Inițializare GLFW/OpenGL, bucla principală de randare |
| `camera.py` | Logica camerei (mișcare, rotație, gluLookAt) |
| `player.py` | Logica playerului (mișcare, coliziuni, desenare cub) |
| `graphics.py` | Funcții de desenare (platformă, case, drumuri, bănci, coșuri, skybox) |
| `textures.py` | Încărcarea texturilor cu Pillow + OpenGL |
| `input.py` | Gestionarea tastaturii și mouse-ului prin callback-uri GLFW |
