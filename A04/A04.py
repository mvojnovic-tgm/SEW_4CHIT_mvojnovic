class Bruch():

    def __init__(self, *list):
        if len(list) == 1:
            if type(list[0]) == int or type(list[0]) == float:
                if type(list[0]) != int:
                    raise (TypeError)
                self.zaehler = list[0]
                self.nenner = 1
            else:
                self.zaehler = list[0].zaehler
                self.nenner = list[0].nenner
        else:
            self.zaehler = list[0]
            self.nenner = list[1]

        if self.nenner == 0:
            raise(ZeroDivisionError)

        if type(self.nenner) != int:
            raise(TypeError)

        if type(self.zaehler) != int:
            raise(TypeError)


    def __float__(self):
        return self.zaehler/self.nenner

    def __int__(self):
        return int(self.zaehler/self.nenner)

    def __invert__(self):
        n = self.zaehler
        z = self.nenner
        return Bruch(z, n)

    def __str__(self):
        if self.nenner == 1:
            return "(" + str(self.zaehler) + ")"
        if self.zaehler < 0 and self.nenner < 0:
            help_z = self.zaehler * (-1)
            help_n = self.nenner * (-1)
            return "(%s/%s)" % (help_z, help_n)
        return "(%s/%s)" % (self.zaehler, self.nenner)

    def __pow__(self, power):
        return Bruch(self.zaehler ** power , self.nenner ** power)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __abs__(self):
        if  float(Bruch(self.zaehler,self.nenner)) >= 0:
            return self.zaehler/ self.nenner
        else:
            if self.zaehler < 0:
                return Bruch(self.zaehler * (-1), self.nenner)
            if self.nenner < 0:
                return Bruch(self.zaehler, self.nenner * -1)

    def __neg__(self):
        return Bruch(self.zaehler * (-1), self.nenner)

    def _Bruch__makeBruch(self, value):
        if type(value) != int:
            raise(TypeError)
        else:
            self.zaehler = value

    def __ge__(self, other):
        return self.zaehler / self.nenner >= other.zaehler / other.nenner

    def __le__(self, other):
        return self.zaehler / self.nenner <= other.zaehler / other.nenner

    def __lt__(self, other):
        return self.zaehler / self.nenner < other.zaehler / other.nenner

    def __gt__(self, other):
        return self.zaehler / self.nenner > other.zaehler / other.nenner


    def __add__(self, other):
        if type(other) == float:
            raise(TypeError)
        if type(other) == int:
            return self.zaehler/self.nenner + other
        return self.zaehler/self.nenner + other.zaehler/other.nenner

    def __radd__(self, other):
        return self.zaehler/self.nenner + other

    def __iadd__(self, other):
        if type(other) != int and  type(other) != Bruch:
            raise(TypeError)
        if type(other) == int:
            self.zaehler = self.zaehler + other*self.nenner
            return Bruch(self.zaehler, self.nenner)
        self.zaehler = self.zaehler + other.zaehler* self.nenner
        return Bruch(self.zaehler, self.nenner)

    def __sub__(self, other):
        return self.zaehler/self.nenner - other.zaehler/other.nenner

    def __isub__(self, other):
        if type(other) != int and type(other) != Bruch:
            raise(TypeError)
        if type(other) == int:
            self.zaehler = self.zaehler -other*self.nenner
        else:
            self.zaehler = self.zaehler -other.zaehler*self.nenner
        return Bruch(self.zaehler, self.nenner)

    def __rsub__(self, other):
        if type(other) == float:
            raise(TypeError)
        return other - self.zaehler / self.nenner

    def __mul__(self, other):
        if type(other) == float:
            raise(TypeError)
        if type(other) == int:
            self.zaehler = self.zaehler * other
            return Bruch(self.zaehler, self.nenner)
        self.zaehler = self.zaehler * other.zaehler
        self.nenner = self.nenner * other.nenner
        return Bruch(self.zaehler, self.nenner)

    def __imul__(self, other):
        if type(other) != int and type(other) != Bruch:
            raise(TypeError)
        if type(other) == int:
            self.zaehler = self.zaehler * other
            return self.zaehler/self.nenner
        self.zaehler = self.zaehler * other.zaehler
        return self.zaehler/self.nenner

    def __rmul__(self, other):
        return self.zaehler / self.nenner * other

    def __truediv__(self, other):
        if type(other) == float:
            raise(TypeError)
        if type(other) == int:
            help = other
            other = Bruch(help)
        return Bruch((self.zaehler*other.nenner),(self.nenner*other.zaehler))

    def __rtruediv__(self, other):
        if type(other) == float:
            raise(TypeError)
        return other / self.zaehler / self.nenner

    def __itruediv__(self, other):
        if type(other) != int and type(other) != Bruch:
            raise(TypeError)
        if type(other) == int:
            self.nenner = self.nenner*other
            return self.zaehler/self.nenner
        self.nenner = self.nenner * other.zaehler
        return self.zaehler/self.nenner

