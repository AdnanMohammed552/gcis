import turtle 

def draw_sides(width,height):
    turtle.pencolor('black')
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)


def draw_rectangle(x,y,width,height,color):
    
    turtle.begin_fill()
    turtle.color(color)

    turtle.penup()
    turtle.goto(x,y)
    draw_sides(width,height)

    turtle.end_fill()

    return x+ (width/2) , y- (height/2)

def draw_circle(x,y,raduis,color):
    turtle.penup()
    turtle.goto(x+raduis,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(raduis)
    turtle.end_fill()
    
def draw_flagpole(x, y, height, color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.right(180)
    turtle.begin_fill()
    turtle.color(color)
    turtle.forward(height)
    turtle.end_fill()
    turtle.left(90)
    

def draw_flag(x, y, scale_factor,height,width):

    screen = turtle.Screen()
    screen.bgcolor("#ADD8E6") 
    center_x , center_y = draw_rectangle(x*scale_factor,y*scale_factor,width*scale_factor,height*scale_factor,'red')
    draw_circle(center_x , center_y,3*scale_factor,'white')
    draw_flagpole((x*scale_factor)-3,y*scale_factor,height*scale_factor*2,'black')
    
    
    


draw_flag(x=-20,y=20,scale_factor=10,height=10,width=15)
draw_flag(x=0,y=30,scale_factor=5,height=10,width=15)

turtle.done()