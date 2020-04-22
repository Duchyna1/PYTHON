# 1
import tkinter

canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

file = open('spokojnost.txt', 'r')
ano = 0
nie = 0
riadok = file.readline()
while riadok != '':
    if riadok.strip() == 'ano':
        ano = ano + 1
    if riadok.strip() == 'nie':
        nie = nie + 1
    riadok = file.readline()
dokopy = ano + nie
percentoAno = ano / dokopy * 100
percentoNie = nie / dokopy * 100
print('Pocet hlasujucic: ' + str(dokopy))
print('Percento ano: ' + str(percentoAno) + '%')
print('Percento nie: ' + str(percentoNie) + '%')

canvas.create_text(150, 450, text='áno')
canvas.create_text(350, 450, text='nie')
canvas.create_rectangle(100, 400-ano*2, 200, 400, fill='red')
canvas.create_rectangle(300, 400-nie*2, 400, 400, fill='blue')

canvas.mainloop()

# # 2
# file = open('kody.txt', 'w')
# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             file.write(str(x) + str(y) + str(z) + '\n')