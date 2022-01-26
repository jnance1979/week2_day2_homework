def sq_footage():
    h = float(input("How many feet wide is the room? "))
    w = float(input("How many feet long is the room? "))
    result = h * w
    return (f'The square footage is {round(result, 2)} feet.')



def circumference():
    import math
    r = float(input("What is the radius of your circle? "))
    result = 2* math.pi * r
    return (f'The circumference is {round(result, 2)}.')
