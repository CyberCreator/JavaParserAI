# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waiting.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 146)
        Dialog.setStyleSheet("#main_frame {\n"
"    border-radius: 15px;\n"
"    background-color: rgba(117, 190, 218, 0.5);\n"
"}\n"
"#frame_label_wait {\n"
"    border-radius: 10px;\n"
"    background-color: rgba(0, 0, 0, 0.6);\n"
"}\n"
"#label_wait {\n"
"    color: white;\n"
"}\n"
"#graphicsView{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"#pushButton{\n"
"    background-color: transparent;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(Dialog)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.main_frame)
        self.pushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.graphicsView = QtWidgets.QGraphicsView(self.main_frame)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_close = QtWidgets.QPushButton(self.main_frame)
        self.pushButton_close.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/label_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon)
        self.pushButton_close.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_close.setShortcut("")
        self.pushButton_close.setCheckable(False)
        self.pushButton_close.setAutoExclusive(False)
        self.pushButton_close.setAutoRepeatDelay(300)
        self.pushButton_close.setAutoDefault(True)
        self.pushButton_close.setDefault(False)
        self.pushButton_close.setFlat(False)
        self.pushButton_close.setObjectName("pushButton_close")
        self.verticalLayout_5.addWidget(self.pushButton_close, 0, QtCore.Qt.AlignRight)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.frame_label_wait = QtWidgets.QFrame(self.main_frame)
        self.frame_label_wait.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_wait.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_wait.setObjectName("frame_label_wait")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_label_wait)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_wait = QtWidgets.QLabel(self.frame_label_wait)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.label_wait.setFont(font)
        self.label_wait.setObjectName("label_wait")
        self.verticalLayout_4.addWidget(self.label_wait, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_label_wait)
        self.verticalLayout.addWidget(self.main_frame)

        self.retranslateUi(Dialog)
        self.pushButton_close.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_wait.setText(_translate("Dialog", "Please wait..."))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
