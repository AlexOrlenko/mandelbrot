"""
Mandelbrot fractal generator
"""

import pygame

W = 640    # window's width
H = 480    # window's height

def draw(window, left = -2, right = 1, top = 1, bottom = -1, iterations = 200):
    """
    Renders the fractal.
    Arguments:
        window - the pygame window;
        left - real part of the view's top-left corner coordinate on the complex plane,
        right - real part of the bottom-right coordinate,
        top - imaginary part of the top-left coordinate,
        bottom - imaginary part of the bottom-right coordinate,
        iterations - maximum number of iterations.
    """
    size_x = float(right - left)
    size_y = float(top - bottom)
    step_x = size_x / W
    step_y = size_y / H
    O_x = abs(left)/size_x * W
    O_y = abs(top)/size_y * H
    sx = lambda x: int(O_x + x*W/size_x)
    sy = lambda y: int(O_y - y*H/size_y)
    def frange(start, end, step):
        while start < end:
            yield start
            start += step

    colors = [(i % 256, i % 256, i % 256) for i in reversed(xrange(iterations + 1))]

    for x in frange(left, right, step_x):
        for y in frange(bottom, top, step_y):
            z = 0 + 0j
            c = complex(x, y)
            i = 0
            while i < iterations:
                i += 1
                z = z**2 + c
                if abs(z) > 2:
                    break
            window.set_at((sx(x),sy(y)), colors[i])
        pygame.display.flip()

def main():
    pygame.init()
    window = pygame.display.set_mode((W, H))

    #draw(window, top = 0.83, bottom = 0.82, left = -0.24, right = -0.22)
    draw(window)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == '__main__':
    main()
