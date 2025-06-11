import pygame
import random
import sys
import time

# Colores
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
PINK = (255, 105, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Constantes
TILE_SIZE = 24

# Mapas predefinidos (tres mapas grandes)
def mapas_predefinidos():
    mapas = [
        [
    "1111111111111111111111111111",
    "1000000000110000000000000001",
    "1011111110110111111111111101",
    "1011111110110111111111111101",
    "1011111110110111111111111101",
    "1000000000000000000000000001",
    "1011110111111111111011111101",
    "1000000100000000001010000001",
    "1111010101110111011010111111",
    "1111110101X101X1011010111111",
    "1111110101110111011010111111",
    "1000000000000000000000000001",
    "1011110110111111111011011101",
    "10000001100000000011X1000001",
    "1111110110110111011011011111",
    "1111110101000100010010011111",
    "1111110101110111011011011111",
    "1000000000110000000000000001",
    "1011111110110111111111111101",
    "1000000000000000000000000001",
    "1111110111110111111110111111",
    "1111110100000000000000101111",
    "1111110101111111111110101111",
    "1000000000000000000000000001",
    "1011111111110111111111111101",
    "1010000000000100000000000101",
    "1010111111110111111111110101",
    "1000100000000000000000001001",
    "1010111111110111111111110101",
    "1000000000000000000000000001",
    "1111111111111111111111111111",
        ],

        [
        "1111111111111111111111111111",
        "1000000000110000000000000001",
        "1011111110110111111111111101",
        "1010000010000100000000000101",
        "1010111111110111111111110101",
        "1010100000000000000000000101",
        "1010101111110111111111010101",
        "1010101000000100000001010101",
        "1010101011110111111011010101",
        "1000001000000000001000000001",
        "1111110111110111111011111111",
        "1000000100000100001000000001",
        "1011110111110111111011111101",
        "1010000000000000000000000101",
        "1010111111110111111111110101",
        "1010100000000100000000000101",
        "1010101111110111111111010101",
        "1010101000000000000001010101",
        "1010101011110111111011010101",
        "1000001000000000001000000001",
        "1111110111110111111011111111",
        "1000000100000100001000000001",
        "1011110111110111111011111101",
        "1010000000000000000000000101",
        "1010111111110111111111110101",
        "1010100000000100000000000101",
        "1010101111110111111111010101",
        "1010101000000000000001010101",
        "1010101011110111111011010101",
        "1000000000000000000000000001",
        "1111111111111111111111111111"
        ],

        [
        "1111111111111111111111111111",
        "1000000000000000000000000001",
        "1011111111110111111111111101",
        "1000000000000000000000000001",
        "1011111110111111111011111101",
        "1000000000100000001000000001",
        "1011111110110111111011111101",
        "1010000010000100001000000101",
        "1010111111110111111111110101",
        "1000100000000000000000001001",
        "1110111111110111111111110111",
        "1000000000000000000000000001",
        "1011110111110111111011111101",
        "1000000100000000001000000001",
        "1011110101110111011011111101",
        "1000000001010101010000000001",
        "1011111101110111011111111101",
        "1000000000000000000000000001",
        "1011111110110111111111111101",
        "1000000000000000000000000001",
        "1011111110110111111111111101",
        "1000000000000000000000000001",
        "1011111111110111111111111101",
        "1000000000000000000000000001",
        "1011111110111111111011111101",
        "1010000000100000001000000101",
        "1010111111110111111111110101",
        "1000100000000000000000001001",
        "1010111111110111111111110101",
        "1000000000000000000000000001",
        "1111111111111111111111111111"
        ]
    ]
    return mapas

frame_count = 0  # Esto debe estar en el scope global del juego

# Clase Jugador (Pac-Man)
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos_prev = (x, y)
        self.dir = (0, 0)
        self.power_mode = False
        self.power_time = 0

    def mover(self):
        self.pos_prev = (self.x, self.y)
        nx, ny = self.x + self.dir[0], self.y + self.dir[1]
        if mapa[ny][nx] != '1':
            self.x, self.y = nx, ny

    def dibujar(self):
        if self.dir == (0, -1):
            imagen = pacman_up_img
        elif self.dir == (0, 1):
            imagen = pacman_down_img
        elif self.dir == (-1, 0):
            imagen = pacman_left_img
        elif self.dir == (1, 0):
            imagen = pacman_right_img
        else:
            imagen = pacman_right_img
        screen.blit(imagen, (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def activar_power(self):
        self.power_mode = True
        self.power_start_time = pygame.time.get_ticks()

    def actualizar_power(self):
        if self.power_mode:
            tiempo_transcurrido = pygame.time.get_ticks() - self.power_start_time
            if tiempo_transcurrido > 5000:  # 5 segundos
                self.power_mode = False
                # Cuando termina el poder, fantasmas dejan de ser vulnerables
                for f in fantasmas:
                    f.vulnerable = False



# Clase Fantasma
class Fantasma:
    def __init__(self, x, y, color=PINK):
        self.x = x
        self.y = y
        self.pos_prev = (x, y)
        self.color = color
        self.dir = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
        self.vulnerable = False  # Se pone True cuando Pac-Man come fruta

    def mover(self):
        global frame_count
        # Mover fantasmas solo cada 4 frames para que vayan más lentos
        if frame_count % 4 != 0:
            return

        self.pos_prev = (self.x, self.y)

        # Solo persiguen a Pac-Man si no son vulnerables
        if not self.vulnerable:
            # Distancia Manhattan
            distancia = abs(self.x - jugador.x) + abs(self.y - jugador.y)
            if distancia <= 6:
                # Intentar acercarse a Pac-Man
                posibles_dir = [(1,0), (-1,0), (0,1), (0,-1)]
                # Filtrar las direcciones válidas (no paredes)
                valid_moves = []
                for dx, dy in posibles_dir:
                    nx, ny = self.x + dx, self.y + dy
                    if mapa[ny][nx] != '1':
                        valid_moves.append((dx, dy))
                
                # Escoger la dirección que minimice la distancia a Pac-Man
                mejor_dir = self.dir
                min_dist = distancia
                for dx, dy in valid_moves:
                    nx, ny = self.x + dx, self.y + dy
                    dist = abs(nx - jugador.x) + abs(ny - jugador.y)
                    if dist < min_dist:
                        min_dist = dist
                        mejor_dir = (dx, dy)
                self.dir = mejor_dir

        # Movimiento aleatorio ocasional
        if random.random() < 0.3:
            posibles_dir = [(1,0), (-1,0), (0,1), (0,-1)]
            valid_moves = []
            for dx, dy in posibles_dir:
                nx, ny = self.x + dx, self.y + dy
                if mapa[ny][nx] != '1':
                    valid_moves.append((dx, dy))
            if valid_moves:
                self.dir = random.choice(valid_moves)

        # Mover si no hay pared
        nx, ny = self.x + self.dir[0], self.y + self.dir[1]
        if mapa[ny][nx] != '1':
            self.x, self.y = nx, ny

    def dibujar(self):
        if self.vulnerable:
            # Fantasma vulnerable se dibuja azul claro
            screen.blit(ghost_2_img, (self.x * TILE_SIZE, self.y * TILE_SIZE))
        else:
            screen.blit(ghost_img, (self.x * TILE_SIZE, self.y * TILE_SIZE))


# Clase Fruta (Power-up)
class Fruta:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        screen.blit(frutita, (self.x * TILE_SIZE, self.y * TILE_SIZE))

# Inicialización del juego
pygame.init()
mapa = random.choice(mapas_predefinidos())
ROWS = len(mapa)
COLS = len(mapa[0])
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pablo`s come cocos")
clock = pygame.time.Clock()
FPS = 10


# Cargar imágenes
ghost_img = pygame.image.load("assets/ghost.gif").convert_alpha()
ghost_2_img = pygame.image.load("assets/ghost_2.gif").convert_alpha()
pacman_up_img = pygame.image.load("assets/pacman-u 5.gif").convert_alpha()
pacman_down_img = pygame.image.load("assets/pacman-d 5.gif").convert_alpha()
pacman_left_img = pygame.image.load("assets/pacman-l 5.gif").convert_alpha()
pacman_right_img = pygame.image.load("assets/pacman-r 5.gif").convert_alpha()
frutita = pygame.image.load("assets/fruit 1.gif").convert_alpha()

jugador = Jugador(1, 1)

# Generar de 2 a 5 fantasmas en posiciones libres (no paredes)
num_fantasmas = random.randint(5, 7)
posiciones_libres = [(x, y) for y in range(ROWS) for x in range(COLS) if mapa[y][x] == '0' and (x, y) != (jugador.x, jugador.y)]

fantasmas = []
for _ in range(num_fantasmas):
    if posiciones_libres:
        pos = random.choice(posiciones_libres)
        posiciones_libres.remove(pos)
        fantasmas.append(Fantasma(pos[0], pos[1]))

# Comida normal
comida = {(x, y) for y in range(ROWS) for x in range(COLS) if mapa[y][x] == '0'}

# Frutas (power-ups) colocadas aleatoriamente en posiciones de comida
posibles_frutas = list(comida)
frutas = []
for _ in range(random.randint(5,8)):
    if posibles_frutas:
        fx, fy = random.choice(posibles_frutas)
        frutas.append(Fruta(fx, fy))
        posibles_frutas.remove((fx, fy))
        if (fx, fy) in comida:
            comida.remove((fx, fy))  # Quitar la comida normal en la posición de la fruta

# Inicializamos el marcador
puntuacion = 0

# Fuente para mostrar la puntuación
fuente_puntos = pygame.font.SysFont(None, 36)

# Bucle principal
while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                jugador.dir = (0, -1)
            elif evento.key == pygame.K_DOWN:
                jugador.dir = (0, 1)
            elif evento.key == pygame.K_LEFT:
                jugador.dir = (-1, 0)
            elif evento.key == pygame.K_RIGHT:
                jugador.dir = (1, 0)

    jugador.mover()
    jugador.actualizar_power()

    # Si Pac-Man come comida normal
    if (jugador.x, jugador.y) in comida:
        comida.remove((jugador.x, jugador.y))
        puntuacion += 10  # Sumar puntos por comida

    # Si Pac-Man come fruta (power-up)
    for fruta in frutas[:]:
        if (jugador.x, jugador.y) == (fruta.x, fruta.y):
            frutas.remove(fruta)
            jugador.activar_power()
            puntuacion += 25  # Sumar puntos por fruta
            # Fantasmas se vuelven vulnerables
            for f in fantasmas:
                f.vulnerable = True

    # Mover fantasmas y manejar vulnerabilidad
    for f in fantasmas[:]:
        f.mover()

        collision = False
        if (f.x, f.y) == (jugador.x, jugador.y):
            collision = True
        elif (f.x, f.y) == jugador.pos_prev and (jugador.x, jugador.y) == f.pos_prev:
            collision = True

        if collision:
            if f.vulnerable or jugador.power_mode:
                fantasmas.remove(f)  # Fantasma muere
            else:
                # Pac-Man muere
                fuente = pygame.font.SysFont(None, 48)
                texto = fuente.render("¡Has perdido!", True, RED)
                screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2 - texto.get_height() // 2))
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                sys.exit()

    # Verificar si ha ganado (comió toda la comida y frutas o mató a todos los fantasmas)
    if (not comida and not frutas) or not fantasmas:
        fuente = pygame.font.SysFont(None, 48)
        texto = fuente.render("¡Has ganado!", True, GREEN)
        screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2 - texto.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    # Dibujar todo
    screen.fill(BLACK)

    # Dibujar paredes
    for y in range(ROWS):
        for x in range(COLS):
            if mapa[y][x] == '1':
                pygame.draw.rect(screen, BLUE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Dibujar comida
    for cx, cy in comida:
        pygame.draw.circle(screen, WHITE, (cx * TILE_SIZE + TILE_SIZE // 2, cy * TILE_SIZE + TILE_SIZE // 2), 3)

    # Dibujar frutas (power-ups)
    for fruta in frutas:
        fruta.dibujar()

    # Dibujar jugador y fantasmas
    jugador.dibujar()
    for f in fantasmas:
        f.dibujar()

    # Mostrar puntuación en pantalla (esquina superior izquierda)
    texto_puntuacion = fuente_puntos.render(f"Puntos: {puntuacion}", True, YELLOW)
    screen.blit(texto_puntuacion, (10, 10))

    pygame.display.flip()
