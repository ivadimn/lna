# Form implementation generated from reading ui file 'FlightDemo.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(433, 270)
        Dialog.setStyleSheet("QDialog {\n"
"\n"
"background-color:yellow\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"color:green\n"
"\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_first = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono PS [UKWN]")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.radioButton_first.setFont(font)
        self.radioButton_first.setObjectName("radioButton_first")
        self.verticalLayout.addWidget(self.radioButton_first)
        self.radioButton_buis = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.radioButton_buis.setFont(font)
        self.radioButton_buis.setObjectName("radioButton_buis")
        self.verticalLayout.addWidget(self.radioButton_buis)
        self.radioButton_econom = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.radioButton_econom.setFont(font)
        self.radioButton_econom.setObjectName("radioButton_econom")
        self.verticalLayout.addWidget(self.radioButton_econom)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.result_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(14)
        font.setBold(True)
        self.result_label.setFont(font)
        self.result_label.setStyleSheet("")
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.verticalLayout_2.addWidget(self.result_label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.radioButton_buis.toggled.connect(self.radio_selected)
        self.radioButton_first.toggled.connect(self.radio_selected)
        self.radioButton_econom.toggled.connect(self.radio_selected)


    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.result_label.setText("You have selected: {0}".format(radio_btn.text()))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Flight type:"))
        self.radioButton_first.setText(_translate("Dialog", "First class      $150"))
        self.radioButton_buis.setText(_translate("Dialog", "Bussines class   $125"))
        self.radioButton_econom.setText(_translate("Dialog", "Economy class    $100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
