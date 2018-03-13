fh = open("9.txt")
input = fh.readline().strip()
input = "{{{}}}"
test_input = "{{<a>},{<a>},{<a>},{<a>}}"
test_input = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
fh.close()

class Item:
    def score(self):
        pass

class Garbage(Item):
    def __init__(self, content):
        self.content = content
    def __repr__(self):
        return "<" + self.content + ">"
    def score(self):
        return 1
    
class Group(Item):
    def __init__(self, items):
        self.items = items
        
    def __repr__(self):
        return "{" + ",".join([repr(item) for item in self.items]) + "}"
        
    def score(self):
        return 1 + sum([item.score for item in self.items])
    

class Machine:
    def next(self, stack, current, input):
        """Takes the stack of items, current item, and input, and 
        returns a changed stack, current item and next state"""
        pass

class InGroup(Machine):
    def next(self, stack, current, input):
        state = self
        if input == '{':
            print ">", input, stack, current
            stack.append(current)
            current = Group([])
        elif input == '}':
            print ">", input, stack, current
            stack[-1].items.append(current)
            pass
        elif input == '<':
            stack.append(current)
            current = []
            state = inGarbage
        else:
            raise Exception("input", self, stack, current, input)
        print "<", stack, current
        return(stack, current, state)

class InGarbage(Machine):
    def next(self, stack, current, input):
        pass    

class InEscaped(Machine):
    def next(self, stack, current, input):
        pass    

inGroup = InGroup()
inGarbage = InGarbage()
inEscaped = InEscaped()

state = inGroup

stack = []
current = Group([])

for c in input:
    (stack, current, state) = state.next(stack, current, c)    

print stack[0]