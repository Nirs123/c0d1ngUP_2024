from PIL import Image

to_check = [(64,38),
(94,49),
(124,65),
(155,52),
(185,60),
(214,68),
(245,54),
(276,45),
(309,53),
(336,47)]

res = []

for i in range(600):
    img = Image.open(f'dents_tooms/tooms_marque_os_{"{:03d}".format(i)}.png')

    pix = img.load()

    tmp = True
    x = 0
    while tmp:
        if pix[to_check[0][0],x] == (255,255,200):
            diff =  to_check[0][1] - x
            tmp = False
        else:
            x += 1

    good = []

    for j in range(len(to_check)):
        r1, g1, b1 = pix[to_check[j][0], to_check[j][1]-diff]
        r2, g2, b2 = pix[to_check[j][0], to_check[j][1]-diff-1]

        if i == 385:
            print(to_check[j][0], to_check[j][1]+diff, r1, g1, b1)
            print(to_check[j][0], to_check[j][1]+diff-1, r2, g2, b2)

        if [r1,g1,b1] == [255,255,200] and [r2,g2,b2] == [0,0,0]:
            good.append(True)
        else:
            good.append(False)

    # print(i, good, diff)

    if good.count(False) == 0:
        res.append(i)

print(sum(res))