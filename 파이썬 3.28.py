import turtle
t = turtle.Turtle()
t.shape('turtle')

t.width(9)  #선의 두께 9로 지정
t.shapesize(2, 2)  #거북이 가로 세로 2배 확대

for i in range(0, 11):  #10번 반복
    k = input('키 입력 :')
    if k == 'a':  #a 입력시 거북이 기준 왼쪽으로 90도 앞으로 50만큼 이동
        t.left(90)
        t.forward(50)

    if k == 'd':  #d를 입력시 거북이 기준 오른쪽으으로 90도 앞으로 50만큼 이동
        t.right(90)
        t.forward(50)

    if k == 'w':  #w를 입력시 거북이 기준 앞으로 50만큼 이동
        t.forward(50)

    if k == 's':  #s를 입력시 거북이 기준 뒤쪽으로 180도 앞으로 50만큼 이동
        t.right(180)
        t.forward(50)

        
