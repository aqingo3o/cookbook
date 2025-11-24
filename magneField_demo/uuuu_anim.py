'''
(20251119) This program is used to demo the motion of a charge in magnetic field.
# universe5961@gmail.com
'''

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

# Constants
mass = 1.0
charge = 1.0
B0 = 1.0
vx0 = 1.0
dt = 0.01
stepp = 500 # 做幾次運算。5000要算很久，500很美麗

# Vectors
mag_field = np.array([0.0, 0.0, B0])  # init
r = np.array([0.0, 0.0, 0.0])
velocity = np.array([vx0, 0.0, 0.0])  # init

def magForce(q, v, B):
    return q * np.cross(v, B)

# Caculatingggggg
position = [] # position
for i in range(stepp):
    f = magForce(charge, velocity, mag_field)
    dv = (f/mass) * dt
    velocity += dv
    dr = velocity * dt
    r += dr
    position.append(r.copy()) # because *r* is a mutable object
'''
    list, array, dict 等等都是可變物件, 在 append 可變物件到別的容器的時候要用 copy()
    這樣進去的才是當下的值, 
    否則所有東西會指向同一個物件，即 append 進去的東西都是同一個值 (最後的 r)

    不可變物件就可以直接 append
    像是 theList.append(a), 
    a 是 int, flaot, str... 都是不可變物件
'''

# Make figure and axis
figg = plt.figure(figsize=(10,8))
axx = figg.add_subplot(projection='3d') # 從官網抄的，要這個才能畫出 3d 的圖辣
# 但同時大概還有三種不同的畫出 3d 圖的方式，隨他媽便，能出現就好。
axx.set_title('Charge in a uniform magnetic field')
axx.set_xlabel('x')
axx.set_ylabel('y')
axx.set_zlabel('z')

# Arrows to mark the vectro field
# ref: https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_simple_demo.html#sphx-glr-gallery-images-contours-and-fields-quiver-simple-demo-py
# 這個上下限應該要以資料為基準下去算，改了的話會刪註解
qu_x, qu_y, qu_z = np.meshgrid(np.linspace(-1, 1, num=10), # 我將要推廣寫 num=
                               np.linspace(-1, 1, num=10),
                               np.linspace(-1, 1, num=5),
                               )
axx.quiver(qu_x, qu_y, qu_z,                         # 插箭頭的點，如果想表示場的話就應該是網格
           mag_field[0], mag_field[1], mag_field[2], # 箭頭的方向，直接很醜的用磁場指定了
           length=0.02, alpha=0.3, lw=1.2,           # 請享用老子精心調製的參數
           color='mediumblue',                       # 每次最期待的就是選顏色環節
           )
'''
# plot without animm
for i in position:
    axx.scatter(i[0], i[1], i[2], s=2, c='r')
'''
# Data prepareeee
posi_x, posi_y, posi_z = [], [], [] # 有夠醜
for i in position:
    posi_x.append(i[0])
    posi_y.append(i[1])
    posi_z.append(i[2])

# Animm
# 參考了 Lorentz attractor 的寫法
traj,  = axx.plot([], [], [], lw=0.5, c='b')
parti, = axx.plot([], [], [], c='r', marker='o')

def update(fr): # 一邊說我他媽還不信了一邊失去耐性，frame 是嗎?從今天開始你叫fr
    traj.set_data(posi_x[:fr], posi_y[:fr])
    traj.set_3d_properties(posi_z[:fr])
    parti.set_data(posi_x[fr-1:fr], posi_y[fr-1:fr]) # 點點會從上一個位子消失
    parti.set_3d_properties(posi_z[fr-1:fr])
    #print(fr) # check point 
    return traj, parti,

anim = FuncAnimation(fig=figg, func=update,
                     frames=np.arange(1, stepp), interval=30, blit=True,)

plt.show()