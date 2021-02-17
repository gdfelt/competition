class Day08(object):
    class Instruction(object):
        def __init__(self, inst, value):
            self.inst = inst
            self.value = int(value)
            self.visited = False

        def __str__(self):
            return str(self.inst) + " " + str(self.value) + " " + str(self.visited)

        def set_visited(self):
            self.visited = True

    def __init__(self):
        self.instruction_set = []
        with open("advent_2020/day_08/day_08.dat") as file:
            for line in file:
                inst, value = line.rstrip().split(" ")
                self.instruction_set.append(self.Instruction(inst, value))

    def part_01(self):
        inst_ptr = 0
        accum = 0
        while True:
            current = self.instruction_set[inst_ptr]

            if current.visited == True:
                break
            else:
                self.instruction_set[inst_ptr].visited = True

            if current.inst == "acc":
                accum += current.value
                inst_ptr += 1
            elif current.inst == "nop":
                inst_ptr += 1
            elif current.inst == "jmp":
                inst_ptr += current.value

        # for i in self.instruction_set:
        #     print(i)

        return accum

    def part_02(self):
        return 0
