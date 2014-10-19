import math
import turtle
import time

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
        return "%s(%s,%s)" % (self.tag,self.beg,self.end)

    def draw(self,pen):
        """draw the line using the provided pen"""
        pen.pencolor(self.pencolor)
        if pen.pos() != self.beg:
            pen.up()
            pen.goto(self.beg)
        pen.down()
        pen.goto(self.end)
        

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
        vertexStr = ",".join([str(v) for v in self.vertices])
        return "%s(%s)" % (self.tag,vertexStr)

    def draw(self, pen):
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
        
class Triangle(Polygon):
    def __init__(self, coord1 = (0.0,0.0), coord2 = (100.0,0.0),
                 coord3 = (50.0,50.0), fillcolor = '', pencolor = 'black'):
        Polygon.__init__(self, [coord1,coord2,coord3], fillcolor, pencolor)
        self.tag = "Triangle"




##        self.vertices = vertices
##        self.pencolor, self.fillcolor = pencolor, fillcolor
##        Polygon.__init__(self, self.vertices, self.pencolor, self.fillcolor)
##        self.tag = "Triangle"
##    def __str__(self):
##        vertexStr = ",".join([str(v) for v in self.vertices])
##        return "%s(%s)" % (self.tag,vertexStr)
##    def draw(self,pen):
##        lines = []
##        vertices = self.vertices
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
        

class Rectangle(object):
    def __init__(self, vertices = [], fillcolor = '', pencolor = 'black'):
        '''Vertices of the lower left corner and upper right corner for the shape'''
        self.vertices = vertices
        self.pencolor, self.fillcolor = pencolor, fillcolor
        Polygon.__init__(self, self.vertices, self.pencolor, self.fillcolor)
        self.tag = "Rectangle"
    def __str__(self):
        vertexStr = ",".join([str(v) for v in self.vertices])
        return "%s(%s)" % (self.tag,vertexStr)
    def draw(self, pen):
        lines = []
        vertice = self.vertices
        print(vertice)
        newlist=[]
        for i in vertice:
            for number in i:
                n=int(number)
                newlist.append(n)
        print(newlist)
        
        vertices=[(int(newlist[0]),int(newlist[1])),(int(newlist[0]),int(newlist[3])),(int(newlist[1]),int(newlist[3])),(int(newlist[1]),int(newlist[2]))]
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

class Circle(object):
    def __init__(self,center = (0,0),radius = 10, fillcolor = 'red', pencolor = 'yellow'):
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
        pen.goto(self.center)
        pen.circle(self.radius)
        pen.end_fill()

def main():
    pen = turtle.Turtle()
    
    lines = [Line((0,0),(40,20)), Line((0,20), (40,0), "red")]
    print(lines)
    for line in lines:
        print (line, end=" ")
        line.draw(pen)
    print()

    p = Polygon([(100,0),(200,0),(200,50),(100,50)], fillcolor="blue")
    p.draw(pen)
    print (p)
    t = Triangle((10,20),(20,0),(0,0),'black','blue')
    t.draw(pen)
    print (t)
    r = Rectangle([(-50,0),(0,50)],fillcolor = 'red')
    r.draw(pen)
    print(r)
    c = Circle((-50,0),100,fillcolor = 'red', pencolor = 'blue')
    c.draw(pen)
    print(c)
    pen.hideturtle()
    time.sleep(5)
    turtle.bye()

main()


      
