#New concept: range(start, stop, step)
#Step: -1 --> go backward each time
#Range excludes stop value. Meaning range(2,11) will start at 2 but stop at 10.

def reverse_string(val):
    new_str = ""

    for i in range(len(val)-1, -1, -1):
        new_str += val[i]

    return new_str

print(reverse_string("hello"))
