#turtle es una forma de crear dibujos sencillos en python
import turtle

turtle.shape("turtle")
turtle.left(45)
turtle.forward(50)
turtle.right(65)
turtle.circle(150,350)
turtle.home()
big=("Arial", 36, "normal")
turtle.penup()
turtle.goto(-40,150)
turtle.write("Hola mundo!", font=big)
turtle.home()
turtle.back(20)
turtle.exitonclick()


