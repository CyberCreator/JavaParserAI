# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.widget = mathlibplot_widget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionAdd_project = QtWidgets.QAction(MainWindow)
        self.actionAdd_project.setObjectName("actionAdd_project")
        self.actionDelete_this_project = QtWidgets.QAction(MainWindow)
        self.actionDelete_this_project.setObjectName("actionDelete_this_project")
        self.menuFile.addAction(self.actionAdd_project)
        self.menuFile.addAction(self.actionDelete_this_project)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JavaParserAI"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "project"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(6).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(7).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(8).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(9).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAdd_project.setText(_translate("MainWindow", "Add project"))
        self.actionDelete_this_project.setText(_translate("MainWindow", "Delete this project"))


from mathlibplot_widget import mathlibplot_widget
