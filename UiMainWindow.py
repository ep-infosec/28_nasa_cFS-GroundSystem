# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lbleier/cFS/tools/cFS-GroundSystem/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.setEnabled(True)
        main_window.resize(552, 305)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(24)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("centralwidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("verticalLayout")
        self.label_home_title = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_home_title.setFont(font)
        self.label_home_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home_title.setObjectName("labelHomeTitle")
        self.vertical_layout.addWidget(self.label_home_title)
        self.line_2 = QtWidgets.QFrame(self.central_widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.vertical_layout.addWidget(self.line_2)
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(size_policy)
        self.label_3.setMinimumSize(QtCore.QSize(141, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.grid_layout.addWidget(self.label_3, 0, 0, 1, 1)
        self.combo_box_ip_addresses = QtWidgets.QComboBox(self.central_widget)
        self.combo_box_ip_addresses.setMinimumSize(QtCore.QSize(132, 0))
        self.combo_box_ip_addresses.setMaximumSize(QtCore.QSize(132, 16777215))
        self.combo_box_ip_addresses.setObjectName("comboBoxIpAddresses")
        self.combo_box_ip_addresses.addItem("")
        self.grid_layout.addWidget(self.combo_box_ip_addresses, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(size_policy)
        self.label_4.setMinimumSize(QtCore.QSize(169, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.grid_layout.addWidget(self.label_4, 1, 0, 1, 1)
        self.cb_tlm_header_ver = QtWidgets.QComboBox(self.central_widget)
        self.cb_tlm_header_ver.setMinimumSize(QtCore.QSize(132, 0))
        self.cb_tlm_header_ver.setMaximumSize(QtCore.QSize(132, 16777215))
        self.cb_tlm_header_ver.setObjectName("cbTlmHeaderVer")
        self.cb_tlm_header_ver.addItem("")
        self.cb_tlm_header_ver.addItem("")
        self.cb_tlm_header_ver.addItem("")
        self.grid_layout.addWidget(self.cb_tlm_header_ver, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setObjectName("label_2")
        self.grid_layout.addWidget(self.label_2, 2, 0, 1, 1)
        self.sb_tlm_offset = QtWidgets.QSpinBox(self.central_widget)
        self.sb_tlm_offset.setEnabled(False)
        self.sb_tlm_offset.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_tlm_offset.setObjectName("sbTlmOffset")
        self.grid_layout.addWidget(self.sb_tlm_offset, 1, 2, 1, 1)
        self.sb_cmd_offset_pri = QtWidgets.QSpinBox(self.central_widget)
        self.sb_cmd_offset_pri.setEnabled(False)
        self.sb_cmd_offset_pri.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_cmd_offset_pri.setObjectName("sbCmdOffsetPri")
        self.grid_layout.addWidget(self.sb_cmd_offset_pri, 2, 2, 1, 1)
        self.cb_cmd_header_ver = QtWidgets.QComboBox(self.central_widget)
        self.cb_cmd_header_ver.setObjectName("cbCmdHeaderVer")
        self.cb_cmd_header_ver.addItem("")
        self.cb_cmd_header_ver.addItem("")
        self.cb_cmd_header_ver.addItem("")
        self.grid_layout.addWidget(self.cb_cmd_header_ver, 2, 1, 1, 1)
        self.sb_cmd_offset_sec = QtWidgets.QSpinBox(self.central_widget)
        self.sb_cmd_offset_sec.setEnabled(False)
        self.sb_cmd_offset_sec.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_cmd_offset_sec.setObjectName("sbCmdOffsetSec")
        self.grid_layout.addWidget(self.sb_cmd_offset_sec, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setObjectName("label")
        self.grid_layout.addWidget(self.label, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.central_widget)
        self.label_6.setObjectName("label_6")
        self.grid_layout.addWidget(self.label_6, 0, 3, 1, 1)
        self.vertical_layout.addLayout(self.grid_layout)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setSpacing(32)
        self.horizontal_layout_2.setObjectName("horizontalLayout_2")
        self.push_button_start_tlm = QtWidgets.QPushButton(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.push_button_start_tlm.sizePolicy().hasHeightForWidth())
        self.push_button_start_tlm.setSizePolicy(size_policy)
        self.push_button_start_tlm.setObjectName("pushButtonStartTlm")
        self.horizontal_layout_2.addWidget(self.push_button_start_tlm)
        self.push_button_start_cmd = QtWidgets.QPushButton(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.push_button_start_cmd.sizePolicy().hasHeightForWidth())
        self.push_button_start_cmd.setSizePolicy(size_policy)
        self.push_button_start_cmd.setObjectName("pushButtonStartCmd")
        self.horizontal_layout_2.addWidget(self.push_button_start_cmd)
        self.vertical_layout.addLayout(self.horizontal_layout_2)
        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.vertical_layout.addWidget(self.line)
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontal_layout_4.addWidget(self.label_5)
        self.push_button = QtWidgets.QPushButton(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.push_button.sizePolicy().hasHeightForWidth())
        self.push_button.setSizePolicy(size_policy)
        self.push_button.setObjectName("pushButton")
        self.horizontal_layout_4.addWidget(self.push_button)
        self.vertical_layout.addLayout(self.horizontal_layout_4)
        main_window.setCentralWidget(self.central_widget)

        self.retranslate_ui(main_window)
        self.push_button.clicked.connect(main_window.close)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Main Window"))
        self.label_home_title.setText(_translate("MainWindow", "CFS Ground System"))
        self.label_3.setText(_translate("MainWindow", "Selected IP Address"))
        self.combo_box_ip_addresses.setItemText(0, _translate("MainWindow", "All"))
        self.label_4.setText(_translate("MainWindow", "Tlm header version"))
        self.cb_tlm_header_ver.setItemText(0, _translate("MainWindow", "1"))
        self.cb_tlm_header_ver.setItemText(1, _translate("MainWindow", "2"))
        self.cb_tlm_header_ver.setItemText(2, _translate("MainWindow", "Custom"))
        self.label_2.setText(_translate("MainWindow", "Cmd header version"))
        self.sb_tlm_offset.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Offset (in bytes) to be <span style=\" font-weight:600;\">added to</span> existing offsets listed in telemetry text files</p></body></html>"))
        self.sb_cmd_offset_pri.setToolTip(_translate("MainWindow",
                                                  "<html><head/><body><p>Offset (in bytes) to be added <span style=\" font-weight:600;\">after</span> the <span style=\" font-weight:600;\">primary</span> header in a command packet</p></body></html>"))
        self.cb_cmd_header_ver.setItemText(0, _translate("MainWindow", "1"))
        self.cb_cmd_header_ver.setItemText(1, _translate("MainWindow", "2"))
        self.cb_cmd_header_ver.setItemText(2, _translate("MainWindow", "Custom"))
        self.sb_cmd_offset_sec.setToolTip(_translate("MainWindow",
                                                  "<html><head/><body><p>Offset (in bytes) to be added <span style=\" font-weight:600;\">after</span> the <span style=\" font-weight:600;\">secondary</span> header in a command packet</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Offsets"))
        self.label_6.setText(_translate("MainWindow", "(Hover for info)"))
        self.push_button_start_tlm.setText(_translate("MainWindow", "Start Telemetry System"))
        self.push_button_start_cmd.setText(_translate("MainWindow", "Start Command System"))
        self.label_5.setText(_translate("MainWindow", "*Read Guide-GroundSystem.txt for help"))
        self.push_button.setText(_translate("MainWindow", "Close"))
