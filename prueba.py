import turtle

# Configuración de la pantalla
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Dibujo del nombre Jonathan")

# Configuración del lápiz
pen = turtle.Turtle()
pen.speed(1)
pen.color("blue")
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# Dibujo de la letra "J"
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(60)
pen.right(180)
pen.forward(120)

# Movimiento del lápiz para dibujar la letra "O"
pen.penup()
pen.goto(-70, 0)
pen.pendown()

# Dibujo de la letra "O"
pen.circle(30)

# Movimiento del lápiz para dibujar la letra "N"
pen.penup()
pen.goto(10, 0)
pen.pendown()

# Dibujo de la letra "N"
pen.left(90)
pen.forward(100)
pen.right(135)
pen.forward(140)
pen.left(135)
pen.forward(100)

# Movimiento del lápiz para dibujar la letra "A"
pen.penup()
pen.goto(130, 0)
pen.pendown()

# Dibujo de la letra "A"
pen.left(75)
pen.forward(140)
pen.right(150)
pen.forward(140)
pen.backward(70)
pen.right(75)
pen.backward(50)

# Mantener la pantalla abierta hasta que se haga clic en ella
wn.exitonclick()
