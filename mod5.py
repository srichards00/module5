# module 5

class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)
print("box: ", box)
print("bomb: ", bomb)

# To create_rectangle
    # operation: create a new instance of Rectangle.
def create_rectangle(x, y, width, height):
    posn = Point(x, y)
    rec = Rectangle(posn, width, height)
    return rec

# To str_rectangle
    # operation: convert given Rectangle instance into string of form (x, y, w, h).
def str_rectangle(rec):
    return(rec.corner.x, rec.corner.y, rec.width, rec.height)

# To shift_rectangle
    # operation: change the x and y coordinates of the given Rectangle instance.
def shift_rectangle(rec, dx, dy):
    rec.corner.x += dx
    rec.corner.y += dy

# To offset_rectangle
    # operation: create a new Rectangle instance which is offset from the given
    # instance in x and y coordinates by dx and dy respectively.
def offset_rectangle(rec, dx, dy):
    x = rec.corner.x + dx
    y = rec.corner.y + dx
    return(create_rectangle(x, y, rec.width, rec.height))

r1 = create_rectangle(10, 20, 30, 40)
print(str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print(str_rectangle(r1))

r2 = offset_rectangle(r1, 100, 100)
print(str_rectangle(r1)) #should be same as previous
print(str_rectangle(r2))
