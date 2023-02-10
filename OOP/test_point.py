import geometry as geo

p = geo.Point(3, 4)
q = geo.Point(1, 3)

# In Python, this is legal!
q.z = 0

print(p)
print(q)

print(p.distance_from_origin())
print(q.distance_from_origin())

print(p.dist_to(q))
print(q.dist_to(p))

print(p.mid_point(q))
print(q.mid_point(p))
