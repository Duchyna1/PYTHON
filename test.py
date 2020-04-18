# 1
file = open('abeceda.txt', 'w')
for i in range(65, 91):
    file.write(chr(i) + '=' + str(i) + '\n')
file.close()

# 2
file = open('abeceda.txt', 'w')
for i in range(65, 91):
    file.write(chr(i) + '=' + str(i) + '\n')
for i in range(97, 123):
    file.write(chr(i) + '=' + str(i) + '\n')
file.close()

# 3
file = open('cisla.txt', 'r')
riadok = file.readline()
while riadok != '':
    print(riadok.strip())
    riadok = file.readline()
file.close()