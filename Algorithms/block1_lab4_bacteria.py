data = list(int(map(int, input().split())))
a = data[0] 
b = data[1] 
c = data[2]
d = data[3] 
k = data[4]

bacteria_number = 0
current_day = 0

while current_day < k:
    current_day += 1
    bacteria_number = a * b
    bacteria_number -= c
    if bacteria_number <= 0:
        print(0)
        exit()

if bacteria_number <= d:
    print(bacteria_number)
else:
    print(d)