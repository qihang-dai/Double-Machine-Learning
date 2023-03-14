import numpy as np

ABCD= [(2,3), (4,6), (5,1), (10, 12)]

center = [(6,9), (8,4)]

def distance(a, b):
    return round(((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5, 2)


C1 = []
C2 = []
for index, point in enumerate(ABCD):
    label = chr(index + ord('A'))
    print(chr(index + ord('A')), point)
    dis = []
    for index, c in enumerate(center):
        print("\t center", index, distance(point, c))
        dis.append(distance(point, c))
    if dis[0] < dis[1]:
        C1.append(label)
    else:
        C2.append(label)
print("C1", C1)
print("C2", C2)

#upadte center with the mean of the points in C1 and C2
center = [(np.mean([ABCD[ord(c)-ord('A')] for c in C1], axis=0)), (np.mean([ABCD[ord(c)-ord('A')] for c in C2], axis=0))]
for index, c in enumerate(center):
    print("center", index, c)

#for k = 2, do it again
print("-------------- k = 2 ----------------")

C1 = []
C2 = []
for index, point in enumerate(ABCD):
    label = chr(index + ord('A'))
    print(chr(index + ord('A')), point)
    dis = []
    for index, c in enumerate(center):
        print("\t center", index, distance(point, c))
        dis.append(distance(point, c))
    if dis[0] < dis[1]:
        C1.append(label)
    else:
        C2.append(label)
print("C1", C1)
print("C2", C2)
center = [(np.mean([ABCD[ord(c)-ord('A')] for c in C1], axis=0)), (np.mean([ABCD[ord(c)-ord('A')] for c in C2], axis=0))]
for index, c in enumerate(center):
    print("center", index, c)

