Numbers = [79620, 58052, 119910, 138477, 139102, 78373, 51937, 63751, 100937, 56664, 128939, 115929, 136981, 68215, 90317, 97455, 130858, 94009, 123221, 81390, 61726, 78271, 73354, 103061, 131261, 140510, 120555, 117319, 91154, 96009, 75491, 90245, 141689, 118783, 104601, 121969, 98547, 108924, 117114, 65916, 120037, 66166, 93973, 105777, 63501, 89199, 117551, 126021, 93466, 107901, 82323, 104471, 98794, 57270, 59457, 120558, 128142, 137648, 127375, 103353, 116578, 97950, 110725, 96438, 128425, 75503, 132178, 138363, 67009, 127873, 135747, 108109, 118818, 75396, 92822, 63886, 82973, 116243, 129066, 74185, 145298, 83483, 83417, 54682, 55648, 142206, 121420, 149890, 56561, 107108, 111376, 139885, 147373, 131657, 140634, 79704, 90263, 139892, 103841, 50730]
sum = 0
for a in range(100):
    sum += Numbers[a]//3-2
print(sum)
