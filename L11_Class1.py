
class TemperatureRange:
    def __init__(self):
        print('__init__ method has been called.')
              
r = TemperatureRange()

class TemperatureRange:
    def __init__(self):
        self.low = self.high = 0
    def print(self):
        print('[{}, {}]'.format(self.low, self.high))
    def difference(self):
        return self.high - self.low
temperature_range = TemperatureRange()
temperature_range.low = 15
temperature_range.high = 21
temperature_range.print()
print('Diff:', temperature_range.difference())

class TemperatureRange:
    def __init__(self):
        self.low=0
        self.high=10
    def __init__(self):
        print('__init__ method has been called.')
    
    def difference(self):
        return self.high-self.low
    
    def print(self):
        print('[{}, {}]'.format(self.low, self.high))
t1=TemperatureRange()
t1.low =15
t1.high=21
t1.print()
print('Diff:', temperature_range.difference())

