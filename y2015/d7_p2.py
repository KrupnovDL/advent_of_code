# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a).
# What new signal is ultimately provided to wire a?


import numpy as np
from input_data import input_data


def get_signal(wire):
    if wire.isdigit():
        return np.uint16(wire)
    if isinstance(wires[wire], list):
        match len(wires[wire]):
            case 1:
                if wires[wire][0].isdigit():
                    signal = np.uint16(wires[wire][0])
                else:
                    signal = np.uint16(get_signal(wires[wire][0]))
            case 2:
                if wires[wire][1].isdigit():
                    signal = ~np.uint16(wires[wire][1])
                else:
                    signal = ~np.uint16(get_signal(wires[wire][1]))
            case 3:
                match wires[wire][1]:
                    case "AND":
                        signal = get_signal(wires[wire][0]) & get_signal(wires[wire][2])
                    case "OR":
                        signal = get_signal(wires[wire][0]) | get_signal(wires[wire][2])
                    case "LSHIFT":
                        signal = get_signal(wires[wire][0]) << get_signal(wires[wire][2])
                    case "RSHIFT":
                        signal = get_signal(wires[wire][0]) >> get_signal(wires[wire][2])
    else:
        return wires[wire]
    wires[wire] = signal
    return signal


def reset_wires():
    for line in input_data:
        line = line.split()
        wires[line.pop()] = line[:-2]


input_data = input_data(2015, 7).splitlines()
wires = {}

reset_wires()
a_signal = get_signal("a")
reset_wires()
wires["b"] = a_signal

print(get_signal("a"))
