def dayup(dt):
    day = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            day *= (1+dt)
        else:
            day *= 0.99
    return day


dt = 0.01
while dayup(dt) < 37.5:
    dt += 0.002
print("{:.3f}".format(dt))
