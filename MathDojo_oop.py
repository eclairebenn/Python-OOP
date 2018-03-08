# pylint: disable=print-statement
class MathDojo(object):
    def __init__(self):
        self.sum = 0
    
    def add(self, *args):
        for idx in range(0,len(args)):
            if isinstance(args[idx], list) == True:
                for i in range(0, len(args[idx])):
                    self.sum += args[idx][i]
            else:
                self.sum += args[idx]
        return self

    def subtract(self, *args):
        for idx in range(0,len(args)):
            if isinstance(args[idx], list) == True:
                for i in range(0, len(args[idx])):
                    self.sum -= args[idx][i]
            else:
                self.sum -= args[idx]
        return self

    def result_sum(self):
        print self.sum

#mathexpl = MathDojo()
#mathexpl.add(2, 3, 4, 5, 6, 7).add(2).add(10,10,10).result_sum()

#md = MathDojo()
#md.add(2).add(2, 5).subtract(3,2).result_sum()

ld = MathDojo()
ld.add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result_sum()

