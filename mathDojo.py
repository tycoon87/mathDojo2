class Math(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    self.result += j
            else:
                self.result += i
        print self.result
        return self
    def subtract(self,*args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    self.result -= j
            else:
                self.result -= i
        print self.result
        return self
equation1 = Math()
equation1.add(2, 5).subtract(2,3)