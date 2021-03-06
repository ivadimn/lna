# Form implementation generated from reading ui file 'RadioDemo.ui'
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
        Dialog.resize(350, 326)
        Dialog.setStyleSheet("QLabel {\n"
"color:purple\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_py = QtWidgets.QRadioButton(Dialog)
        self.radioButton_py.setObjectName("radioButton_py")
        self.verticalLayout.addWidget(self.radioButton_py)
        self.radioButton_java = QtWidgets.QRadioButton(Dialog)
        self.radioButton_java.setObjectName("radioButton_java")
        self.verticalLayout.addWidget(self.radioButton_java)
        self.radioButton_js = QtWidgets.QRadioButton(Dialog)
        self.radioButton_js.setObjectName("radioButton_js")
        self.verticalLayout.addWidget(self.radioButton_js)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_card = QtWidgets.QRadioButton(Dialog)
        self.radioButton_card.setObjectName("radioButton_card")
        self.verticalLayout_2.addWidget(self.radioButton_card)
        self.radioButton_paypal = QtWidgets.QRadioButton(Dialog)
        self.radioButton_paypal.setObjectName("radioButton_paypal")
        self.verticalLayout_2.addWidget(self.radioButton_paypal)
        self.radioButton_cash = QtWidgets.QRadioButton(Dialog)
        self.radioButton_cash.setObjectName("radioButton_cash")
        self.verticalLayout_2.addWidget(self.radioButton_cash)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_result = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout_3.addWidget(self.label_result)

        self.radioButton_py.toggled.connect(self.radio_selected)
        self.radioButton_java.toggled.connect(self.radio_selected)
        self.radioButton_js.toggled.connect(self.radio_selected)
        self.radioButton_card.toggled.connect(self.radio_selected)
        self.radioButton_paypal.toggled.connect(self.radio_selected)
        self.radioButton_cash.toggled.connect(self.radio_selected)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def radio_selected(self):
        book_selected = ""
        payment_selected = ""
        if self.radioButton_py.isChecked():
            book_selected = "Python"
        if self.radioButton_java.isChecked():
            book_selected = "Java"
        if self.radioButton_js.isChecked():
            book_selected = "JavaScript"

        if self.radioButton_card.isChecked():
            payment_selected = "Debit / Credit Card"
        if self.radioButton_paypal.isChecked():
            payment_selected = "PayPal"
        if self.radioButton_cash.isChecked():
            payment_selected = "Cash"

        self.label_result.setText("Selected book: {0}, Payment method: {1}".format(book_selected, payment_selected))



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select the Book:"))
        self.radioButton_py.setText(_translate("Dialog", "Python"))
        self.radioButton_java.setText(_translate("Dialog", "Java"))
        self.radioButton_js.setText(_translate("Dialog", "JavaScript"))
        self.label_2.setText(_translate("Dialog", "Select payment method:"))
        self.radioButton_card.setText(_translate("Dialog", "Debit / Credit Card"))
        self.radioButton_paypal.setText(_translate("Dialog", "PayPal"))
        self.radioButton_cash.setText(_translate("Dialog", "Cash"))
        self.label_result.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
