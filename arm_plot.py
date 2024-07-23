import numpy as np
from xarm.wrapper import XArmAPI

arm = XArmAPI('192.168.1.205') #Arm is named arm

arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

pendia = 8 #mm

arm.set_world_offset([-260,0,8,0,0,0]) #accounting for 8 mm thick base arm is mounted to
arm.set_tcp_offset([42.75 + np.sqrt(2)*(pendia/2), 0, 97, 0, 0, 0]) #pen tip position relative to center of mount
arm.set_state(state=0)

# moves down to pen
arm.set_position(x = 0, y = 0, z = 0.5, roll = 180, pitch = 0, yaw = 0, speed = 20, wait = True)

#insert pen here!!
input('Insert the pen and press enter!')


#continue
arm.set_position(z = 10, speed = 5, wait = True)

zdraw = 0
zmove = 5
movespeed = 80
drawspeed = 30

moves = np.genfromtxt('commands.csv', delimiter=',')

positions = np.array([[0,0,zmove,movespeed]])
for move in moves:
    if move[0] == 0:
        positions = np.append(positions,[[move[2],move[1],zmove,movespeed]], axis = 0)
        positions = np.append(positions,[[move[2],move[1],zdraw,drawspeed]], axis = 0)
    elif move[0] == 1:
        positions = np.append(positions,[[move[2],move[1],zdraw,drawspeed]], axis = 0)
    elif move[0] == 2:
        positions = np.append(positions,[[move[2],move[1],zdraw,drawspeed]], axis = 0)
        positions = np.append(positions,[[move[2],move[1],zmove,drawspeed]], axis = 0)
    else:
        print('uh oh')


for coords in positions:
    arm.set_position(*coords[0:3], speed = coords[3], radius = -1, wait=True)