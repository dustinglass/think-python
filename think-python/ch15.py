"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

import math
import copy


class Point(object):
    """Represents a point in 2-D space."""


def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)


def distance_between_points(p1, p2):
    """Return the distance between two points.

    Use the equation a^2 + b^2 = c^2."""
    a = float(abs(p1.x - p2.x))
    b = float(abs(p1.y - p2.y))
    c = math.sqrt(a ** 2 + b ** 2)
    return c


class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def move_rectangle(rect, dx, dy):
    """Modify the rectangle by adding to its corner point.

    rect: Rectangle object.
    dx: change in x corner coordinate (can be negative).
    dy: change in y corner coordinate (can be negative).
    """
    rect.corner.x += dx
    rect.corner.y += dy


def copy_move_rectangle(rect, dx, dy):
    """Copy the rectangle and modify the copy according to move_rectangle."""
    rect_copy = copy.deepcopy(rect)
    move_rectangle(rect_copy, dx, dy)
    return rect_copy


def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print 'blank',
    print_point(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print 'center',
    print_point(center)

    print box.width
    print box.height
    print 'grow'
    grow_rectangle(box, 50, 100)
    print box.width
    print box.height


if __name__ == '__main__':
    main()
