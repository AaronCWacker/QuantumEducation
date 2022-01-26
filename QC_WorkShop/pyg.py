import win32api
import win32con
import win32gui
import pygame


pygame.init()
icon = pygame.image.load("surf-van.png")
screen = pygame.display.set_mode((1365, 750), 1, pygame.NOFRAME)
pygame.display.set_icon(icon)
pygame.display.set_caption("Moving Vehicles")
left = False
pink = (255, 192, 203)  # Transparency color
x = -1000


# Variables
vehicle = pygame.image.load("surf-van.png")
y = 300
endpoint = 3000
speed = 0.5

# Set window transparency color
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*pink), 0, win32con.LWA_COLORKEY)


def boatie(x, y) :
    screen.blit(vehicle, (x, y))
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.fill(pink)  # Transparent background
    x += speed
    if x > endpoint:
        x = -1000

    boatie(x, y)
    pygame.display.update()