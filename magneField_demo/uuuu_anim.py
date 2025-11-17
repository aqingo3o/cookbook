# This program is to demo a charge's motion in a uniform magnetic field
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation

# Conatantttt
mass = 1.0
charge = 1.0 # 點撞名了
B0 = 10.0
vx0 = 1.0
dt = 0.01
stepp = 50 # 做幾次運算

# Vector
mag_field = np.array([0.0, 0.0, B0]) # init
r = np.array([0.0, 0.0, 0.0]) # 說了就是這樣
velo = np.array([vx0, 0.0, 0.0]) # init

def magForce(q, v, B):
    return q * np.cross(v, B)

# Make figure and axis
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

# Arrows to mark the vectro field
# ref: https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_simple_demo.html#sphx-glr-gallery-images-contours-and-fields-quiver-simple-demo-py
qu_x, qu_y, qu_z = np.meshgrid(np.linspace(-1, 1, num=10), # 我將要推廣寫 num=
                               np.linspace(-1, 1, num=10),
                               np.linspace(-1, 1, num=5),
                               )
axx.quiver(qu_x, qu_y, qu_z,                         # 插箭頭的點，如果想表示場的話就應該是網格
           mag_field[0], mag_field[1], mag_field[2], # 箭頭的方向，直接很醜的用磁場指定了
           length=0.02, alpha=0.3, lw=1.2,           # 請享用老子精心調製的參數
           color='mediumblue',                       # 每次最期待的就是選顏色環節
           )

# plot while caculatingggggg
position = []
cc = 0
while cc<stepp: # 直接被 vpython 定型了啦
    f = magForce(charge, velo, mag_field)
    dv = (f/mass) * dt
    velo += dv
    dr = velo * dt
    r += dr
    position.append(r.copy())
    '''
    不知道為麼 r is changing all the time 就不能直接 append?
    屁眼
    '''
    cc+=1



###################################################################################################
# 不知道現在到底在呼叫的是哪個他嗎物件

    
'''
for i in position: # 畫上去的部分
    axx.scatter(i[0], i[1], i[2], s=2, c='r')
'''

anim_plot  =  axx.scatter([], [], []) # 3d 所以這樣了
# 媽的不知道怎麼設啦


print('idk what update is about')
def update_parti(frame):
    anim_plot.set_data(position[0], position[1], position[2])
    print('idk what update is about')
    return anim_plot,

anim = FuncAnimation(fig=figg,
                   func=update_parti,
                   frames=stepp,
                   interval=7)



plt.show()



'''
許願軌跡有劃線出來
許願除了這樣很醜的 += 之外，可不可以有解方程式版本的
雖然說 += 就是數值解的他媽核心
'''