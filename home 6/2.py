class Road():
    _leight = 0
    _width = 0
    def mass_asp(self, leight, width):
        return (leight*width*25*5)/1000
r = Road()
print(str(r.mass_asp(20,5000)) + " т")