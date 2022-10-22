import json
import random, time, datetime, math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from threading import Thread
from PyQt5.QtCore import *
from matplotlib.artist import getp

def incircle(center, point, radius):
    # 判断一个点是否在圆中, 返回bool
    # args:
    # center : tuple circle centre position 
    # point : tuple target point position
    # radius : float
    dis = math.sqrt((center[0] - point[0]) ** 2 + (center[1] - point[1]) ** 2)
    if dis <= radius:
        return True
    else:
        return False

def getPosition(seat,student):
    #给定座位列表，学生名，返回坐标
    pos = (-1,-1)
    for i in range(len(seat)):
        for j in seat[i]:
            if student == j:
                pos = (seat[i].index(j),i)
    if pos == (-1,-1):
        raise ValueError
    else:
        return pos
    
def getx(seat,student):
    return getPosition(seat,student)[0]
def gety(seat,student):
    return getPosition(seat,student)[0]

def getDistance(seat,Stu1:str,Stu2:str):
    pos1 = getPosition(seat,Stu1)
    pos2 = getPosition(seat,Stu2)
    dx = pos1[0]-pos2[0]
    dy = pos1[1]-pos2[1]
    return (dx**2+dy**2)**0.5

def maxDistance(seat,Stus):
    #返回stus列表里面的距离的最大值
    lengths = []
    for stu1 in Stus:
        for stu2 in Stus:
            if stu1!=stu2: lengths.append(getDistance(seat,stu1,stu2))
    return max(lengths)

def minDistance(seat,Stus):
    lengths = []
    for stu1 in Stus:
        for stu2 in Stus:
            if stu1!=stu2: lengths.append(getDistance(seat,stu1,stu2))
    return min(lengths)

def integerpoint_in_circle(center, radius):
    # 返回已知圆心和半径的圆中的整数点(排除圆心)
    # args:
    # center : tuple (x,y)
    # radius : float
    xs = center[0] - radius
    ys = center[1] - radius
    xe = center[0] + radius
    ye = center[1] + radius

    point_list = list()
    for x in range(int(xs), int(xe) + 1):
        for y in range(int(ys), int(ye) + 1):
            if (
                incircle(center, (x, y), radius)
                and center != (x, y)
                and x >= 0
                and y >= 0
            ):
                point_list.append((x, y))

    return point_list

def log(output,msg):
    #在窗口列表中记录信息
    output.addItem(msg)


class Seat(QObject):

    signal = pyqtSignal()


    def __init__(self,stu_list,spl):
        super().__init__()
        # stu_list : list 学生名单
        # spl : int 每行学生数

        # initialize seat list
        self.stu_list = stu_list
        self.spl = spl
        

        #完成的座位列表
        self.completed = list()
        #判断条件列表
        self.judgment = list()
        #生成条件列表
        self.generation = list()
        #开始时间
        self.now = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        #是否设置信息输出
        self.ifInfoOutput = False
        #禁止出现人的位置
        self.forbidden = list()
        #已经出现的Generation
        self.showed = list()
        #耗时
        self.timedict=dict()
        #时间提醒阈值
        self.notify = 20000
        #之前的座位
        self.former = []
        #后排系数（排数*系数向上取整，此排包括之后的都算后排）
        self.backward = 0.8

        
    
    def setInfo(self,infoList,progressnumber,progressbar):
        #初始化设置信息输出 输出列表 数字显示 进度条
        self.ifInfoOutput = True
        self.infoList = infoList
        self.progressnumber=progressnumber
        self.progressbar=progressbar

    def initialization(self):
        # 初始化座位列表
        self.seatsize = [ self.spl, int(len(self.stu_list) / self.spl) + 1]
        self.seat = [["" for _ in range(self.spl)] for _ in range(self.seatsize[1])]
        self.name = self.stu_list.copy()
        self.deleted = list()

    def init_factor(self, judgment_path, generation_path):
        #初始化判断条件和生成条件
        #args: judgment_path:str,generation_path:str
        if judgment_path != "":
            try:
                with open(judgment_path, "r", encoding="utf8") as e:
                    for i in e.readlines():
                        
                        if i[0] not in "#\n ":
                            self.judgment.append(i)
            except FileNotFoundError:
                self.infoList.addItem("#Processing 载入Judgment失败！")
        else:
            self.judgment = None
            self.infoList.addItem("#Processing 无Judgment输入")

        if generation_path != "":
            try:
                with open(generation_path, "r", encoding="utf8") as e:
                    for j in e.readlines():
                        if j[0] not in "#\n ":
                            self.generation.append(j)
            except FileNotFoundError:
                self.infoList.addItem("#Processing 载入Generation失败！")
        
        
        else:
            self.generation = None
            self.infoList.addItem("#Processing 无Generation输入")
        
    def init_generation(self,seat,deleted):
        #Generation条件初始化
        if bool(self.generation):
            if "Loading" not in self.showed:  #防止出现太多次提示
                self.infoList.addItem("#Processing 载入Generation中")
                self.showed.append("Loading")
            for g in self.generation:
                l=g.replace("\n","").split(" ")
                try:
                    if l[0] == "g1":
                        if l not in self.showed:
                            self.showed.append(l)
                            self.infoList.addItem("在{}位置生成{}".format(l[2],l[1]))
                        if l[1] == "None":   #禁止出现的位置
                            self.forbidden.append(eval(l[2]))
                            self.generating(" ",eval(l[2]),deleted=deleted)
                        else:
                            self.generating(l[1],eval(l[2]),deleted=deleted)

                    elif l[0]=="g2":

                        if len(l) == 4:    #包含圆心
                            if l not in self.showed:
                                self.showed.append(l)
                                self.infoList.addItem("在圆心为{},半径为{}的圆内生成{}".format(l[3],l[2],l[1]))
                            position = json.loads(l[3].replace("(","[").replace(")","]"))
                            self.generate_by_radius( l[1].split(","), float(l[2]), deleted, position)
                        else:
                            if l not in self.showed:
                                self.showed.append(l)
                                self.infoList.addItem("在圆心随机,半径为{}的圆内生成{}".format(l[2],l[1]))
                            self.generate_by_radius( l[1].split(","), float(l[2]), deleted)

                    elif l[0]=="g3":
                        if l not in self.showed:
                            self.showed.append(l)
                            self.infoList.addItem("在圆心为{},半径为{}的圆内,以{}为中心生成{}".format(l[4],l[3],l[1],l[2]))
                        position = json.loads(l[4].replace("(","[").replace(")","]"))  #把字符(1,2)转为list
                        self.generate_by_radius( l[2].split(","), float(l[3]), deleted , position , l[1])
                    else:
                        self.infoList.addItem("#Generation 操作符输入错误:{}".format(g))
                        raise ValueError
                except IndexError as e:
                    #输入错误导致项溢出
                    self.infoList.addItem("#Generation 输入错误,项溢出:" + str(e.args))

    def init_judgment(self,seat):
        ans = True
        operators = ['<','>','<=','>=','=']
        if bool(self.judgment):
            if "Loading" not in self.showed:  #防止出现太多次提示
                self.infoList.addItem("#Processing 载入Judgment中")
                self.showed.append("Loading")
            for g in self.judgment:
                l=g.replace("\n","").split(" ")
                if l[0]=="distance":
                    #距离关系
                    stu1 = l[1]
                    stu2 = l[2]
                    o = l[3]
                    length = l[4]
                    if o not in operators or stu1 not in self.stu_list or stu2 not in self.stu_list:
                        raise RuntimeError("操作符错误 或 学生姓名输入错误")
                    ans = ans and eval(str(getDistance(self.seat,stu1,stu2))+o+length)

                elif l[0]=="getx":
                    #横坐标关系
                    stu = l[1]
                    o = l[2]
                    x = l[3]
                    if o not in operators or stu not in self.stu_list:
                        raise RuntimeError("操作符错误 或 学生姓名输入错误")
                    ans = ans and eval(str(getx(self.seat,stu))+o+x)
                
                elif l[0]=="gety":
                    #纵坐标关系
                    stu = l[1]
                    o = l[2]
                    y = l[3]
                    if o not in operators or stu not in self.stu_list:
                        raise RuntimeError("操作符错误 或 学生姓名输入错误")
                    ans = ans and eval(str(gety(self.seat,stu))+o+x)
                
                elif l[0]=="getxy":
                    #纵坐标关系
                    stu = l[1]
                    pos = l[2]
                    if stu not in self.stu_list:
                        raise RuntimeError("学生姓名输入错误")
                    ans = ans and eval(str(getPosition(self.seat,stu))+"=="+pos)
                
                elif l[0]=="maxdistance":
                    stus = l[1].split(",")
                    o = l[2]
                    length = l[3]
                    if o not in operators:
                        raise RuntimeError("学生姓名输入错误")
                    ans = ans and eval(str(maxDistance(self.seat,stus))+o+length)
                
                elif l[0]=="mindistance":
                    stus = l[1].split(",")
                    o = l[2]
                    length = l[3]
                    if o not in operators:
                        raise RuntimeError("学生姓名输入错误")
                    ans = ans and eval(str(minDistance(self.seat,stus))+o+length)
                
                else:
                    self.infoList.addItem("#Judgment 操作符输入错误:{}".format(g))
                    raise ValueError
        return ans

    def isFair(self,seat,former):
        #使座位更公平
        if len(former[0])!=len(seat[0]):
            self.infoList.addItem("两次座位每行人数不同！")
            raise RuntimeError

        for stu in self.stu_list:
            #防止坐同一个位置
            if getPosition(seat,stu) == getPosition(former,stu):
                return False
        
        line = len(former)
        new_line = len(seat)
        for stu in self.stu_list:
            #防止有人一直坐后排
            if gety(former,stu)>=int(line*self.backward)+1 and gety(seat,stu)>=int(new_line*self.backward)+1:
                return False
        
        return True

    def generating(self,stuName,position,deleted = None, enforce = False , ifShow = False):
        # Generation , 在一个固定位置生成
        # seat : list = 生成座位
        # stuName : str = 生成的学生名
        # position : tuple = 位置
        if position[0] > self.seatsize[0]-1:
            #横坐标过大
            raise ValueError
        elif position[1] > self.seatsize[1] -1 :
            #添加的行数在现有之外
            for _ in range(position[1] - self.seatsize[1] +1):
                self.seatsize[1]+=1
                self.seat.append(['']*self.spl)


        if enforce and self.seat[position[1]][position[0]] != "":
            
            if ifShow: self.infoList.addItem("#Generating 强制生成{}在{},原位置为：{}".format(stuName, position, self.seat[position[1]][position[0]]))
            self.seat[position[1]][position[0]] = stuName
            deleted += [stuName]
        elif self.seat[position[1]][position[0]] == "":
            if ifShow: self.infoList.addItem("#Generating 生成{}在{}".format(stuName, position))
            self.seat[position[1]][position[0]] = stuName
            deleted += [stuName]
        elif (not enforce) and self.seat[position[1]][position[0]] != "":
            if ifShow: self.infoList.addItem("#Generating 未生成{}在{}：原位置已有{}".format(stuName, position, self.seat[position[1]][position[0]]))
        
    
    def generate_by_radius(self,Student_list:list,radius,deleted,centerPosition=(-1,-1), MainStudent = None):
        # Generation , 以一个圆生成 
        # Student_list: 学生列表
        # radius: 圆半径
        # deleted: 被删除学生的列表
        # centerPosition: 圆心位置（可选）
        size = self.seatsize
        deleted += Student_list
        random.shuffle(Student_list)
        if bool(MainStudent):
            centerStudent = MainStudent
        else:
            centerStudent = Student_list.pop(0)
        if centerPosition == (-1,-1):
            #随机中心点
            centerPosition = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))

        else:
            # BugFixed： centerPosition 为 str
            x,y = centerPosition
            #判断坐标是否合法
            if not (x >= 0 and x <= size[0] - 1 and y >= 0 and y <= size[1] - 1):
                self.infoList.addItem(f"#GenerationG2 坐标错误:({x},{y})")

        if bool(MainStudent):
            self.generating(centerStudent, centerPosition, deleted)
        else:
            self.generating(centerStudent, centerPosition, deleted)

        point_list = integerpoint_in_circle(centerPosition, radius).copy()
        random.shuffle(point_list)
        points = point_list.copy()
        if len(points) < len(Student_list):
            self.infoList.addItem("#GenerationG2 生成半径过小")
        for p in point_list:
            x, y = p
            if not (x >= 0 and x <= size[0] - 1 and y >= 0 and y <= size[1] - 1):
                points.remove(p)

        for stu in range(len(Student_list)):
            if len(points) < len(Student_list):
                return None
            pos = points[stu]
            if self.seat[pos[1]][pos[0]] == "":
                self.generating(Student_list[stu], points[stu], self.deleted)
                point_list.remove(pos)
            else:
                point_list.remove(pos)
                pos = points[0]
                while self.seat[pos[1]][pos[0]] != "":
                    points.remove(pos)
                    pos = points[0]
                    if len(points) == 0:
                        self.infoList.addItem("#GenerationG2 生成半径过小")
                        return None



    def draw(self,size,seat,savePath):
        # 画出座位表
        # size:tuple 图片大小
        # seat:座位
        if savePath == "":
            self.infoList.addItem("#Processing 请输入保存位置！")
            raise RuntimeError
        image = Image.new("RGB", size , (0, 0, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("Deng.ttf", 55)
        image.filter(ImageFilter.BLUR)
        for i in range(self.seatsize[1]):
            for j in range(self.spl):
                #TODO:根据图片大小和spl决定w,h
                w = 30 + 240 * j
                h = 120 + 120 * i
                if i < self.seatsize[1]:
                    draw.text((w, h), seat[i][j], font=font)
                else:
                    try:
                        draw.text((w, h), seat[i][j], font=font)
                    except IndexError:
                        pass

        save_dir = "{}\\{}.jpg".format( savePath, self.completed.index(seat) )
        image.save(save_dir, "jpeg")
        return "已保存图片: {}".format(save_dir)

    def generate(self):
        #尝试生成 成功返回1 否则返回0
        time0 = time.time()
        stu_copy = self.stu_list.copy()
        random.shuffle(stu_copy)
        self.initialization()


        self.init_generation(self.seat,self.deleted)
        #删去已经存在的人
        for d in stu_copy:
            if d in self.deleted:
                stu_copy.remove(d)
        
        #填入空格 
        for s2 in range(len(self.seat)):
            for s in range(self.spl):
                if self.seat[s2][s] == "":
                    try:
                        self.seat[s2][s] = stu_copy.pop(0)
                    except IndexError:
                        #如果人数不足
                        pass
        #如果空格不够填完所有学生
        if len(stu_copy)>0:
            for i in range(0,len(stu_copy),self.spl):
                appendix = stu_copy[:self.spl]
                self.seat.append(stu_copy[:self.spl]+ ['']*(self.spl-len(stu_copy[:self.spl])) )
                self.seatsize[1]+=1
                del stu_copy[:self.spl]

        count = 0
        for i in self.seat:
            for j in i:
                if j in self.stu_list:
                    count+=1
        
        if bool(self.judgment) and not self.init_judgment(self.seat):
            #Judgment判断
            return 0

        if self.formerPath!="":
            #上次座位判断
            try:
                self.former=json.loads(open(self.formerPath,"r",encoding="utf-8").read())
            except UnicodeDecodeError:
                self.infoList.addItem("前座位文件选择错误")
                raise RuntimeError
            
            if not self.isFair(self.seat,self.former):
                return 0
            
        #确认每个人都在
        if count == len(self.stu_list):

            for i in self.forbidden:
                if self.seat[i[1]][i[0]]  != " ":
                    return 0

            #在A1.1.0中将修改生成图片方式为只要生成完就画图
            self.completed.append(self.seat)
            self.draw(self.size,self.completed[-1],self.path)
            open("{}//{}".format(self.path,str(len(self.completed)-1) + ".json"),"w", encoding="UTF8").write(str(self.completed[-1]).replace("'",'"'))
            self.signal.emit()
            self.performance_estimater(time.time()-time0)
            if self.loop_times == len(self.completed):
                self.infoList.addItem("完成！")
                avgTime = self.performance[0]/self.performance[1]
                self.infoList.addItem(f"平均时长{avgTime:.4f}s/张")
            #self.upgrade_saving_info(len(self.completed))

            
            
            return 1
        else:
            return 0

    def generate_loop(self,loop_times):
        # 多次生成
        self.performance = [0,0]
        self.runtime = 0 #防止陷入死循环
        self.x = loop_times
        self.loop_times = loop_times
        self.infoList.addItem("#Processing 正在生成...")
        while self.x>0:
            #self.infoList.addItem("#Processing 正在生成第{}张座位".format(loop_times - x))
            self.x-= self.generate()
            self.runtime+=1
            if self.runtime>=self.notify:
                self.infoList.addItem("#Processing 似乎陷入较长循环，建议修改judgment")
                self.runtime =0

    def upgrade_saving_info(self,times):
        self.progressbar.setValue(times)
        self.progressnumber.display(times)
        
    def performance_estimater(self,interval):
        #评估生成速度
        self.performance[0]+=interval
        self.performance[1]+=1

    def save(self,size,path):
    # 统一保存：生成图片、csv、json文件,保存路径
    # x,y : tuple 图片宽、高
        times = 0
        self.timedict["savingBegin"] = time.time()
        if self.ifInfoOutput:
            self.infoList.addItem("正在保存....")
            self.progressbar.setMaximum(len(self.completed))
            self.progressbar.setValue(0)
            self.progressnumber.display(0)
        for c in self.completed:
            # 以图片保存
            self.draw(size,c,path)
            # 以json保存
            if path == "":
                path = os.getcwd()
            open("{}//{}".format(path,str(self.completed.index(c)) + ".json"),"w", encoding="UTF8").write(str(c))
            times+=1
            if self.ifInfoOutput:
                self.signal.emit()
                #self.upgrade_saving_info(times)
                
        self.timedict["savingEnd"] = time.time()
        self.t = (self.timedict["savingEnd"] - self.timedict["savingBegin"]) / len(self.completed)
        self.infoList.addItem("图片生成平均耗时：{:.4f}秒".format(self.t))
            
