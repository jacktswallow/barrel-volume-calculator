import csv
import os
import math
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
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_4.addWidget(self.attributeFrame_1)
        
        self.errorFrame = QtWidgets.QFrame(self.inputFrame)
        self.errorFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.errorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.errorFrame.setObjectName("errorFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.errorFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.errorLabel = QtWidgets.QLabel(self.errorFrame)
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setWordWrap(True)
        self.verticalLayout_5.addWidget(self.errorLabel)
        self.verticalLayout_4.addWidget(self.errorFrame)

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
        self.volumeLabel.setText(_translate("MainWindow", "Volume:"))
        self.volumeResultLabel.setText(_translate("MainWindow", "0.00L"))
        self.calculatePushButton.setText(_translate("MainWindow", "Calculate"))

    def calculateClicked(self):
        #remove previous error label
        self.errorLabel.setText('')

        #retrieve user input
        lineText = self.lineEdit.text()

        #test input is both numerical and non-negative
        try:
            dip = float(lineText)
            if(dip < 0):
                raise ValueError
        except ValueError:
            #set error label text
            self.errorLabel.setText('<font color="red">Enter non-negative numerical values only.</font>')
        else:
            #retrieve user barrel selection
            comboBoxIndex = self.barrelSelectionComboBox.currentIndex()
            #calculate result, passing user inputs
            result = self.calculate(comboBoxIndex, dip)
            #if result was correctly calculated, set label to result
            if result:
                _translate = QtCore.QCoreApplication.translate
                self.volumeResultLabel.setText(_translate("MainWindow", str(round(result,2))+"L"))

    def calculate(self, comboBoxIndex, dip):
        #set barrel from selected index
        barrel = barrelList[comboBoxIndex]

        #convert attributes to floats to allow for any adjustments
        try:
            try:
                height  = float(barrel.height)
            except ValueError:
                raise ValueError("In the .csv file 'H' must be set to a numerical value for the current barrel.")
            try:
                #if thickness has been given, subtract it from height
                if barrel.thickness != '-':
                    height -= float(barrel.thickness) 
            except ValueError:
                raise ValueError("In the .csv file 'Thickness' must be set to '-' or a numerical value for the current barrel.")
            try:
                endRadius = float(barrel.endRadius)
            except ValueError:
                raise ValueError("In the .csv file 'r' must be set to a numerical value for the current barrel.")
            try:
                middleRadius = float(barrel.middleRadius)
            except ValueError:
                raise ValueError("In the .csv file 'R' must be set to a numerical value for the current barrel.")
        except ValueError as e:
            #display error
            self.errorLabel.setText('<font color="red">%s</font>' %e)
            return
        else:       
            #retrieve formula for selected barrel
            equation = barrel.formula

            #convert floats back to strings and substitute into equation
            equation = equation.replace("H", str(height))
            equation = equation.replace("r", str(endRadius))
            equation = equation.replace("R", str(middleRadius))
            equation = equation.replace("d", str(dip))

            try:
                #evaluate string and give definition for pi
                result = ne.evaluate(equation, local_dict={'pi': math.pi}, global_dict={})
            except KeyError:
                self.errorLabel.setText('<font color="red">Incorrect variable found in formula for the current barrel in the .csv file. Consult the README for formatting help.</font>')
                return
            except TypeError:
                self.errorLabel.setText('<font color="red">Incorrect formatting found in formula for the current barrel in the .csv file. Consult the README for formatting help.</font>')
                return
            else:
                #convert to litres
                result = result/1000

                return result


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())