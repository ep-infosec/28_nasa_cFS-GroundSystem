# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lbleier/cFS/tools/cFS-GroundSystem/Subsystems/cmdGui/ParameterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiDialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.setEnabled(True)
        dialog.resize(782, 550)
        self.label_title = QtWidgets.QLabel(dialog)
        self.label_title.setGeometry(QtCore.QRect(330, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_instructions = QtWidgets.QLabel(dialog)
        self.label_instructions.setGeometry(QtCore.QRect(120, 140, 551, 31))
        self.label_instructions.setAlignment(QtCore.Qt.AlignCenter)
        self.label_instructions.setObjectName("label_instructions")
        self.button_box = QtWidgets.QDialogButtonBox(dialog)
        self.button_box.setGeometry(QtCore.QRect(670, 490, 101, 31))
        self.button_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.button_box.setCenterButtons(True)
        self.button_box.setObjectName("buttonBox")
        self.status_box = QtWidgets.QTextBrowser(dialog)
        self.status_box.setGeometry(QtCore.QRect(480, 40, 201, 41))
        self.status_box.setAutoFillBackground(False)
        self.status_box.setObjectName("status_box")
        self.label_param_title_2 = QtWidgets.QLabel(dialog)
        self.label_param_title_2.setGeometry(QtCore.QRect(480, 10, 61, 21))
        self.label_param_title_2.setObjectName("label_param_title_2")
        self.send_button_1 = QtWidgets.QPushButton(dialog)
        self.send_button_1.setGeometry(QtCore.QRect(690, 47, 71, 27))
        self.send_button_1.setAutoDefault(False)
        self.send_button_1.setDefault(True)
        self.send_button_1.setObjectName("SendButton_1")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(260, 10, 81, 20))
        self.label_5.setObjectName("label_5")
        self.sub_system_command_page_label = QtWidgets.QLabel(dialog)
        self.sub_system_command_page_label.setGeometry(QtCore.QRect(30, 10, 91, 24))
        self.sub_system_command_page_label.setObjectName("subSystemCommandPageLabel")
        self.sub_system_text_browser = QtWidgets.QTextBrowser(dialog)
        self.sub_system_text_browser.setGeometry(QtCore.QRect(30, 40, 221, 41))
        self.sub_system_text_browser.setObjectName("subSystemTextBrowser")
        self.command_address_text_browser = QtWidgets.QTextBrowser(dialog)
        self.command_address_text_browser.setGeometry(QtCore.QRect(260, 40, 211, 41))
        self.command_address_text_browser.setObjectName("commandAddressTextBrowser")
        self.tbl_parameters = QtWidgets.QTableWidget(dialog)
        self.tbl_parameters.setGeometry(QtCore.QRect(20, 180, 731, 301))
        self.tbl_parameters.setObjectName("tblParameters")
        self.tbl_parameters.setColumnCount(3)
        self.tbl_parameters.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_parameters.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_parameters.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_parameters.setHorizontalHeaderItem(2, item)
        self.tbl_parameters.verticalHeader().setVisible(False)

        self.retranslate_ui(dialog)
        self.button_box.clicked['QAbstractButton*'].connect(dialog.close)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.status_box, self.send_button_1)
        dialog.setTabOrder(self.send_button_1, self.sub_system_text_browser)
        dialog.setTabOrder(self.sub_system_text_browser, self.command_address_text_browser)

    def retranslate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_title.setText(_translate("Dialog", "Parameters"))
        self.label_instructions.setText(_translate("Dialog", "Please enter the following parameters then click \'Send\':"))
        self.label_param_title_2.setText(_translate("Dialog", "Status:"))
        self.send_button_1.setText(_translate("Dialog", "Send"))
        self.label_5.setText(_translate("Dialog", "Command:"))
        self.sub_system_command_page_label.setText(_translate("Dialog", "Subsystem:"))
        item = self.tbl_parameters.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Parameter"))
        item = self.tbl_parameters.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Description"))
        item = self.tbl_parameters.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Input"))

