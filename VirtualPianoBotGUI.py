# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VirtualPianoBotGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PianoKeys import *
from PianoSongs import *
import pyautogui

def clicked1():
     Keys.c1()

def clicked2():
     Keys.c2()

def clicked3():
     Keys.c3()

def clicked4():
     Keys.c4()

def clicked5():
     Keys.c5()

###############################################

def clicked6():
     Keys.d1()

def clicked7():
     Keys.d2()

def clicked8():
     Keys.d3()

def clicked9():
     Keys.d4()

def clicked10():
     Keys.d5()

#################################################

def clicked11():
     Keys.e1()

def clicked12():
     Keys.e2()

def clicked13():
     Keys.e3()

def clicked14():
     Keys.e4()

def clicked15():
     Keys.e5()

###################################################

def clicked16():
     Keys.f1()

def clicked17():
     Keys.f2()

def clicked18():
     Keys.f3()

def clicked19():
     Keys.f4()

def clicked20():
     Keys.f5()

#########################################################

def clicked21():
     Keys.g1()

def clicked22():
     Keys.g2()

def clicked23():
     Keys.g3()

def clicked24():
     Keys.g4()

def clicked25():
     Keys.g5()

#####################################################


def clicked26():
     Keys.a1()

def clicked27():
     Keys.a2()

def clicked28():
     Keys.a3()

def clicked29():
     Keys.a4()

def clicked30():
     Keys.a5()

########################################################

def clicked31():
     Keys.b1()

def clicked32():
     Keys.b2()

def clicked33():
     Keys.b3()

def clicked34():
     Keys.b4()

def clicked35():
     Keys.b5()
     
def clicked36():
     Keys.b6()

#########################################################

def createSongFile(songFileName):
     print("Please name your song file")

     songFileName = input()

     file = open(songFileName + ".txt",  "w+")

     print("Write something")

     userInput = input()

     file.write(userInput)

     file.close()

     file = open(songFileName + ".txt", "r")

     contents = file.read()

     list1 = [contents]

     print(contents)

     file.close()

#def keyCaller(b):
#     print("Test")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 378)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.C1 = QtWidgets.QPushButton(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(50, 180, 31, 141))
        self.C1.setObjectName("C1")
        self.C1.clicked.connect(clicked1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 180, 31, 141))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(clicked2)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 180, 31, 141))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(clicked3)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 180, 31, 141))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(clicked4)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(890, 180, 31, 141))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(clicked5)
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 180, 31, 141))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(clicked6)
        
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(920, 180, 31, 141))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(clicked7)
        
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 180, 31, 141))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(clicked8)
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(710, 180, 31, 141))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(clicked9)
        
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(500, 180, 31, 141))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(clicked10)
        
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(110, 180, 31, 141))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(clicked11)
        
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(950, 180, 31, 141))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(clicked12)
        
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(320, 180, 31, 141))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(clicked13)
        
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(740, 180, 31, 141))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(clicked14)
        
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(530, 180, 31, 141))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(clicked15)
        
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(140, 180, 31, 141))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(clicked16)
        
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(980, 180, 31, 141))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(clicked17)
        
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(350, 180, 31, 141))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(clicked18)
        
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(770, 180, 31, 141))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(clicked19)
        
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(560, 180, 31, 141))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(clicked20)
        
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(170, 180, 31, 141))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.clicked.connect(clicked21)
        
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(1010, 180, 31, 141))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(clicked22)
        
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(380, 180, 31, 141))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(clicked23)
        
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(800, 180, 31, 141))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.clicked.connect(clicked24)
        
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(590, 180, 31, 141))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.clicked.connect(clicked25)
        
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(200, 180, 31, 141))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_26.clicked.connect(clicked26)
        
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(1040, 180, 31, 141))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.clicked.connect(clicked27)
        
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(410, 180, 31, 141))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_28.clicked.connect(clicked28)
        
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(830, 180, 31, 141))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.clicked.connect(clicked29)
        
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(620, 180, 31, 141))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_30.clicked.connect(clicked30)
        
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(230, 180, 31, 141))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_31.clicked.connect(clicked31)
        
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(1070, 180, 31, 141))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_32.clicked.connect(clicked32)
        
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(440, 180, 31, 141))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_33.clicked.connect(clicked33)
        
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(860, 180, 31, 141))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_34.clicked.connect(clicked34)
        
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(650, 180, 31, 141))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_35.clicked.connect(clicked35)
        
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setGeometry(QtCore.QRect(20, 180, 31, 141))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_36.clicked.connect(clicked36)
        
        self.song = QtWidgets.QPushButton(self.centralwidget)
        self.song.setGeometry(QtCore.QRect(420, 50, 201, 23))
        self.song.setObjectName("song")
        self.song.clicked.connect(createSongFile)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 41, 41))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_37.setGeometry(QtCore.QRect(80, 130, 41, 41))
        self.pushButton_37.setObjectName("pushButton_37")
        
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_38.setGeometry(QtCore.QRect(120, 130, 41, 41))
        self.pushButton_38.setObjectName("pushButton_38")
        
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_40.setGeometry(QtCore.QRect(160, 130, 41, 41))
        self.pushButton_40.setObjectName("pushButton_40")
        
        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setGeometry(QtCore.QRect(200, 130, 41, 41))
        self.pushButton_41.setObjectName("pushButton_41")
        
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(290, 130, 41, 41))
        self.pushButton_43.setObjectName("pushButton_43")
        
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(330, 130, 41, 41))
        self.pushButton_44.setObjectName("pushButton_44")
        
        self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_45.setGeometry(QtCore.QRect(250, 130, 41, 41))
        self.pushButton_45.setObjectName("pushButton_45")
        
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_46.setGeometry(QtCore.QRect(410, 130, 41, 41))
        self.pushButton_46.setObjectName("pushButton_46")
        
        self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_47.setGeometry(QtCore.QRect(370, 130, 41, 41))
        self.pushButton_47.setObjectName("pushButton_47")
        
        self.pushButton_50 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_50.setGeometry(QtCore.QRect(500, 130, 41, 41))
        self.pushButton_50.setObjectName("pushButton_50")
        
        self.pushButton_51 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_51.setGeometry(QtCore.QRect(540, 130, 41, 41))
        self.pushButton_51.setObjectName("pushButton_51")
        
        self.pushButton_52 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_52.setGeometry(QtCore.QRect(460, 130, 41, 41))
        self.pushButton_52.setObjectName("pushButton_52")
        
        self.pushButton_53 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_53.setGeometry(QtCore.QRect(620, 130, 41, 41))
        self.pushButton_53.setObjectName("pushButton_53")
        
        self.pushButton_54 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_54.setGeometry(QtCore.QRect(580, 130, 41, 41))
        self.pushButton_54.setObjectName("pushButton_54")
        
        self.pushButton_55 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_55.setGeometry(QtCore.QRect(790, 130, 41, 41))
        self.pushButton_55.setObjectName("pushButton_55")
        
        self.pushButton_56 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_56.setGeometry(QtCore.QRect(710, 130, 41, 41))
        self.pushButton_56.setObjectName("pushButton_56")
        
        self.pushButton_57 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_57.setGeometry(QtCore.QRect(670, 130, 41, 41))
        self.pushButton_57.setObjectName("pushButton_57")
        
        self.pushButton_58 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_58.setGeometry(QtCore.QRect(830, 130, 41, 41))
        self.pushButton_58.setObjectName("pushButton_58")
        
        self.pushButton_59 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_59.setGeometry(QtCore.QRect(750, 130, 41, 41))
        self.pushButton_59.setObjectName("pushButton_59")
        
        self.pushButton_60 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_60.setGeometry(QtCore.QRect(1000, 130, 41, 41))
        self.pushButton_60.setObjectName("pushButton_60")
        
        self.pushButton_61 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_61.setGeometry(QtCore.QRect(920, 130, 41, 41))
        self.pushButton_61.setObjectName("pushButton_61")
        
        self.pushButton_62 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_62.setGeometry(QtCore.QRect(880, 130, 41, 41))
        self.pushButton_62.setObjectName("pushButton_62")
        
        self.pushButton_63 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_63.setGeometry(QtCore.QRect(1040, 130, 41, 41))
        self.pushButton_63.setObjectName("pushButton_63")
        
        self.pushButton_64 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_64.setGeometry(QtCore.QRect(960, 130, 41, 41))
        self.pushButton_64.setObjectName("pushButton_64")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 21))
        self.menubar.setObjectName("menubar")
        self.menuKeyboard = QtWidgets.QMenu(self.menubar)
        self.menuKeyboard.setObjectName("menuKeyboard")
        self.menuPlay_Song = QtWidgets.QMenu(self.menubar)
        self.menuPlay_Song.setObjectName("menuPlay_Song")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuKeyboard.menuAction())
        self.menubar.addAction(self.menuPlay_Song.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.C1.setText(_translate("MainWindow", "C1"))
        self.pushButton_2.setText(_translate("MainWindow", "C2"))
        self.pushButton_3.setText(_translate("MainWindow", "C3"))
        self.pushButton_4.setText(_translate("MainWindow", "C4"))
        self.pushButton_5.setText(_translate("MainWindow", "C5"))
        self.pushButton_6.setText(_translate("MainWindow", "D1"))
        self.pushButton_7.setText(_translate("MainWindow", "D5"))
        self.pushButton_8.setText(_translate("MainWindow", "D2"))
        self.pushButton_9.setText(_translate("MainWindow", "D4"))
        self.pushButton_10.setText(_translate("MainWindow", "D3"))
        self.pushButton_11.setText(_translate("MainWindow", "E1"))
        self.pushButton_12.setText(_translate("MainWindow", "E5"))
        self.pushButton_13.setText(_translate("MainWindow", "E2"))
        self.pushButton_14.setText(_translate("MainWindow", "E4"))
        self.pushButton_15.setText(_translate("MainWindow", "E3"))
        self.pushButton_16.setText(_translate("MainWindow", "F1"))
        self.pushButton_17.setText(_translate("MainWindow", "F5"))
        self.pushButton_18.setText(_translate("MainWindow", "F2"))
        self.pushButton_19.setText(_translate("MainWindow", "F4"))
        self.pushButton_20.setText(_translate("MainWindow", "F3"))
        self.pushButton_21.setText(_translate("MainWindow", "G1"))
        self.pushButton_22.setText(_translate("MainWindow", "G5"))
        self.pushButton_23.setText(_translate("MainWindow", "G2"))
        self.pushButton_24.setText(_translate("MainWindow", "G4"))
        self.pushButton_25.setText(_translate("MainWindow", "G3"))
        self.pushButton_26.setText(_translate("MainWindow", "A1"))
        self.pushButton_27.setText(_translate("MainWindow", "A5"))
        self.pushButton_28.setText(_translate("MainWindow", "A2"))
        self.pushButton_29.setText(_translate("MainWindow", "A4"))
        self.pushButton_30.setText(_translate("MainWindow", "A3"))
        self.pushButton_31.setText(_translate("MainWindow", "B1"))
        self.pushButton_32.setText(_translate("MainWindow", "B5"))
        self.pushButton_33.setText(_translate("MainWindow", "B2"))
        self.pushButton_34.setText(_translate("MainWindow", "B4"))
        self.pushButton_35.setText(_translate("MainWindow", "B3"))
        self.pushButton_36.setText(_translate("MainWindow", "B6"))
        self.song.setText(_translate("MainWindow", "Create new Song File"))
        self.pushButton.setText(_translate("MainWindow", "C#_1"))
        self.pushButton_37.setText(_translate("MainWindow", "D#_1"))
        self.pushButton_38.setText(_translate("MainWindow", "F#_1"))
        self.pushButton_40.setText(_translate("MainWindow", "G#_1"))
        self.pushButton_41.setText(_translate("MainWindow", "A#_1"))
        self.pushButton_43.setText(_translate("MainWindow", "D#_2"))
        self.pushButton_44.setText(_translate("MainWindow", "F#_2"))
        self.pushButton_45.setText(_translate("MainWindow", "C#_2"))
        self.pushButton_46.setText(_translate("MainWindow", "A#_2"))
        self.pushButton_47.setText(_translate("MainWindow", "G#_2"))
        self.pushButton_50.setText(_translate("MainWindow", "D#_3"))
        self.pushButton_51.setText(_translate("MainWindow", "F#_3"))
        self.pushButton_52.setText(_translate("MainWindow", "C#_3"))
        self.pushButton_53.setText(_translate("MainWindow", "A#_3"))
        self.pushButton_54.setText(_translate("MainWindow", "G#_3"))
        self.pushButton_55.setText(_translate("MainWindow", "G#_4"))
        self.pushButton_56.setText(_translate("MainWindow", "D#_4"))
        self.pushButton_57.setText(_translate("MainWindow", "C#_4"))
        self.pushButton_58.setText(_translate("MainWindow", "A#_4"))
        self.pushButton_59.setText(_translate("MainWindow", "F#_4"))
        self.pushButton_60.setText(_translate("MainWindow", "G#_5"))
        self.pushButton_61.setText(_translate("MainWindow", "D#_5"))
        self.pushButton_62.setText(_translate("MainWindow", "C#_5"))
        self.pushButton_63.setText(_translate("MainWindow", "A#_5"))
        self.pushButton_64.setText(_translate("MainWindow", "F#_5"))
        self.menuKeyboard.setTitle(_translate("MainWindow", "Keyboard"))
        self.menuPlay_Song.setTitle(_translate("MainWindow", "Play Song"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
