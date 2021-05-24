# 作者：宁方笑
# 开发时间：2021/5/3 21:32
def robotSim(commands, obstacles):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    x=y=di=0
    obstacleSet=set(map(tuple,obstacles))   #map函数，对obstacles里的每一个对象进行元组转化
    ans=0
    for cmd in commands:
        if cmd==-2:
            di=(di-1)%4
        elif cmd==-1:
            di=(di+1)%4
        else:
            for _ in range(cmd):
                if (x+dx[di],y+dy[di]) not in obstacleSet:
                    x+=dx[di]
                    y+=dy[di]
                    ans=max(ans,x**2+y**2)
    return ans

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
print(robotSim(commands,obstacles))