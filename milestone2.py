import numpy as np
import math
f =  open("D:\\KLA_Hackathon\\KLA_Hackathon\\Workshop2024\\Milestone2\\Input\\Testcase1.txt",'r') 
lines = f.readlines()
dic = {}
for i in lines:
    ls = i.split(":")
    dic[ls[0]] = ls[1].strip("\n")
print(dic)
dic['WaferDiameter'] = int(dic['WaferDiameter'])
dic['DieSize'] = ( int(dic['DieSize'][0:2]),int(dic['DieSize'][3:]))
dic['DieShiftVector'] = (int(dic['DieShiftVector'][1]),int(dic['DieShiftVector'][3]))
dic['ReferenceDie'] =  (int(dic['ReferenceDie'][1:3]),int(dic['ReferenceDie'][4:6]))    
print(dic)
radius = dic['WaferDiameter']//2
"""
def get_lower_left_corners(n, shift_vector, ref_position, radius, cell_size):
    # Calculate the center of the circle
    a, b = np.add(ref_position, shift_vector)

    # List to store the lower left corners within the circle
    lower_left_corners = []

    # Iterate over the n*n grid
    for i in range(n):
        for j in range(n):
            # Calculate the lower left corner position of the cell
            x_ll, y_ll = i * cell_size, j * cell_size

            # Calculate the distance from (x_ll, y_ll) to the center (a,b)
            distance = np.sqrt((x_ll - a)**2 + (y_ll - b)**2)

            # If the distance is less than or equal to the radius, add (x_ll, y_ll) to the list
            if distance <= radius:
                lower_left_corners.append((x_ll, y_ll))

    return lower_left_corners


print(get_lower_left_corners(300, (15,15), (10,10), radius, 10))

"""


dic_points = {}

def calculate_lower_left_corners(diameter, cell_size, shift_x, shift_y, reference_cell):
    rec_x,rec_y = reference_cell[0],reference_cell[1]
    cent_posi = (diameter//cell_size[0]-1,diameter//cell_size[0]-1)
    for i in range(diameter//cell_size[0]):
        for j in range(diameter//cell_size[0]):
            dic_points[(rec_x-i,rec_y-j)] = ((cent_posi[0]-(i+1)*cell_size[0]),(cent_posi[1]-(j+1)*cell_size[0]))
    
    return dic_points


# Example usage

diameter = dic['WaferDiameter']  # Diameter of the circle
cell_size = dic['DieSize'][0]  # Size of each cell in the grid
shift_x = dic['DieShiftVector'][0]  # Shift in the x-direction
shift_y = dic['DieShiftVector'][1]  # Shift in the y-direction
reference_cell = list(dic['ReferenceDie'])  # Reference cell [i, j]
points = calculate_lower_left_corners(dic['WaferDiameter'],dic['DieSize'],dic['DieShiftVector'][0],dic['DieShiftVector'][0],dic['ReferenceDie'])

#result = calculate_lower_left_corners(diameter, cell_size, shift_x, shift_y, reference_cell)
#print(result)   




print(dic_points.values())
output_filename = 'output11.txt'
with open(output_filename, 'w') as file:
    for point in points:
        v = "("+str(point[0])+","+str(point[1])+") : ("+str(points[point][0])+","+str(points[point][1])+")"
        file.write(v+'\n')
f.close()













