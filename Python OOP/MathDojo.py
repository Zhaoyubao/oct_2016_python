class MathDojo1(object):
    def __init__(self):
        self.result = 0
    def add(self, arg1, *args):
        self.result += arg1 + sum(args)
        return self
    def subtract(self, arg1, *args):
        self.result -= arg1 + sum(args)
        return self

md = MathDojo1()
print "Result:",md.add(2).add(2,5).subtract(3,2).result

class MathDojo2(object):
    def __init__(self):
        self.result = 0
    def add(self, arg1, *args):
        if isinstance(arg1, int):
            self.result += arg1
        else:
            self.result += sum(arg1)
        if args:
            for arg in args:
                if isinstance(arg, int):
                    self.result += arg
                else:
                    self.result += sum(arg)
        return self
    def subtract(self, arg1, *args):
        if isinstance(arg1, int):
            self.result -= arg1
        else:
            self.result -= sum(arg1)
        if args:
            for arg in args:
                if isinstance(arg, int):
                    self.result -= arg
                else:
                    self.result -= sum(arg)
        return self
md = MathDojo2()
print "Result:",md.add([1],3,(4)).add([3, 5, 7, 8], (2, 4.3, 1.25)).subtract(2, (2,3), [1.1, 2.3]).result
