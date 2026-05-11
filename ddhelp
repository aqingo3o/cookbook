'''
用來做單位換算的
尤其是距離單位
'''
import numpy as np

print('沼安! Welcome to ddhelp :D')
Dist = float(input("Source's distance in pc >> "))
Dec = abs(float(input("Source's  declination in deg >> ")))
cosine_val = np.cos(np.deg2rad(Dec)) # 仰角太高就會需要修正
print()

while True:
    size = input("The size is? [with unit: arcsec, second, deg] >> ")
    if size == 'q':
        print('good bye ddhelp :)')
        break

    # if not:
    size_num, size_unit = float(size.split()[0]), size.split()[1]
    if size_unit  == 'arcsec':
        angle = np.deg2rad(size_num / 3600)

    elif size_unit == 'second' or size_unit == 'sec': # RA second
        angle = np.deg2rad((size_num * 15 * cosine_val) / 3600)
        # 1 時間秒 = 15 arcsesc, 因為是赤經所以乘上投影修正

    elif size_unit == 'deg':
        angle = np.deg2rad(size_num)

    else:
        print('The unit is not supported :(')
        continue # 跳過接下來的步驟
    
    arcLen = Dist * angle
    print(f'Size is {arcLen:.2f} pc.')
