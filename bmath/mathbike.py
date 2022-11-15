import math

g = 9.80665
w = 72 + 10
crr = 0.0050
air = 1.225

l = 1/(1-0.03)
fg = g * w * math.sin(math.atan(0))
fr = g * w * math.cos(math.atan(0)) * crr
def fd(vel):
    return 0.5 * 0.330 * air * math.exp(-0.00011856 * 320) * vel * vel

def vel(watts, vel):
    return watts * l / (fg + fr + fd(vel))

def iterVel(watts, guess):
    v = vel(watts, guess)
    while abs(v - guess) >= 0.1/3.6:
        if v - guess > 0:
            guess += 0.05/3.6
        if v - guess < 0:
            guess -= 0.05/3.6
        v = vel(watts, guess)
    return v