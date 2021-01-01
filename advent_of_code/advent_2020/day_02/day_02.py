

class Day02(object):

    lines = []
    count = 0

    def __init__(self):
        with open('advent_2020/day_02/day_02.dat') as file:
            self.lines = [line.rstrip() for line in file]
            
    '''
    Returns true if pw conforms to policy; false otherwise
    '''
    def parse_pwd(self, policy_line):
        policy = policy_line.split(':')[0].strip()
        pw = policy_line.split(':')[1].strip()

        # Parse policy part
        minmax, target = policy.split(' ')
        min, max = minmax.split('-')

        return (pw.count(str(target)) <= int(max) and pw.count(str(target)) >= int(min))
    
    def part_01(self):
        for l in self.lines:
            if self.parse_pwd(l):
                self.count+=1
        return self.count



