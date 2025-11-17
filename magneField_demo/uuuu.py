# this program is to demo a charge's motion in a uniform magnetic field
# 很醜的 充滿源碼的版本

import numpy as np
import matplotlib.pyplot as plt

# conatantttt
# 隨便設
# be careful about the type issue
# 因爲 numpy 是他嗎 fortran 湯底啦！
mass = 1.0
charge = 1.0 # 有點撞名了
B0 = 10.0
vx0 = 1.0
dt = 0.01
stepp = 200 # 做幾次運算

# vector
mag_field = np.array([0.0, 0.0, B0]) # init
r = np.array([0.0, 0.0, 0.0]) # 說了就是這樣
velo = np.array([vx0, 0.0, 0.0]) # init

def magForce(q, v, B):
    return q * np.cross(v, B)

'''
# SHAPE OF ARRAYYYY
f = magForce(charge, velo, mag_field)
print('shape of r', np.shape(r))
print('shape of velo', np.shape(velo))
print('shape of force', np.shape(f))

dv = np.array([(f/mass)*dt])
dv = (f/mass)*dt # 超級屁眼，多一個 np.array() 就是多包一層
print('shape of dv', np.shape(dv))
'''

# make figure and axis
'''
太好了不是只有我看不懂 axis和axes
原來是 matlab
你和 numpy 都是小蛇叛徒
'''
figg = plt.figure(figsize=(10,8))
axx = figg.add_subplot(projection='3d') # 從官網超的，要這個才能畫出 3d 的圖辣
axx.set_xlabel('x')
axx.set_ylabel('y')
axx.set_zlabel('z')

# arrows to mark the vectro field
# ref: https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_simple_demo.html#sphx-glr-gallery-images-contours-and-fields-quiver-simple-demo-py
'''
# 這樣是畫一根
axx.quiver(0, 0, 0,  # 箭頭 origin
           0, 0, 1,  # 箭指的方向
           )
# quiver 是箭袋的意思
'''
# 這樣畫一堆
# 我將要推廣寫 num=
qu_x, qu_y, qu_z = np.meshgrid(np.linspace(-1, 1, num=10),
                               np.linspace(-1, 1, num=10),
                               np.linspace(-1, 1, num=5)
                               )
axx.quiver(qu_x, qu_y, qu_z,                         # 插箭頭的點，如果想表示場的話就應該是網格
           mag_field[0], mag_field[1], mag_field[2], # 箭頭的方向，直接很醜的用磁場指定了
           length=0.02, alpha=0.3, lw=1.2,           # 請享用老子精心調製的參數
           color='mediumblue',                       # 每次最期待的就是選顏色環節
           )

'''
# np.meshgrid(), 直翻的話就是 網格網格 （草）
如果
X = [1, 2, 3]
Y = [20, 10]
做成網格的話就是:
(1, 20); (2, 20); (3, 20)
(1, 10); (2, 10); (3, 10)
np.meshgrid() 就是在做這件事情: 把倆 (或三個?) 1d array 組成矩陣，反正就是那樣
他的回傳值有兩個 (因為我是傳入倆 1d array, 所以回傳值是兩個)
分別是 網格化產物（以上六個座標）的 x和y 座標
belike:
U, V = np.meshgrid(X, Y)
>> U = [[1, 2, 3], [1, 2, 3]]
>> V = [[20, 10], [20, 10], [20, 10]]
之類的吧，非常正確的話請看他媽的官方文件
'''

# plot while caculatingggggg
cc = 0
while cc<stepp: # 直接被 vpython 定型了啦
    f = magForce(charge, velo, mag_field)
    dv = (f/mass) * dt
    velo += dv
    dr = velo * dt
    r += dr

    # 直接畫啦劍塚
    axx.scatter(r[0], r[1], r[2], s=2, c='r')

    cc+=1

plt.show()