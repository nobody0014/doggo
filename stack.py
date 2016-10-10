class stack(Object):
    def __init__(self):
        self.container = []
    def isEmpty(self):
        return len(self.container)==0
    def push(item,self):
        self.container.append(item)
    def top(self):
        return self.container[len(self.container)-1]
