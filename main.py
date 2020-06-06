from declaration import *
import turtle
import random

turtle.tracer(0)
turtle.hideturtle()

colors = ['green', 'blue', 'pink', 'orange', 'red', 'black', 'brown', 'yellow']
lst_ufo = []
turtle.showturtle()
response = turtle.numinput('Ответ', 'Введите желаемое кол-во тарелок:')
if response is None:
    pass
else:
    for i in range(int(response)):
        lst_ufo.append(Ufo('Пришелец-' + str(i), random.randint(-600, 600),
                           random.randint(-600, 600), random.randint(30, 300),
                           colors[random.randint(0, 7)], random.randint(3, 10),
                           random.randint(2, 8)))

while True:
    for i in range(len(lst_ufo)):
        lst_ufo[i].show()
        lst_ufo[i].move()
    turtle.update()
    turtle.clear()

    turtle.listen()

    turtle.onkey(lst_ufo.pop, 'Up')

tr.update()
tr.mainloop()
