class Cats():
    def __init__(self):
        self.cat_list  = ['bob', 'tigre', 'charlie']
        self.n = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.cat_list) == self.n:
            raise StopIteration
        
        self.n += 1
        return self.cat_list[self.n - 1]

obj = Cats()

for i in obj:
    print (i)