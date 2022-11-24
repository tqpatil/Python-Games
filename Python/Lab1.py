# A user defined class to represent Complex numbers
class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # prints the formal object's information
    def __repr__(self):
        return 'Complex(%s, %s)' % (self.real, self.imag)    

    # prints the readable form, used by print()
    def __str__(self):
        return '%s + %si' % (self.real, self.imag)    


# Driver program to test the class
if __name__ == '__main__':
    t = Complex(10, 20)
    print (repr(t))