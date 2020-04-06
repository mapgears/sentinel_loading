class Point:
    def __init__(self, abs, ord):
        self.point=[]
        self.point.append(abs)
        self.point.append(ord)

    def get_point(self):
        return self.point
    def set_point(self,x,y):
        self.point[0] =x
        self.point[1] =y  
