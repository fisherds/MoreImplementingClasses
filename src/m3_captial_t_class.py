"""
A   CapitalT   class and methods that use the Cross class.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """

    """
    run_test_simple_t()
    run_test_set_colors()
    run_test_move_by()
    run_test_clone()


def run_test_simple_t():
    window = rg.RoseWindow(600, 400, 'Test 1 - Simple Ts')
    t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
    t1.attach_to(window)
    t2 = CapitalT(rg.Point(150, 150), 100, 150, 40)
    t2.attach_to(window)
    t3 = CapitalT(rg.Point(450, 150), 10, 15, 4)
    t3.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def run_test_set_colors():
    window = rg.RoseWindow(600, 400, 'Test 2 - Colorful Ts')
    t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
    t1.set_colors('red', 'magenta')
    t1.attach_to(window)
    t2 = CapitalT(rg.Point(150, 150), 100, 150, 40)
    t2.set_colors('green', 'purple')
    t2.attach_to(window)
    t3 = CapitalT(rg.Point(450, 150), 10, 15, 4)
    t3.set_colors('blue', 'gray')
    t3.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def run_test_move_by():
    window = rg.RoseWindow(600, 400, 'Test 3 - Moving T')
    little_red_t = CapitalT(rg.Point(300, 50), 60, 80, 5)
    little_red_t.set_colors('red', 'gray')
    little_red_t.attach_to(window)
    window.render(0.5)
    little_red_t.move_by(0, 100)
    window.render(0.5)
    little_red_t.move_by(0, 100)
    window.render(0.5)
    for k in range(40):
        little_red_t.move_by(5, -2)
        window.render(0.05)
    window.close_on_mouse_click()


def run_test_clone():
    window = rg.RoseWindow(650, 400, 'Test 4 - Cloning Ts')
    first_t = CapitalT(rg.Point(75, 50), 80, 80, 40)
    first_t.set_colors('blue', 'cyan')
    for k in range(6):
        t = first_t.clone()
        if k < 2:
            t.set_colors('white', 'black')
        t.move_by(100 * k, 20 * k)
        t.attach_to(window)
    first_t.move_by(0, 200)
    first_t.attach_to(window)
    window.render()
    window.close_on_mouse_click()


# ----------------------------------------------------------------------
# TODO: 2. Implement a class called   Cross   that has a constructor and
#   two methods, as described below.  Your finished Cross class should
#   cause the code above to display the expected output.
#
# Constructor
#     What comes in:
#        -- self
#        -- a string for the name of the baby
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#        -- Sets instance variables as needed
#        -- Prints 'Hello baby <your baby's name>!'
#
# feed_baby
#     What comes in:
#        -- self
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#        -- Prints 'Thank you for feeding baby <your baby's name>.'
#        -- Modifies instance variables if needed
#
# hour_passes
#     What comes in:
#        -- self
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#      -- If it is the first time this function has been called since Baby was created or fed
# 	       -- Prints 'Baby <your baby's name> is sleeping.'
#      -- If it is the second time this function has been called since baby was created or fed
# 	       -- Prints 'Baby <your baby's name> is awake.  Time for food.'
#      -- If it is the third (or more) time this function has been called since baby was created or fed
# 	       -- Prints 'Baby <your baby's name> is CRYING uncontrollably!  Feed the Baby!'
#
# Notice that the baby is never printed, so you are not required to make
#     a __repr__ method.  Each method call above simply does a print as
#     a side effect.
# ----------------------------------------------------------------------

########################################################################
# The   Baby   class (and its methods) should begins here.
# Here is a reminder for the syntax to create a new class.
#
#      class NameOfClass(object):
#          """ Brief description of what objects of the class 'are'. """
#
########################################################################

class CapitalT(object):
    """ Manages a CapitalT graphics object. """

    def __init__(self, intersection_center, width, height, letter_thickness):
        """
        What comes in:
           -- self
           -- an rg.Point for the intersection center of the CapitalT
              -- This point is the center of the horizontal rectangle
                 and the top center of the vertical rectangle.
           -- a number for the width of the CapitalT
           -- a number for the height of the CapitalT
           -- a number for the thickness of each rectangle (bar thickness)
        What goes out:  Nothing (i.e., None).
        Side effects:
           -- Sets instance variables as needed"""
        horz_c1_x =  intersection_center.x - width / 2
        horz_c1_y =  intersection_center.y - letter_thickness / 2
        horz_c1 = rg.Point(horz_c1_x, horz_c1_y)

        horz_c2_x = intersection_center.x + width / 2
        horz_c2_y =  intersection_center.y + letter_thickness / 2
        horz_c2 = rg.Point(horz_c2_x, horz_c2_y)

        vert_c1_x =  intersection_center.x - letter_thickness / 2
        vert_c1_y =  intersection_center.y - letter_thickness / 2
        vert_c1 = rg.Point(vert_c1_x, vert_c1_y)

        vert_c2_x = intersection_center.x + letter_thickness / 2
        vert_c2_y =  vert_c1_y + height
        vert_c2 = rg.Point(vert_c2_x, vert_c2_y)

        self.horz_rect = rg.Rectangle(horz_c1, horz_c2)
        self.vert_rect = rg.Rectangle(vert_c1, vert_c2)

    def attach_to(self, window):
        self.vert_rect.attach_to(window)
        self.horz_rect.attach_to(window)

    def move_by(self, dx, dy):
        self.horz_rect.move_by(dx, dy)
        self.vert_rect.move_by(dx, dy)

    def clone(self):
        cloned_t = CapitalT(self.horz_rect.get_center(), self.horz_rect.get_width(),
                            self.vert_rect.get_height(), self.vert_rect.get_width())
        cloned_t.set_colors(self.horz_rect.fill_color, self.horz_rect.outline_color)
        return cloned_t

    def set_colors(self, fill_color, outline_color):
        self.horz_rect.outline_color = outline_color
        self.horz_rect.fill_color = fill_color
        self.vert_rect.outline_color = outline_color
        self.vert_rect.fill_color = fill_color


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
