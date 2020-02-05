S = int(input())
H = S // 3600
S = S % 3600
M = S // 60
S = S % 60
print(f'{H} h. {M} min. {S} s.')