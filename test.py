import math
radii = input('Enter radii to compute volume -> ')
volume = (4/3)*(math.pi*(int(radii)**3))
print(type(volume))
print('The volume is {} cubic units'.format(round(volume, 3)))
print('the valume is '+ str(volume) + ' cubic units')