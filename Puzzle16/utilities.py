
def pt_in_rect(pt, rect):
    ll = rect.getP1()
    ur = rect.getP2()
    return ll.getX() <= pt.getX() < ur.getX() and ll.getY() <= pt.getY() < ur.getY()
