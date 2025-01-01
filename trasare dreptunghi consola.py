import turtle
print("Trasarea unui dreptunghi")
lud=int(input("Introduceti lungimea dreptunghiului"))
lad=int(input("Introduceti latimea dreptunghiului"))
culoare=input("Introduceti culoarea dreptunghiului")
d=turtle.Turtle()
d.speed(1)
d.color(culoare)
d.fd(lud)
d.left(90)
d.fd(lad)
d.left(90)
d.fd(lud)
d.left(90)
d.fd(lad)


