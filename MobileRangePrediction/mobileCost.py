# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mobileCost.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 1000)
        Form.setMaximumSize(QtCore.QSize(1000, 1000))
        Form.setAutoFillBackground(True)
        Form.setStyleSheet("font: 75 11pt \"Comic Sans MS\";\n"
"color: rgb(255, 247, 234);\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 30, 381, 51))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1001, 1001))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/Downloads/pexels-arun-thomas-1156684.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/Downloads/pexels-arun-thomas-1156684.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 150, 171, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(170, 210, 181, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(630, 220, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(120, 350, 191, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(560, 430, 191, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(700, 570, 68, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(620, 150, 161, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(160, 280, 151, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(690, 290, 68, 19))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(540, 350, 211, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(50, 430, 261, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(10, 500, 291, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(510, 500, 261, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(50, 570, 261, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(80, 640, 331, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(540, 640, 321, 31))
        self.label_18.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(260, 720, 68, 19))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(610, 710, 241, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(240, 790, 68, 19))
        self.label_21.setObjectName("label_21")
        self.clockspeed = QtWidgets.QLineEdit(Form)
        self.clockspeed.setGeometry(QtCore.QRect(310, 220, 241, 31))
        self.clockspeed.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.clockspeed.setObjectName("clockspeed")
        self.batterypower = QtWidgets.QLineEdit(Form)
        self.batterypower.setGeometry(QtCore.QRect(310, 150, 241, 31))
        self.batterypower.setStyleSheet("color: rgb(0, 0, 0);")
        self.batterypower.setObjectName("batterypower")
        self.bluetooth = QtWidgets.QLineEdit(Form)
        self.bluetooth.setGeometry(QtCore.QRect(740, 150, 241, 31))
        self.bluetooth.setStyleSheet("color: rgb(0, 0, 0);")
        self.bluetooth.setObjectName("bluetooth")
        self.dualsim = QtWidgets.QLineEdit(Form)
        self.dualsim.setGeometry(QtCore.QRect(740, 220, 241, 31))
        self.dualsim.setStyleSheet("color: rgb(0, 0, 0);")
        self.dualsim.setObjectName("dualsim")
        self.fc = QtWidgets.QLineEdit(Form)
        self.fc.setGeometry(QtCore.QRect(310, 290, 241, 31))
        self.fc.setStyleSheet("color: rgb(0, 0, 0);")
        self.fc.setObjectName("fc")
        self.fourg = QtWidgets.QLineEdit(Form)
        self.fourg.setGeometry(QtCore.QRect(740, 290, 241, 31))
        self.fourg.setStyleSheet("color: rgb(0, 0, 0);")
        self.fourg.setObjectName("fourg")
        self.intmemo = QtWidgets.QLineEdit(Form)
        self.intmemo.setGeometry(QtCore.QRect(310, 360, 221, 31))
        self.intmemo.setStyleSheet("color: rgb(0, 0, 0);")
        self.intmemo.setObjectName("intmemo")
        self.mobdep = QtWidgets.QLineEdit(Form)
        self.mobdep.setGeometry(QtCore.QRect(750, 360, 231, 31))
        self.mobdep.setStyleSheet("color: rgb(0, 0, 0);")
        self.mobdep.setObjectName("mobdep")
        self.wtphone = QtWidgets.QLineEdit(Form)
        self.wtphone.setGeometry(QtCore.QRect(310, 430, 221, 31))
        self.wtphone.setStyleSheet("color: rgb(0, 0, 0);")
        self.wtphone.setObjectName("wtphone")
        self.cores = QtWidgets.QLineEdit(Form)
        self.cores.setGeometry(QtCore.QRect(750, 430, 231, 31))
        self.cores.setStyleSheet("color: rgb(0, 0, 0);")
        self.cores.setObjectName("cores")
        self.pc = QtWidgets.QLineEdit(Form)
        self.pc.setGeometry(QtCore.QRect(310, 500, 191, 31))
        self.pc.setStyleSheet("color: rgb(0, 0, 0);")
        self.pc.setObjectName("pc")
        self.pxheight = QtWidgets.QLineEdit(Form)
        self.pxheight.setGeometry(QtCore.QRect(760, 500, 221, 31))
        self.pxheight.setStyleSheet("color: rgb(0, 0, 0);")
        self.pxheight.setObjectName("pxheight")
        self.pxwidth = QtWidgets.QLineEdit(Form)
        self.pxwidth.setGeometry(QtCore.QRect(300, 570, 221, 31))
        self.pxwidth.setStyleSheet("color: rgb(0, 0, 0);")
        self.pxwidth.setObjectName("pxwidth")
        self.ram = QtWidgets.QLineEdit(Form)
        self.ram.setGeometry(QtCore.QRect(760, 570, 221, 31))
        self.ram.setStyleSheet("color: rgb(0, 0, 0);")
        self.ram.setObjectName("ram")
        self.scheight = QtWidgets.QLineEdit(Form)
        self.scheight.setGeometry(QtCore.QRect(310, 640, 211, 31))
        self.scheight.setStyleSheet("color: rgb(0, 0, 0);")
        self.scheight.setObjectName("scheight")
        self.scwidth = QtWidgets.QLineEdit(Form)
        self.scwidth.setGeometry(QtCore.QRect(760, 640, 221, 31))
        self.scwidth.setStyleSheet("color: rgb(0, 0, 0);")
        self.scwidth.setObjectName("scwidth")
        self.threeg = QtWidgets.QLineEdit(Form)
        self.threeg.setGeometry(QtCore.QRect(310, 710, 231, 31))
        self.threeg.setStyleSheet("color: rgb(0, 0, 0);")
        self.threeg.setObjectName("threeg")
        self.ts = QtWidgets.QLineEdit(Form)
        self.ts.setGeometry(QtCore.QRect(760, 710, 221, 31))
        self.ts.setStyleSheet("color: rgb(0, 0, 0);")
        self.ts.setObjectName("ts")
        self.wifi = QtWidgets.QLineEdit(Form)
        self.wifi.setGeometry(QtCore.QRect(310, 780, 231, 31))
        self.wifi.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifi.setObjectName("wifi")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(510, 860, 201, 34))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(290, 930, 141, 21))
        self.label_22.setObjectName("label_22")
        self.cost = QtWidgets.QLineEdit(Form)
        self.cost.setGeometry(QtCore.QRect(430, 930, 431, 31))
        self.cost.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.cost.setObjectName("cost")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.clockspeed.raise_()
        self.batterypower.raise_()
        self.bluetooth.raise_()
        self.dualsim.raise_()
        self.fc.raise_()
        self.fourg.raise_()
        self.intmemo.raise_()
        self.mobdep.raise_()
        self.wtphone.raise_()
        self.cores.raise_()
        self.pc.raise_()
        self.pxheight.raise_()
        self.pxwidth.raise_()
        self.ram.raise_()
        self.scheight.raise_()
        self.scwidth.raise_()
        self.threeg.raise_()
        self.ts.raise_()
        self.wifi.raise_()
        self.pushButton.raise_()
        self.label_22.raise_()
        self.cost.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Mobile Price Prediction"))
        self.label_3.setText(_translate("Form", "Battery Power:"))
        self.label_4.setText(_translate("Form", "Clock Speed:"))
        self.label_5.setText(_translate("Form", "Dual Sim:"))
        self.label_6.setText(_translate("Form", "Internal Memory:"))
        self.label_7.setText(_translate("Form", "Number of Cores:"))
        self.label_8.setText(_translate("Form", "Ram:"))
        self.label_9.setText(_translate("Form", "Bluetooth:"))
        self.label_10.setText(_translate("Form", "Front Camera:"))
        self.label_11.setText(_translate("Form", "4G:"))
        self.label_12.setText(_translate("Form", "Mobile Depth in cm:"))
        self.label_13.setText(_translate("Form", "Weight of mobile phone:"))
        self.label_14.setText(_translate("Form", "Primary Camera mega pixels:"))
        self.label_15.setText(_translate("Form", "Pixel Resolution Height:"))
        self.label_16.setText(_translate("Form", "Pixel Resolution Width:"))
        self.label_17.setText(_translate("Form", "Screen Height in cm:"))
        self.label_18.setText(_translate("Form", "Screen Width in cm    :"))
        self.label_19.setText(_translate("Form", "3G:"))
        self.label_20.setText(_translate("Form", "Touch Screen:"))
        self.label_21.setText(_translate("Form", "WiFi:"))
        self.pushButton.setText(_translate("Form", "Predict the cost"))
        self.label_22.setText(_translate("Form", "Mobile Cost:"))
import mobile_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
