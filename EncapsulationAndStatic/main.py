# Write OOP classes to handle the following scenarios:
# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line

class Point:

    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y

    def __str__(self):
        return f"<{self.x_cord}, {self.y_cord}>"

    # find distance between two point
    def euclidean_distancs(self, other):
        return ((self.x_cord - other.x_cord)**2 + (self.y_cord - other.y_cord)**2)**0.5

    # find distance from origin
    def distance_from_origin(self):
        # return self.euclidean_distancs(Point(0, 0))
        return (self.x_cord**2 + self.y_cord**2)**0.5

class Line:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
    # Format the first term (Ax)
    # If A is 0, we omit it. If A is 1 or -1, we can just show x or -x.
        if self.A == 0:
            first_term = ""
        elif self.A == 1:
            first_term = "x"
        elif self.A == -1:
            first_term = "-x"
        else:
            first_term = f"{self.A}x"

        # Format the second term (By)
        if self.B == 0:
            second_term = ""
        elif self.B > 0:
            # Add a plus sign if it's not the very first term
            sign = " + " if first_term else ""
            coeff = "" if self.B == 1 else self.B
            second_term = f"{sign}{coeff}y"
        else:
            sign = " - " if first_term else "-"
            coeff = "" if self.B == -1 else abs(self.B)
            second_term = f"{sign}{coeff}y"

        # Format the constant term (C)
        if self.C == 0:
            third_term = ""
        elif self.C > 0:
            sign = " + " if (first_term or second_term) else ""
            third_term = f"{sign}{self.C}"
        else:
            sign = " - " if (first_term or second_term) else "-"
            third_term = f"{sign}{abs(self.C)}"

        # Combine everything. If all are 0, just return "0"
        result = f"{first_term}{second_term}{third_term}"
        return f"{result if result else '0'} = 0"


    def is_on_line(line, point):
        LHS = (line.A * point.x_cord) + (line.B * point.y_cord) + line.C
        RHS = 0
        if LHS == RHS:
            return "Given point lies on the line."
        else:
            return "Given point dosen't lies on line."

    def shortest_distance(line, point):
        return abs(line.A * point.x_cord + line.B * point.y_cord + line.C)/(line.A ** 2 + line.B ** 2)**0.5




# p1 = Point(0, 0)
# p2 = Point(1, 1)

# # result = p1.euclidean_distancs(p2)
# result = p2.distance_from_origin()
# print(result)

l1 = Line(1, 1, -2)
p1 = Point(1, 10)
# print(p1)
# print(l1)
# result = l1.is_on_line(p1)
result = l1.shortest_distance(p1)
print(result)
