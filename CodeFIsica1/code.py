import pygame
import sys
import math
from matplotlib import pyplot as plt


def draw_fondo():
    fondo = pygame.image.load("paisajesdebosque.jpg").convert()
    fondo = pygame.transform.scale(fondo, (800, 600))
    ventana.blit(fondo, (0, 0))


def draw_proyectil():
    image = pygame.image.load("proyectil.png").convert()
    image = pygame.transform.scale(image, (100, 100))
    ventana.blit(image, (-30, 510))


def frange(start, final, incremento):
    nombres = []
    while start < final:
        nombres.append(start)
        start = start + incremento
    return nombres


# def draw_grafico(x, y):
#   plt.plot(x, y)
#  plt.xlabel('x - coordenadas')
# plt.ylabel('y - coordenadas')
# plt.title(' protectil de una bola')

# funcion donde nos dibuja la trayactoria
def draw_trayectoria(u, theta, gravedad, x, y):
    # conventimos a radianes
    theta = math.radians(theta)

    # calculamos tiempo de vuelo del objeto
    t_vuelo = 2 * u + math.sin(theta) / gravedad
    # utilizamos intervalos desde el inicio hasta el vuelo con nintervales de 0.01
    intervalos = frange(0, t_vuelo, 0.01)
    # lista de y x cordenas de tracyetoria del proyectil

    for t in intervalos:
        # los valores de u de x u de y los guardamos en listas
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * gravedad * t * t)
        # draw_grafico(x, y)

        # Ux = u * math.cos(theta) * t
        # Uy = u * math.sin(theta) * t - 0.5 * gravedad * t * t
        # print("x: ", Ux, " y: ", Uy)


# draw_trayectoria(60, 45, 9.8)

class Coordenadas():
    def cuadro_mostrar_cordenada(slef, surf, xCord, yCord, font):
        labelX = font.render("x cordenada: " + str(xCord), 1, (255, 0, 0))
        labelY = font.render("y cordenada: " + str(yCord), 1, (255, 0, 0))
        # asignamos colores
        surf.fill((0, 0, 0))
        surf.blit(labelX, (10, 10))
        surf.blit(labelY, (10, 40))


cordenadas = Coordenadas()

width = 800
height = 600
fps = 60

velocidad = 90
angulo = 60
gravedad = 9.8

x = []
y = []

draw_trayectoria(velocidad, angulo, gravedad, x, y)

pygame.init()

ventana = pygame.display.set_mode((width, height))
cordenadasFont = pygame.font.SysFont("Comic sans MS", 20)
textoSurface = pygame.Surface((350, 80))

time = pygame.time.Clock()

correrVentana = True

draw_fondo()

while correrVentana:
    # se activa catidad de frame por un segundo
    tick = time.tick(fps) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correrVentana = False

    # decimos que mientras alla una cordena nos muestre de las baja a la mas alta
    if (len(x) > 0 and len(y) > 0):
        xCoordenada = x.pop(0)
        yCoordenada = y.pop(0)
        cordenadas.cuadro_mostrar_cordenada(textoSurface, xCoordenada, yCoordenada, cordenadasFont)
        ventana.blit(textoSurface, (0, 0))
        # le pedimos que nos dibuje una rectangulo asiganmos los valores
        pygame.draw.rect(ventana, (0, 255, 0), (xCoordenada, height - yCoordenada, 15, 15))
        draw_proyectil()
    pygame.display.flip()
pygame.quit()
