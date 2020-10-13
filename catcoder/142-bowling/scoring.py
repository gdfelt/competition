#!/usr/bin/env python

def calc_score(throws):
    num_rounds, pins = throws.split(':')
    num_rounds = int(num_rounds)
    pins = pins.split(',')
    pins[:] = list(map(int, pins))
    scores = []

    # Calculate scores
    for x in range(num_rounds):
        if pins[2 * x] == 10:
            pins.insert(2 * x + 1, 0)

        scores.append(pins[2 * x] + pins[2 * x + 1])
        if x != 0:
            scores[x] += scores[x-1]

        # Check for strikes
        if pins[2 * x] == 10:
            scores[x] += pins[2 * x + 2] + pins[2 * x + 3]
            
        # Check for spares
        elif (pins[2 * x] + pins[2 * x + 1]) == 10:
            scores[x] += pins[2 * x + 2]
                    
    return str(scores).strip('[]').replace(" ", "")
