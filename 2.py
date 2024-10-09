import turtle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 3D Рекурсивный способ для тетраэдра Серпинского
def midpoint(p1, p2):
    return [(p1[i] + p2[i]) / 2 for i in range(len(p1))]

def sierpinski_tetrahedron(vertices, depth, ax):
    if depth == 0:
        faces = [
            [vertices[0], vertices[1], vertices[2]],
            [vertices[0], vertices[1], vertices[3]],
            [vertices[0], vertices[2], vertices[3]],
            [vertices[1], vertices[2], vertices[3]]
        ]
        poly = Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='black', alpha=0.5)
        ax.add_collection3d(poly)
        plt.draw()
        plt.pause(0.1)
    else:
        midpoints = [
            midpoint(vertices[0], vertices[1]),
            midpoint(vertices[0], vertices[2]),
            midpoint(vertices[0], vertices[3]),
            midpoint(vertices[1], vertices[2]),
            midpoint(vertices[1], vertices[3]),
            midpoint(vertices[2], vertices[3])
        ]
        sierpinski_tetrahedron([vertices[0], midpoints[0], midpoints[1], midpoints[2]], depth - 1, ax)
        sierpinski_tetrahedron([midpoints[0], vertices[1], midpoints[3], midpoints[4]], depth - 1, ax)
        sierpinski_tetrahedron([midpoints[1], midpoints[3], vertices[2], midpoints[5]], depth - 1, ax)
        sierpinski_tetrahedron([midpoints[2], midpoints[4], midpoints[5], vertices[3]], depth - 1, ax)

# Итеративный способ с помощью L-системы (2D)
def sierpinski_l_system(axiom, rules, iterations):
    for _ in range(iterations):
        new_axiom = ""
        for char in axiom:
            new_axiom += rules.get(char, char)
        axiom = new_axiom
    return axiom

def draw_l_system(t, instructions, length, angle):
    for command in instructions:
        if command == 'F':
            t.forward(length)
        elif command == '+':
            t.left(angle)
        elif command == '-':
            t.right(angle)

# Основная программа
def main():
    choice = input("Выберите метод построения фрактала: '3D' для рекурсивного способа, '2D' для L-системы: ").strip().lower()
    
    if choice == '3d':
        # 3D рекурсивное построение
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Определение начальных вершин тетраэдра
        vertices = [
            [0, 0, 0],
            [1, 0, 0],
            [0.5, np.sqrt(3) / 2, 0],
            [0.5, np.sqrt(3) / 6, np.sqrt(2 / 3)]
        ]
        
        # Рисование фрактала
        sierpinski_tetrahedron(vertices, 3, ax)
        
        # Настройки отображения графика
        ax.set_axis_off()
        plt.show()

    elif choice == '2d':
        # 2D Итеративное построение с помощью L-системы
        axiom = "F-G-G"
        rules = {
            'F': "F-G+F+G-F",
            'G': "GG"
        }
        iterations = 4

        # Генерация строки L-системы
        instructions = sierpinski_l_system(axiom, rules, iterations)

        # Инициализация turtle
        screen = turtle.Screen()
        screen.bgcolor("white")
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(-200, -150)
        t.pendown()

        # Рисование фрактала
        draw_l_system(t, instructions, 5, 120)
        turtle.done()

    else:
        print("Неверный ввод. Пожалуйста, выберите '3D' или '2D'.")

if __name__ == "__main__":
    main()
