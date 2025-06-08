print (max(-1,2,-3)) # 2
print (1 + 6 // 4) # 2
print ('abcde'[-1:7]) # e
print (bool('False')) # True
print ('' in 'abc') # True
print ([1, 3] * 2) # [1, 3, 1, 3]
print ((1, [2], 3)[1]) # [2]
print ([[1, 2], [3, 4, 5]][1][2]) # 5 
print (sorted('abracadabra')[:3]) # ['a', 'a', 'a']
print ({1: 2, 2: 1}[1] + {3: 4, 0: 1}[0]) # 3
print ( {1: 2, 3: 4}.get(2)) # None
# print ({1: {2: {3: 4}}}[{1: 2, 3: 4}[1]]) # Key Error: 2 - Evaluating this expression yields an error
print ([i - 1 for i in [1, 2]]) # [0, 1]
print ([i for i in [0, 1, 2] if i - 1]) # [0, 2]
# a = map (int, '123')
# print (max(a) + min(a)) # ValueError: min() arg is an empty sequence - Evaluating this expression yields an error

a = int(input())
cond = a == 1
if cond == True:
    print(1)
else:
    print('not 1')

class Duck:
    def __init__(self):
        self.sound = 'quack'

print(Duck().sound) # quack
print(str(Duck())) # <__main__.Duck object at 0x1047156d0>

def f21(n):
    if n > 5: return 5
    if n > 3: return 3
    if n > 1: return 1
    return 0
print (f21(2)) # 1

def f22(seq):
    if isinstance(seq, str):
        return seq
    return ''.join([f22(i) for i in seq])
print (f22(['a', ['b', ['c']], [['d']]])) # abcd

def f23(d):
    acc = {}
    for k, v in d.items():
        if v not in acc:
            acc[v] = []
        acc[v].append(k)
    return acc
print (f23({1: 2, 2: 3, 3: 2, 4:2, 5: 4})) # {2: [1, 3, 4], 3: [2], 4: [5]}

f = lambda y: lambda x: x[-y]
ls = [['i', 'am'], ['an', 'SoC'], [], ['student']]
_ = map(f, range(1, 5))
_ = map(lambda f: f(ls), _)
_ = map(' '.join, _)
_ = filter(bool, _)
res = ' '.join(_) 
print(res)

class Entity:
    def reset(self):
        self.uuid = 0

class Named(Entity):
    def reset(self):
        self.name = ''
        super().reset()

class WithEmail(Entity):
    def reset(self):
        self.email = ''
        super().reset()

class User(Named, WithEmail):
    def __init__(self):
        self.name = 'Bob'
        self.email = 'bob@gmail.com'
        self.uuid = 123
    def reset(self):
        super().reset()

bob = User()
bob.reset()
print([bob.uuid, bob.name, bob.email])