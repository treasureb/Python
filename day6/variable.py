#注释
def average(*args):
    if args:
        return float(sum(args))/len(args)
    else:
        return 0.0

print average()
print average(1,2)
print average(1,2,3,4)
