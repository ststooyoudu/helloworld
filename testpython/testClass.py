class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def run(self):
        print(f'{self.name} is runing')

    def printColor(self):
        print(f'it"s color {self.color}')

mydog = Dog('cat', 'yellow')
print(mydog.name)
mydog.run()
