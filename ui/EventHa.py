# Form implementation generated from reading ui file 'Event.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/python.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 10, 391, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_click = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_click.setFont(font)
        self.btn_click.setObjectName("btn_click")
        self.btn_click.clicked.connect(self.clicke_me)
        self.horizontalLayout.addWidget(self.btn_click)
        self.line_edit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(12)
        font.setBold(True)
        self.line_edit.setFont(font)
        self.line_edit.setObjectName("line_edit")
        self.horizontalLayout.addWidget(self.line_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(389, 91))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"color:red\n"
"\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def clicke_me(self):
        mytext = self.line_edit.text()
        self.label.setText(mytext)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Qt Designer Application"))
        self.btn_click.setText(_translate("Form", "Click me"))
        self.line_edit.setPlaceholderText(_translate("Form", "Please Enter your name..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())