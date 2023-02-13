import geometry as geo

p = geo.Point(3, 4)
q = geo.Point(1, 3)

print(p)
print(q)

# Python allows direct access to instance variables.
print(p.x, p.y)
print(q.x, q.y)

print(geo.Point.origin_x)
print(geo.Point.origin_y)

# In Python, even this is legal!
q.z = 0

# This is also legal, but a really, really bad idea (IMO).
geo.Point.origin_x = 1
geo.Point.origin_y = 1
geo.Point.origin_z = 1

print(geo.Point.origin_x)
print(geo.Point.origin_y)
print(geo.Point.origin_z)

print(p.distance_from_origin())
print(q.distance_from_origin())

print(p.dist_to(q))
print(q.dist_to(p))

# an alternate way to call dist_to
print(geo.Point.dist_to(p, q))
print(geo.Point.dist_to(q, p))

# another form of distance_from_origin()
print(geo.Point(0,0).dist_to(p))

print(geo.mid_point(p, q))
print(geo.mid_point(q, p))

# A glimpse at some Python internals
print(p.__dict__)
print(type(p).__dict__)
