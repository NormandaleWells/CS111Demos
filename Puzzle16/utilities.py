
'''
Returns True if the given Point is inside the given Rectangle.

Through the wonders of run-time method binding, we don't need
to import graphics.py here.
'''
def pt_in_rect(pt, rect):
    ll = rect.getP1()
    ur = rect.getP2()
    return ll.getX() <= pt.getX() < ur.getX() and ll.getY() <= pt.getY() < ur.getY()
