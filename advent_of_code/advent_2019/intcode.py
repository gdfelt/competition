

class Intcode:

    memory = []
    pointer = 0 # Instruction currently being processed

    def __init__(self, memory, param_one, param_two):
        self.memory = memory
        self.memory[1] = param_one
        self.memory[2] = param_two


    def process(self):

        while(True):
            if self.memory[self.pointer] == 1:
                self.add()
            elif self.memory[self.pointer] == 2:
                self.multiply()
            elif self.memory[self.pointer] == 99:
                return self.memory[0]
            else:
                print('bad intcode: {}', self.memory[self.pointer])
                return -1


    def reset(self, new_memory, param_one, param_two):
        self.memory = new_memory
        self.memory[1] = param_one
        self.memory[2] = param_two
        self.pointer = 0


    def add(self):
        # Add
        self.memory[self.memory[self.pointer + 3]] = self.memory[self.memory[self.pointer + 1]] + self.memory[self.memory[self.pointer + 2]]
        self.pointer += 4


    def multiply(self):
        # multiply
        self.memory[self.memory[self.pointer + 3]] = self.memory[self.memory[self.pointer + 1]] * self.memory[self.memory[self.pointer + 2]]
        self.pointer += 4


