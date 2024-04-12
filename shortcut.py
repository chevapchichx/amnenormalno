import turtle

class Point:
    x = 0
    y = 0

class Segment:
    a = -1
    b = -1

points = []
segments = []

def parse_input_point(ip):
    coordinates = ip.split(' ')
    if len(coordinates) != 2:
        print('Точка должна быть задана только 2 числами')
        return
    x = 0
    for i in range(len(coordinates)):
        if coordinates[i].isdigit():
            if i == 0:
                x = int(coordinates[i])
            else:
                y = int(coordinates[i])
                point = Point()
                point.x = x
                point.y = y
                points.append(point)
        else:
            print(f'{coordinates[i]} не является целым числом')

def parse_input_segment(sd):
    path = sd.split(' ')
    if len(path) != 2:
        print('Сегмент должен быть задан только 2 числами')
        return
    a = 0
    for i in range(len(path)):
        if path[i].isdigit():
            if i == 0:
                a = int(path[i])
            else:
                b = int(path[i])
                segment = Segment()
                segment.a = a - 1
                segment.b = b - 1
                if a <= 0 or a > len(points):
                    print(f'Точка {a} не существует')
                    return
                if b <= 0 or b > len(points):
                    print(f'Точка {b} не существует')
                    return
                segments.append(segment)
        else:
            print(f'{path[i]} не является целым числом')

def draw_segment(t,a,b):
    t.penup()
    t.goto(a.x, a.y)
    t.pendown()
    t.goto(b.x, b.y)


while True:
    p = input('Введите координаты точки через пробел или Enter для завершения: ')
    if p == '':
        break
    else:
       parse_input_point(p)

print(f'Вы ввели все точки. Всего введено точек: {len(points)}. Введенные точки: ')
for i in range(len(points)):
    p = points[i]
    print(f'{i+1}: x: {p.x}, y: {p.y}')

print('Создайте сегменты, указывая номера точек через пробел или Enter для завершения (каждый сегмент должен состоят из 2 точек): ')
while True:
    s = input()
    if s == '':
        break
    else:
        parse_input_segment(s)

# print(f'Вы ввели все сегменты. Введенные сегменты: ')
# for i in range(len(segments)):
#     s = segments[i]
#     print(f' Связанные точки: {s.a} и {s.b}')

window = turtle.Screen()
window.bgcolor(50/255,50/255,100/255)
turtle.color("yellow")
turtle.shape("circle")
turtle.turtlesize(0.2)
for i in segments:
    draw_segment(turtle, points[i.a], points[i.b])
turtle.done()

