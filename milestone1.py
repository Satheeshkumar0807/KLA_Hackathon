import numpy as np
f =  open("D:\\KLA_Hackathon\\KLA_Hackathon\\Workshop2024\\Milestone1\\Input\\Testcase1.txt",'r') 
lines = f.readlines()
dic = {}
for i in lines:
    kst = i.split(":")
    dic[kst[0]] = int(kst[1])
print(dic)
radius = dic['WaferDiameter']//2

def generate_points(n, k,radius):
    
    theta = np.radians(k)

    radii = np.linspace(-radius,radius, n)

    x = radii * np.cos(theta)  # List of all points of x-coordinate
    
    y = radii * np.sin(theta)  # List of all points of y-coordinate
 
    return x, y


points = generate_points(dic['NumberOfPoints'],dic['Angle'], dic['WaferDiameter']//2)
x = list(points[0])
y = list(points[1])
list_points=[]
for i in range(len(x)):
    list_points.append((x[i],y[i]))
print(list_points)

with open('Output1.txt','w') as f:
    for i in list_points:
        s = "("+str(i[0])+","+str(i[1])+")"
        f.write(s+"\n")


