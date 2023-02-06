import math

#weight of rider + bike, equipment, etc. [[ change this !!! ]]
weight = 68 + 8
#gravity
gravity = 9.80665
#speed of head-wind is set at 0 and not used
pass
#uphill or downhill
grade = 0
# coefficient of rolling resistance
crr = 0.0050
# frontal area * drag coefficient
cd = 0.330
# air density (Rho)
air = 1.225
# 1 / ( 1 - drive_train_loss / 100 )  
l = 1/(1-0.03)


#F_{gravity}
fg = gravity * weight * math.sin(math.atan(grade/100))
#F_{rolling}
fr = gravity * weight * math.cos(math.atan(grade/100)) * crr
#F_{drag}
def fd(vel):
    return 0.5 * cd * air * math.exp(-0.00011856 * 320) * vel * vel

def vel(watts, vel):
    return watts * l / (fg + fr + fd(vel))

def iterVel(watts, guess=20/3.6):
    v = vel(watts, guess)
    while abs(v - guess) >= 0.1/3.6:
        if v - guess > 0:
            guess += 0.05/3.6
        if v - guess < 0:
            guess -= 0.05/3.6
        v = vel(watts, guess)
    return v
