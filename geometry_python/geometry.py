from geometry_python.geom2d import point


l = list(map(lambda i: point.Point(i, i*i), range(-5, 6)))

l2 = list(filter(lambda p: p.x % 2 == 0, l))

print(l)
print(l2)