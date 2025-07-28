class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    def __add__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + self.inches
        total_height_inches = height_A_inches + height_B_inches
        output_feet = total_height_inches // 12
        output_inches = total_height_inches - (output_feet * 12)
        return Height(output_feet, output_inches)

    def __sub__(self, other):
        height_C_inches = self.feet * 12 + self.inches
        height_D_inches = other.feet * 12 + other.inches
        subtracted_height_inches = height_C_inches - height_D_inches
        subtracted_feet = subtracted_height_inches // 12
        subtractet_inches = subtracted_height_inches - (subtracted_feet * 12)
        return Height(subtracted_feet, subtractet_inches)

    # try greater than >
    # try greater than or equal >=
    # try not equal to !=

    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B

    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B

    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B


# Test
print(Height(4, 6) > Height(4, 5))
print(Height(4, 5) >= Height(4, 5))
print(Height(5, 9) != Height(5, 10))
