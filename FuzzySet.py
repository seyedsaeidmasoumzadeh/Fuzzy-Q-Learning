class Trapeziums(object):
    def __init__(self, left, left_top, right_top, right):
        self.left = left
        self.right = right
        self.left_top = left_top
        self.right_top = right_top

    def membership_value(self, input_value):
        if (input_value >= self.left_top) and (input_value <= self.right_top):
            membership_value = 1.0
        elif (input_value <= self.left) or (input_value >= self.right_top):
            membership_value = 0.0
        elif input_value < self.left_top:
            membership_value = (input_value - self.left) / (self.left_top - self.left)
        elif input_value > self.right_top:
            membership_value = (input_value - self.right) / (self.right_top - self.right)
        else:
            membership_value = 0.0
        return membership_value


class Triangles(object):

    def __init__(self, left, top, right):
        self.left = left
        self.right = right
        self.top = top

    def membership_value(self, input_value):
        if input_value == self.top:
            membership_value = 1.0
        elif input_value <= self.left or input_value >= self.right:
            membership_value = 0.0
        elif input_value < self.top:
            membership_value = (input_value - self.left) / (self.top - self.left)
        elif input_value > self.top:
            membership_value = (input_value - self.right) / (self.top - self.right)
        return membership_value





