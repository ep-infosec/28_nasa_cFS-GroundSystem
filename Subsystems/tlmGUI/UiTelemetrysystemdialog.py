# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lbleier/cFS/tools/cFS-GroundSystem/Subsystems/tlmGUI/TelemetrySystemDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiTelemetrysystemdialog(object):
    def setupUi(self, telemetry_system_dialog):
        telemetry_system_dialog.setObjectName("TelemetrySystemDialog")
        telemetry_system_dialog.resize(625, 908)
        self.vertical_layout = QtWidgets.QVBoxLayout(telemetry_system_dialog)
        self.vertical_layout.setObjectName("verticalLayout")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontalLayout")
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacer_item)
        self.label = QtWidgets.QLabel(telemetry_system_dialog)
        self.label.setObjectName("label")
        self.horizontal_layout.addWidget(self.label)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacer_item1)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontal_layout_3.setObjectName("horizontalLayout_3")
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_3.addItem(spacer_item2)
        spacer_item3 = QtWidgets.QSpacerItem(80, 32, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_3.addItem(spacer_item3)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontalLayout_2")
        spacer_item4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacer_item4)
        self.label_6 = QtWidgets.QLabel(telemetry_system_dialog)
        self.label_6.setObjectName("label_6")
        self.horizontal_layout_2.addWidget(self.label_6)
        self.packet_count = QtWidgets.QSpinBox(telemetry_system_dialog)
        self.packet_count.setReadOnly(True)
        self.packet_count.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.packet_count.setMaximum(16384)
        self.packet_count.setProperty("value", 0)
        self.packet_count.setObjectName("packetCount")
        self.horizontal_layout_2.addWidget(self.packet_count)
        spacer_item5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacer_item5)
        self.horizontal_layout_3.addLayout(self.horizontal_layout_2)
        spacer_item6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_3.addItem(spacer_item6)
        self.button_box = QtWidgets.QDialogButtonBox(telemetry_system_dialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.button_box.setObjectName("buttonBox")
        self.horizontal_layout_3.addWidget(self.button_box)
        self.vertical_layout.addLayout(self.horizontal_layout_3)
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_4.setObjectName("horizontalLayout_4")
        spacer_item7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_4.addItem(spacer_item7)
        self.label_2 = QtWidgets.QLabel(telemetry_system_dialog)
        self.label_2.setObjectName("label_2")
        self.horizontal_layout_4.addWidget(self.label_2)
        spacer_item8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_4.addItem(spacer_item8)
        self.vertical_layout.addLayout(self.horizontal_layout_4)
        self.tbl_tlm_sys = QtWidgets.QTableWidget(telemetry_system_dialog)
        self.tbl_tlm_sys.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_tlm_sys.setObjectName("tblTlmSys")
        self.tbl_tlm_sys.setColumnCount(4)
        self.tbl_tlm_sys.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tlm_sys.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tlm_sys.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tlm_sys.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_tlm_sys.setHorizontalHeaderItem(3, item)
        self.tbl_tlm_sys.verticalHeader().setVisible(False)
        self.vertical_layout.addWidget(self.tbl_tlm_sys)

        self.retranslateUi(telemetry_system_dialog)
        self.button_box.clicked['QAbstractButton*'].connect(telemetry_system_dialog.close)
        QtCore.QMetaObject.connectSlotsByName(telemetry_system_dialog)

    def retranslateUi(self, telemetry_system_dialog):
        _translate = QtCore.QCoreApplication.translate
        telemetry_system_dialog.setWindowTitle(_translate("TelemetrySystemDialog", "Dialog"))
        self.label.setText(_translate("TelemetrySystemDialog", "cFE/CFS Subsystem Telemetry"))
        self.label_6.setText(_translate("TelemetrySystemDialog", "Packets Received"))
        self.label_2.setText(_translate("TelemetrySystemDialog", "Available Pages"))
        item = self.tbl_tlm_sys.horizontalHeaderItem(0)
        item.setText(_translate("TelemetrySystemDialog", "Subsystem/Page"))
        item = self.tbl_tlm_sys.horizontalHeaderItem(1)
        item.setText(_translate("TelemetrySystemDialog", "Packet ID"))
        item = self.tbl_tlm_sys.horizontalHeaderItem(2)
        item.setText(_translate("TelemetrySystemDialog", "Packet Count"))
        item = self.tbl_tlm_sys.horizontalHeaderItem(3)
        item.setText(_translate("TelemetrySystemDialog", " "))

