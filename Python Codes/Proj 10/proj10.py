# Martin Mukasa
# CSE 231 - 009
# 11/ 28/ 2012

import math
import turtle
import time

# This project uses turtle graphics to draw two snow people I have defined at least
# 7 classes and. Also I do the minimum required (# 6) as said in the project description
# At a minimum, a snow person should include three snowballs, drawn one on top of the other, and
# two eyes and a mouth. Feel free to personalize your classes to include other components.
# I talked to the prof. and she said that should be fine.

# This function draws my 3 snow balls one on top of each other.
class Snow_person():

    """Line class"""
    # I set the cirlce/ position of the cricle to draw in the center at 0.
    def __init__(self, pos = (0, 0.0)):
        """
        create a line starting from the coordinates given by beg to
        the coordinates given by end
        """
        self.pos = pos

    def __str__(self):
        """ a conversion method, it returns the string to be used for
        printing an instance in python
        """
        return "%s(%s,%s)" % (self.tag,self.beg,self.end)
    
    def lines(self,pen):
        lines = [Line((100,0),(40,20)), Line((0,20), (40,0), "red")]
        print(lines)
        for line in lines:
            print (line, end=" ")
            line.draw(pen)
        print()

    def draw(self,pen):
       
        x,y = self.pos
        
        """draw the line using the provided pen"""
        # c is my first circle.
        c = Circle((self.pos[0],100),40,fillcolor = 'white', pencolor = 'black')
        c.draw(pen)
        print(c)

        # c2 is my second circle bellow.
        c2 = Circle((self.pos[0],-20),60,fillcolor = 'white', pencolor = 'black')
        c2.draw(pen)
        print(c2)
        # c3 is my thrid circle at the bottom
        c3= Circle((self.pos[0],-180),80,fillcolor = 'white', pencolor = 'black')
        c3.draw(pen)
        print(c3)

        pen.up()
        pen.goto((x-20),(y+155))
        c = Circle(((x-20),(y+130)),7,fillcolor = 'red', pencolor = 'red')
        c.draw(pen)

        pen.up()
        pen.goto((x+20),(y+155))
        c = Circle(((x+20),(y+130)),7,fillcolor = 'red', pencolor = 'red')
        c.draw(pen)
        
        pen.up()
        r = Rectangle(((x-10),(y+115)),((x+10),(y+115)), ((x+10),(y+120)),((x-10),(y+120)))
        r.draw(pen)

# This function draws the snow lady with a ribbon on top of her head.
class Snow_lady(Snow_person):
    def __init__(self, pos = (0, 0.0)):
        """
        create a line starting from the coordinates given by beg to
        the coordinates given by end
        """
        self.pos = pos

    def __str__(self):
        """ a conversion method, it returns the string to be used for
        printing an instance in python
        """
        return "%s(%s,%s)" % (self.tag,self.beg,self.end)

    def draw(self,pen):
        Snow_person.draw(self,pen)
        rect = Rectangle((-37.5,217.5), (-37.5,167.5), (32.5,217.5), (32.5,167.5))
        rect.draw(pen)

# This function draws the snow man with a hat on top of his head.
class Snow_man(Snow_person):
    def __init__(self, pos = (200,0)):
        self.pos = pos

    def __str__(self):
        """ a conversion method, it returns the string to be used for
        printing an instance in python
        """
        return "%s(%s,%s)" % (self.tag,self.beg,self.end)

    def draw(self,pen):
        Snow_person.draw(self,pen)
        rect = Rectangle((172.5,170),(222.5,170),(222.5,220),(172.5,220))
        rect.draw(pen)

        

# This function is used to draw my lines for both the snow man and snow woman.
class Line(object):
    """Line class"""
    def __init__(self, beg = (0.0, 0.0), end = (50.0, 0.0),
                 pencolor = "black"):
        """
        create a line starting from the coordinates given by beg to
        the coordinates given by end
        """
        self.pencolor = pencolor
        self.beg = beg
        self.end = end
        self.tag = "Line"

    def __str__(self):
        """ a conversion method, it returns the string to be used for
        printing an instance in python
        """
        return "%s(%s,%s)" % (self.tag,self.beg,self.end)

    def draw(self,pen):
        """draw the line using the provided pen"""
        pen.pencolor(self.pencolor)
        if pen.pos() != self.beg:
            pen.up()
            pen.goto(self.beg)
        pen.down()
        pen.goto(self.end)

# This function is used to better align the angles and dimenssions for my shapes being drawn.
class Polygon(object):
    """Polygon class"""
    def __init__(self, vertices = [],
                 fillcolor = "", pencolor = "black"):
        """
        create a polygon from a list of its vertices
        """
        self.vertices = vertices
        self.pencolor, self.fillcolor = pencolor, fillcolor
        self.tag = "Poly"

    def __str__(self):
        ''' a conversion method, it returns the string to be used for printing an instance in python '''
        vertexStr = ",".join([str(v) for v in self.vertices])
        return "%s(%s)" % (self.tag,vertexStr)

    def draw(self, pen):
        """draw the line using the provided pen"""
        lines = []
        vertices = self.vertices
        print(vertices)
        if vertices:
            for i in range(len(vertices)-1):
                lines.append(Line(vertices[i],vertices[i+1], self.pencolor))
            lines.append(Line(vertices[-1],vertices[0]))
        pen.color(self.pencolor, self.fillcolor)
        if self.fillcolor: pen.begin_fill()
        for l in lines:
            l.draw(pen)
        pen.end_fill()

# This function is used to draw my triangle for the snow woman.

class Triangle(Polygon):
    def __init__(self, coord1 = (0.0,0.0), coord2 = (100.0,0.0),
                 coord3 = (50.0,50.0), fillcolor = '', pencolor = 'black'):
        Polygon.__init__(self, [coord1,coord2,coord3], fillcolor, pencolor)
        self.tag = "Triangle"

    def __str__(self):
        vertexStr = ",".join([str(v) for v in self.vertices])
        return "%s(%s)" % (self.tag,vertexStr)
    
    def draw(self,pen):
        lines = []
        vertices = self.vertices
        print(vertices)
        if vertices:
            for i in range(len(vertices)-1):
                lines.append(Line(vertices[i],vertices[i+1],self.pencolor))
            lines.append(Line(vertices[-1],vertices[0]))
        pen.color(self.pencolor, self.fillcolor)
        if self.fillcolor: pen.begin_fill()
        for l in lines:
            l.draw(pen)
        pen.end_fill()

# This function is used to draw my rectangle for the snow woman.

class Rectangle(Polygon):
    def __init__(self, cd1 = (0,0), cd2 = (20,0), cd3 = (20,30), cd4 = (0,30), fillcolor = 'green', pencolor = 'black'):
        Polygon.__init__(self,[cd1,cd2,cd3,cd4],fillcolor,pencolor)
        self.tag = 'Rect'
        
    def __str__(self):
        ''' a conversion method, it returns the string to be used for printing an instance in python '''
        vertexStr = ",".join([str(v) for v in self.vertices])
        return "%s(%s)" % (self.tag,vertexStr)

    def draw(self, pen):
        """draw the line using the provided pen"""
        lines = []
        vertices = self.vertices
        print(vertices)
        if vertices:
            for i in range(len(vertices)-1):
                lines.append(Line(vertices[i],vertices[i+1], self.pencolor))
            lines.append(Line(vertices[-1],vertices[0]))
        pen.color(self.pencolor, self.fillcolor)
        if self.fillcolor: pen.begin_fill()
        for l in lines:
            l.draw(pen)
        pen.end_fill()


##class Rectangle(Polygon):
##    def __init__(self, vertices = [], fillcolor = '', pencolor = 'black'):
##        '''This is the constructor that takes arguments indicating the positions of one or more reference points
##        and other arguments appropriate that will define appropriate default values for most of the arguments.'''
##        self.vertices = vertices
##        self.pencolor, self.fillcolor = pencolor, fillcolor
##        Polygon.__init__(self, self.vertices, self.pencolor, self.fillcolor)
##        self.tag = "Rectangle"
##    def __str__(self):
##        """ a conversion method, it returns the string to be used for
##        printing an instance in python
##        """    
##        vertexStr = ",".join([str(v) for v in self.vertices])
##        return "%s(%s)" % (self.tag,vertexStr)
##    def draw(self, pen):
##        """draw the line using the provided pen"""
##        lines = []
##        vertice = self.vertices
##        print(vertice)
##        newlist=[]
##        for i in vertice:
##            for number in i:
##                n=int(number)
##                newlist.append(n)
##        print(newlist)
##        
##        vertices=[(int(newlist[0]),int(newlist[1])),(int(newlist[0]),int(newlist[3])),(int(newlist[1]),int(newlist[3])),(int(newlist[1]),int(newlist[2]))]
##        print(vertices)
##        if vertices:
##            for i in range(len(vertices)-1):
##                lines.append(Line(vertices[i],vertices[i+1],self.pencolor))
##            lines.append(Line(vertices[-1],vertices[0]))
##        pen.color(self.pencolor, self.fillcolor)
##        if self.fillcolor: pen.begin_fill()
##        for l in lines:
##            l.draw(pen)
##        pen.end_fill()
        
# The circle function is used to draw my circles.
class Circle(object):
    def __init__(self,center = (0,0),radius = 0, fillcolor = 'white', pencolor = 'black'):
        '''This is the constructor that takes arguments indicating the positions of one or more reference points
        and other arguments appropriate that will define appropriate default values for most of the arguments.'''
        self.center = center
        self.radius = radius
        self.pencolor, self.fillcolor = pencolor, fillcolor
        self.tag = "Circle"
        
    def __str__(self):
        return "%s(%s,%s)" % (self.tag,self.center,self.radius)
    def draw(self,pen):
        pen.color(self.pencolor, self.fillcolor)
        if self.fillcolor:
            pen.begin_fill()
        print(self.center)
        pen.up()
        pen.goto(self.center)
        pen.down()
        pen.circle(self.radius)
        pen.end_fill()

# The main function is used to run my whole program which then prints out the
# coordinates where my snow person and man are drawn.

def main():
    pen = turtle.Turtle()
    pen.speed(60)

    snowperson = Snow_man()
    snowperson.draw(pen)
    snowperson2 = Snow_lady()
    snowperson2.draw(pen)

main()
