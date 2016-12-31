__author__ = 'Fan Zhang'

f = open("input.txt", "r")
fout = open("output.txt", "w")

s = f.readline().split()
dict = {}

for word in s:
    if word not in dict.keys():
        dict[word] = 1
    else:
        dict[word] += 1

for key, value in dict.items():
    fout.write("{0} {1}\n".format(key, value))

f.close()
fout.close()
