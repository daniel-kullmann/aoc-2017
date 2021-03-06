fh = open("9.txt")
input = fh.readline().strip()
test_input = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
test_input = "{{{}},{},{{}}}"
test_input = "{{<a>},{<a>},{<a>},{<a>}}"
test_input = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
fh.close()


class Item:
    def calculateScore(self, containerScore):
        pass
    def score(self):
        pass
    def groups(self):
        pass
    
    
class Garbage(Item):
    def __init__(self, content):
        self.content = content
    def __repr__(self):
        return "<" + self.content + ">"
    def calculateScore(self, containerScore):
        pass
    def score(self):
        return 0
    def addContent(self, add):
        self.content += add


class Group(Item):
    def __init__(self, items):
        self.items = items
        self._score = 0
        
    def __repr__(self):
        return "{" + ",".join([repr(item) for item in self.items]) + "}"
        
    def calculateScore(self, containerScore):
        self._score = containerScore+1
        for item in self.items:
            item.calculateScore(self._score)

    def score(self):
        return self._score + sum([item.score() for item in self.items])
    

class Machine:
    def next(self, stack, input):
        """Takes the stack of items and input, and 
        returns a changed stack and next state"""
        pass

class InGroup(Machine):
    def next(self, stack, input):
        state = self
        if input == '{':
            #print ">", input, stack
            stack.append(Group([]))
        elif input == '}':
            #print ">", input, stack
            current = stack.pop()
            stack[-1].items.append(current)
            pass
        elif input == ',':
            pass
        elif input == '<':
            stack.append(Garbage(""))
            state = inGarbage
        else:
            raise Exception("input", self, stack, input)
        #print "<", stack
        return(stack, state)

class InGarbage(Machine):
    def next(self, stack, input):
        state = self
        if input == '!':
            stack[-1].addContent(input)
            state = inEscaped
        elif input == '>':
            current = stack.pop()
            stack[-1].items.append(current)
            state = inGroup
        else:
            stack[-1].addContent(input)
        return(stack, state)

class InEscaped(Machine):
    def next(self, stack, input):
        stack[-1].addContent(input)
        state = inGarbage
        return(stack, state)

inGroup = InGroup()
inGarbage = InGarbage()
inEscaped = InEscaped()

state = inGroup

stack = [Group([])]

for c in input:
    (stack, state) = state.next(stack, c)    

result = stack[0].items[0]
result.calculateScore(0)
print result, result.score()
