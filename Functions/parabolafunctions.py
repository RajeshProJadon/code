import math
try:
    import tkinter
except ImportError:  # Python2
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(-size, size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)

# Modify the circle function so that it allows to colour of circle to be specified
# and defaults to red if a colour is not given. You may want to review the previous lectures
# about named parameters and defaults values.
#


def circle(page, radius, g, h, colour="red"):
    for x in range(g * 100, (g + radius) * 100):
        page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)
        # x /= 100
        # print(x)
        # y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
        # plot(page, x, y)
        # plot(page, x, 2 * h - y)
        # plot(page, 2 * g - x, y)
        # plot(page, 2 * g - x, 2 * h - y)


def draw_axis(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="green")
    page.create_line(0, y_origin, 0, -y_origin, fill="green")
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x+1, -y+1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)
parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, "green")
circle(canvas, 100, 100, -100, "yellow")
circle(canvas, 100, -100, 100, "magenta")
circle(canvas, 100, -100, -100, "blue")
circle(canvas, 10, 30, 30, "navy blue")
circle(canvas, 10, 30, -30, "sky blue")
circle(canvas, 10, -30, 30, "violet")
circle(canvas, 10, -30, -30, "pink")
circle(canvas, 30, 0, 0, "light green")

# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
# canvas2.grid(row=0, column=1)

# print(repr(canvas), repr(canvas2))
# draw_axis(canvas2)

# for x in range(-100, 100):
#     y = parabola(x)
#     # print(y)
#     plot(canvas, x, -y)
#     # plot(canvas2, x, -y)

mainWindow.mainloop()
