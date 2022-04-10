from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog
import ui,sys,os,functions,json

class mainwindow(QWidget,ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('分座位器 By:Hangba NNSZ')

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
        filePath,fileType = QFileDialog.getOpenFileName(self, "选取Generator文件", os.getcwd(), "All Files(*.*);;Text Files(*.txt)")
        self.GeneratorPath.setText(filePath)
    
    def read_judgment_path(self):
        filePath,fileType = QFileDialog.getOpenFileName(self, "选取Judgment文件", os.getcwd(), "All Files(*.*);;Text Files(*.txt)")
        self.JudgmentPath.setText(filePath)

    def read_Json_path(self):
        filePath,fileType = QFileDialog.getOpenFileName(self, "选择上次座位文件", os.getcwd(), "All Files(*.*);;Json Files(*.json)")
        self.JsonPath.setText(filePath)

    def read_Names_path(self):
        filePath,fileType = QFileDialog.getOpenFileName(self, "选择名单文件", os.getcwd(), "All Files(*.*);;Text Files(*.json)")
        self.Names.setText(filePath)
    
    def read_save_path(self):
        path= QFileDialog.getExistingDirectory(self, "选择保存路径", os.getcwd())
        self.SavePath.setText(path)

    def load_seat(self):

        self.GeneratorPath.setText("F:/编程/分座位器/UI.Ver/NewGeneration.txt")
        self.Names.setText("F:/编程/分座位器/UI.Ver/2118name.json")
        self.SavePath.setText("F:/编程/分座位器/Test")
        self.SampleNumber.setText("8")
        self.splNumber.setText("8")

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
        except ValueError:
            #spl数据错误
            self.seats = functions.Seat( [] , 0)
            self.seats.setInfo(self.InfoList,self.Progress,self.ProgressBar)
            self.InfoList.addItem("载入失败：每行学生数输入错误")
        
        if isLoadingSuccessful:
            #载入条件
            self.seats.init_factor(self.JudgmentPath.text(),self.GeneratorPath.text())
            if True: #try:
                if int(self.SampleNumber.text())<=0:
                    raise ValueError
                self.seats.generate_loop(int(self.SampleNumber.text()))
                
            else: #except ValueError as e:
                self.InfoList.addItem("生成失败,样本数输入错误 : "+str(e))
            #self.seats.save(self.getsize(),self.SavePath.text())
            
            """
            self.seats.completed.append( eval(open("F:\\编程\\分座位器\\2022-04-05-13-47-24\\@0.json","r",encoding="UTF8").read()) )
            self.seats.completed.append( eval(open("F:\\编程\\分座位器\\2022-04-05-13-47-24\\@1.json","r",encoding="UTF8").read()) )
            self.seats.completed.append( eval(open("F:\\编程\\分座位器\\2022-04-05-13-47-24\\@2.json","r",encoding="UTF8").read()) )
            self.seats.initialization()
            
            """

app=QApplication(sys.argv)
w=mainwindow()
w.show()
sys.exit(app.exec_())
