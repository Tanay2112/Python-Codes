## d = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)**0.5
  ##  return float(format(d, '.2f'))

n = int(input('Enter n :'))
p = []
for i in range(n):
    p.append((int(input('x = ')), int(input('y = '))))
print(p)
min_dis=((p[0][0]-p[1][0])** 2 +(p[0][1]-p[1][1])**2)**0.5
min_points=[]
min_points.append((p[0], p[1]))
for i in range(n):
    for j in range(i+2, n):
        d=((p[i][0]-p[j][0])** 2 +(p[i][1]-p[j][1])**2)**0.5
        if d<min_dis:
            min_dis=((p[i][0]-p[j][0])** 2 +(p[i][1]-p[j][1])**2)**0.5
            min_points=[]
            min_points.append((p[i], p[j]))
            print(min_points)
        elif d==min_dis:
            min_points=[]
            min_points.append((p[i], p[j]))
            print(min_points)
for i in range(len(min_points)):
    print(min_points[i][0], 'and', min_points[i][1])
