from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog
import ui,sys,os,functions,json
from threading import Thread
from PyQt5.QtCore import *

class CustomThread():

    def __init__(self):
        pass

    def run(self, function, args):
        self.thread1 = Thread(target= function,args = args, daemon=True)
        self.thread1.start()


class mainwindow(QWidget,ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Seat Generator By Hangba NNSZ')

        #绑定函数
        self.SetGeneratorPath.clicked.connect(self.read_generator_path)
        self.SetJudgmentPath.clicked.connect(self.read_judgment_path)
        self.SetNames.clicked.connect(self.read_Names_path)
        self.SetJsonPath.clicked.connect(self.read_Json_path)
        self.SetSavePath.clicked.connect(self.read_save_path)
        self.Generate.clicked.connect(self.load_seat)
        

    def getsize(self):
        width = self.PicWidth.text()
        height = self.PicHeight.text()
        return ( int(width), int(height))

    def read_generator_path(self):
        filePath,fileType = QFileDialog.getOpenFileName(self, "选取Generation文件", os.getcwd(), "All Files(*.*);;Text Files(*.txt)")
        self.GeneratorPath.setText(filePath)
    
    def read_judgment_path(self):
        filePath,fileType = QFileDialog.getOpenFileName(self, "选取Judgment文件", os.getcwd(), "All Files(*.*);;Text Files(*.txt)")
        self.JudgmentPath.setText(filePath)

    def read_Json_path(self):
        filePath,fileType = QFileDialog.getOpenFileName(self, "选择上次座位文件", os.getcwd(), "All Files(*.*);;Json Files(*.json)")
        self.JsonPath.setText(filePath)

    def read_Names_path(self):
        filePath,fileType = QFileDialog.getOpenFileName(self, "选择名单文件", os.getcwd(), "All Files(*.*);;Json Files(*.json)")
        self.Names.setText(filePath)
    
    def read_save_path(self):
        path= QFileDialog.getExistingDirectory(self, "选择保存路径", os.getcwd())
        self.SavePath.setText(path)

    def updateInfo(self):
        self.ProgressBar.setValue(len(self.seats.completed))
        self.Progress.display(len(self.seats.completed))

    def load_seat(self):

        #多线程准备
        self.thread = CustomThread()
        #载入名单
        isLoadingSuccessful = False #是否载入成功
        try:
            with open(self.Names.text(),"r",encoding="UTF8") as e:
                name = json.loads(e.read())
                self.seats = functions.Seat( name , int( self.splNumber.text() ))
                self.seats.setInfo(self.InfoList,self.Progress,self.ProgressBar)
            self.InfoList.addItem("载入Seat成功！")
            isLoadingSuccessful = True
        except FileNotFoundError:
            #名单文件错误
            self.seats = functions.Seat( [] , 0)
            self.seats.setInfo(self.InfoList,self.Progress,self.ProgressBar)
            self.InfoList.addItem("载入失败：名单文件不存在")
        except ValueError as e:
            #spl数据错误
            self.seats = functions.Seat( [] , 0)
            self.seats.setInfo(self.InfoList,self.Progress,self.ProgressBar)
            self.InfoList.addItem("载入失败：每行学生数输入错误 : "+str(e))
        
        if isLoadingSuccessful:
            #载入条件
            self.seats.init_factor(self.JudgmentPath.text(),self.GeneratorPath.text())
            try:
                if int(self.SampleNumber.text())<=0:
                    raise ValueError
                #传递绘图用参数
                self.seats.size = self.getsize()
                self.seats.path = self.SavePath.text()
                self.seats.formerPath = self.JsonPath.text()
                self.ProgressBar.setMaximum(int(self.SampleNumber.text()))
                self.thread = Thread(target=self.seats.generate_loop,args=[int(self.SampleNumber.text())],daemon=True)
                self.seats.signal.connect(self.updateInfo)
                self.thread.start()
                
                
            except ValueError as e:
                self.InfoList.addItem("生成失败,样本数输入错误 : "+str(e))
            

app=QApplication(sys.argv)
w=mainwindow()
w.show()
sys.exit(app.exec_())
