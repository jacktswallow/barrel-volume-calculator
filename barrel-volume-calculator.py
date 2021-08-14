import csv
import os
import math
import numpy as np
import numexpr as ne
from PyQt5 import QtCore, QtGui, QtWidgets

#class for all barrel attributes
class Barrel:
    def __init__(self, name, height, endRadius, middleRadius, thickness, formula):
        self.name = name
        self.height = height
        self.endRadius = endRadius
        self.middleRadius = middleRadius
        self.thickness = thickness
        self.formula = formula

barrelList = []

#get csv file name
dirName = os.path.dirname(__file__)
fileName = os.path.join(dirName, 'barrels.csv')

#open csv
with open(fileName, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #iterate through csv rows, skipping the first row as it is the table header
    next(reader)
    for row in reader:
        barrel = Barrel(row[0], row[1], row[2], row[3], row[4], row[5])
        barrelList.append(barrel)

def calculate(comboBoxIndex, dip):
    barrel = barrelList[comboBoxIndex]

    #convert attributes to floats to allow for any adjustments
    #if thickness has been given, subtract it from height
    height  = float(barrel.height)
    if barrel.thickness != '-':
        height -= float(barrel.thickness) 

    endRadius = float(barrel.endRadius)
    middleRadius = float(barrel.middleRadius) - dip
    
    #hardcoded equation
    equation = "pi*H*(3*r**2+4*R*r+8*R**2)/15"

    #convert floats back to strings and substitute into equation
    equation = equation.replace("H", str(height))
    equation = equation.replace("r", str(endRadius))
    equation = equation.replace("R", str(middleRadius))

    # print(equation)
    
    #evaluate string supplying a definition for pi
    result = ne.evaluate(equation, local_dict={'pi': math.pi}, global_dict={})

    #convert to litres
    result = result/1000

    print(str(result))
    return result
    


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.barrelSelectionFrame = QtWidgets.QFrame(self.centralwidget)
        self.barrelSelectionFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.barrelSelectionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barrelSelectionFrame.setObjectName("barrelSelectionFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.barrelSelectionFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.barrelSelectionComboBox = QtWidgets.QComboBox(self.barrelSelectionFrame)
        self.barrelSelectionComboBox.setObjectName("barrelSelectionComboBox")
        self.verticalLayout_2.addWidget(self.barrelSelectionComboBox)

        #add barrels to combobox
        for barrel in barrelList:
            self.barrelSelectionComboBox.addItem(barrel.name)

        self.verticalLayout.addWidget(self.barrelSelectionFrame, 0, QtCore.Qt.AlignTop)
        self.inputFrame = QtWidgets.QFrame(self.centralwidget)
        self.inputFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputFrame.setObjectName("inputFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.inputFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.attributeFrame_1 = QtWidgets.QFrame(self.inputFrame)
        self.attributeFrame_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.attributeFrame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.attributeFrame_1.setObjectName("attributeFrame_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.attributeFrame_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.attributeFrame_1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.attributeFrame_1)
        self.lineEdit.setObjectName("lineEdit")

        # get line text
        # dip = self.lineEdit.text
        # print(self.lineEdit.text)

        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_4.addWidget(self.attributeFrame_1)
        # self.attributeFrame_2 = QtWidgets.QFrame(self.inputFrame)
        # self.attributeFrame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.attributeFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.attributeFrame_2.setObjectName("attributeFrame_2")
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.attributeFrame_2)
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.label_2 = QtWidgets.QLabel(self.attributeFrame_2)
        # self.label_2.setObjectName("label_2")
        # self.horizontalLayout_2.addWidget(self.label_2)
        # self.lineEdit_2 = QtWidgets.QLineEdit(self.attributeFrame_2)
        # self.lineEdit_2.setObjectName("lineEdit_2")
        # self.horizontalLayout_2.addWidget(self.lineEdit_2)
        # self.verticalLayout_4.addWidget(self.attributeFrame_2)
        self.verticalLayout.addWidget(self.inputFrame)
        self.calculateFrame = QtWidgets.QFrame(self.centralwidget)
        self.calculateFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.calculateFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calculateFrame.setObjectName("calculateFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.calculateFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.resultFrame = QtWidgets.QFrame(self.calculateFrame)
        self.resultFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.resultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame.setObjectName("resultFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.resultFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.volumeLabel = QtWidgets.QLabel(self.resultFrame)
        self.volumeLabel.setObjectName("volumeLabel")
        self.horizontalLayout_3.addWidget(self.volumeLabel)
        self.volumeResultLabel = QtWidgets.QLabel(self.resultFrame)
        self.volumeResultLabel.setObjectName("volumeResultLabel")
        self.horizontalLayout_3.addWidget(self.volumeResultLabel)
        self.verticalLayout_3.addWidget(self.resultFrame)
        self.calculatePushButton = QtWidgets.QPushButton(self.calculateFrame)
        self.calculatePushButton.setObjectName("calculatePushButton")
        self.verticalLayout_3.addWidget(self.calculatePushButton)

        #connect pushbutton to function
        self.calculatePushButton.clicked.connect(self.calculateClicked)

        self.verticalLayout.addWidget(self.calculateFrame, 0, QtCore.Qt.AlignBottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Barrel Volume Calculator"))
        self.label.setText(_translate("MainWindow", "Dip (cm):"))
        # self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume:"))
        self.volumeResultLabel.setText(_translate("MainWindow", "0.00L"))
        self.calculatePushButton.setText(_translate("MainWindow", "Calculate"))

    def calculateClicked(self):
        lineText = self.lineEdit.text()

        try:
            dip = float(lineText)
            print("Positive float: " + str(dip))
            comboBoxIndex = self.barrelSelectionComboBox.currentIndex()
            result = calculate(comboBoxIndex, dip)
            _translate = QtCore.QCoreApplication.translate
            self.volumeResultLabel.setText(_translate("MainWindow", str(result)+"L"))
        except ValueError:
            print("Enter a positive number")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




