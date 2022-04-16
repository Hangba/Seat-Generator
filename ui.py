from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 578)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        #MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 771, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SetGeneratorPath = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SetGeneratorPath.setFont(font)
        self.SetGeneratorPath.setObjectName("SetGeneratorPath")
        self.horizontalLayout.addWidget(self.SetGeneratorPath)
        self.GeneratorPath = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.GeneratorPath.setFont(font)
        self.GeneratorPath.setFrame(True)
        self.GeneratorPath.setClearButtonEnabled(False)
        self.GeneratorPath.setObjectName("GeneratorPath")
        self.horizontalLayout.addWidget(self.GeneratorPath)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SetJudgmentPath = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SetJudgmentPath.setFont(font)
        self.SetJudgmentPath.setObjectName("SetJudgmentPath")
        self.horizontalLayout_2.addWidget(self.SetJudgmentPath)
        self.JudgmentPath = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.JudgmentPath.setFont(font)
        self.JudgmentPath.setObjectName("JudgmentPath")
        self.horizontalLayout_2.addWidget(self.JudgmentPath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.SetNames = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SetNames.setFont(font)
        self.SetNames.setObjectName("SetNames")
        self.horizontalLayout_8.addWidget(self.SetNames)
        self.Names = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.Names.setFont(font)
        self.Names.setFrame(True)
        self.Names.setClearButtonEnabled(False)
        self.Names.setObjectName("Names")
        self.horizontalLayout_8.addWidget(self.Names)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SetJsonPath = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SetJsonPath.setFont(font)
        self.SetJsonPath.setObjectName("SetJsonPath")
        self.horizontalLayout_3.addWidget(self.SetJsonPath)
        self.JsonPath = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.JsonPath.setFont(font)
        self.JsonPath.setObjectName("JsonPath")
        self.horizontalLayout_3.addWidget(self.JsonPath)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.SetSavePath = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SetSavePath.setFont(font)
        self.SetSavePath.setObjectName("SetSavePath")
        self.horizontalLayout_17.addWidget(self.SetSavePath)
        self.SavePath = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.SavePath.setFont(font)
        self.SavePath.setText("")
        self.SavePath.setObjectName("SavePath")
        self.horizontalLayout_17.addWidget(self.SavePath)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.SampleNumber = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.SampleNumber.setFont(font)
        self.SampleNumber.setObjectName("SampleNumber")
        self.horizontalLayout_6.addWidget(self.SampleNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.splNumber = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.splNumber.setFont(font)
        self.splNumber.setObjectName("splNumber")
        self.horizontalLayout_5.addWidget(self.splNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.PicWidth = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.PicWidth.setFont(font)
        self.PicWidth.setObjectName("PicWidth")
        self.horizontalLayout_4.addWidget(self.PicWidth)
        self.PicHeight = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.PicHeight.setFont(font)
        self.PicHeight.setObjectName("PicHeight")
        self.horizontalLayout_4.addWidget(self.PicHeight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Generate = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.Generate.setFont(font)
        self.Generate.setObjectName("Generate")
        self.horizontalLayout_7.addWidget(self.Generate)
        self.Progress = QtWidgets.QLCDNumber(self.layoutWidget)
        self.Progress.setMode(QtWidgets.QLCDNumber.Dec)
        self.Progress.setProperty("value", 0.0)
        self.Progress.setObjectName("Progress")
        self.horizontalLayout_7.addWidget(self.Progress)
        self.ProgressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.ProgressBar.setMaximum(100)
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("ProgressBar")
        self.horizontalLayout_7.addWidget(self.ProgressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.InfoList = QtWidgets.QListWidget(self.layoutWidget)
        self.InfoList.setObjectName("InfoList")
        self.verticalLayout_2.addWidget(self.InfoList)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "分座位器"))
        self.SetGeneratorPath.setText(_translate("MainWindow", "设置Generation路径"))
        self.SetJudgmentPath.setText(_translate("MainWindow", "设置Judgment路径"))
        self.SetNames.setText(_translate("MainWindow", "设置名单Json路径"))
        self.SetJsonPath.setText(_translate("MainWindow", "设置前位置Json路径"))
        self.SetSavePath.setText(_translate("MainWindow", "设置保存路径"))
        self.label_2.setText(_translate("MainWindow", "生成样本数"))
        self.label_3.setText(_translate("MainWindow", "每行学生数"))
        self.label_4.setText(_translate("MainWindow", "生成图片宽，高"))
        self.PicWidth.setText(_translate("MainWindow", "1920"))
        self.PicHeight.setText(_translate("MainWindow", "1080"))
        self.Generate.setText(_translate("MainWindow", "创建座位表"))
        self.ProgressBar.setFormat(_translate("MainWindow", "%p%"))