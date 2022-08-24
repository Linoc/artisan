# Form implementation generated from reading ui file 'ui/MeasureDialog.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_setMeasureDialog(object):
    def setupUi(self, setMeasureDialog):
        setMeasureDialog.setObjectName("setMeasureDialog")
        setMeasureDialog.resize(466, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(setMeasureDialog.sizePolicy().hasHeightForWidth())
        setMeasureDialog.setSizePolicy(sizePolicy)
        setMeasureDialog.setWindowTitle("Set Measure from Profile")
        setMeasureDialog.setToolTip("")
        setMeasureDialog.setAccessibleDescription("")
        setMeasureDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(setMeasureDialog)
        self.verticalLayout.setContentsMargins(10, 12, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(setMeasureDialog)
        self.groupBox.setToolTip("")
        self.groupBox.setAccessibleDescription("")
        self.groupBox.setTitle("Title")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.loadBlabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        self.loadBlabel.setFont(font)
        self.loadBlabel.setToolTip("")
        self.loadBlabel.setAccessibleDescription("")
        self.loadBlabel.setText("Load B")
        self.loadBlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loadBlabel.setObjectName("loadBlabel")
        self.gridLayout.addWidget(self.loadBlabel, 2, 4, 1, 2)
        self.loadC = QtWidgets.QLabel(self.groupBox)
        self.loadC.setToolTip("")
        self.loadC.setAccessibleDescription("")
        self.loadC.setText("")
        self.loadC.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.loadC.setObjectName("loadC")
        self.gridLayout.addWidget(self.loadC, 3, 6, 1, 1)
        self.durationlabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        self.durationlabel.setFont(font)
        self.durationlabel.setToolTip("")
        self.durationlabel.setAccessibleDescription("")
        self.durationlabel.setText("Duration")
        self.durationlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.durationlabel.setObjectName("durationlabel")
        self.gridLayout.addWidget(self.durationlabel, 2, 0, 1, 1)
        self.loadDlabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        self.loadDlabel.setFont(font)
        self.loadDlabel.setToolTip("")
        self.loadDlabel.setAccessibleDescription("")
        self.loadDlabel.setText("Load D")
        self.loadDlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loadDlabel.setObjectName("loadDlabel")
        self.gridLayout.addWidget(self.loadDlabel, 2, 8, 1, 2)
        self.loadAunit = QtWidgets.QLabel(self.groupBox)
        self.loadAunit.setToolTip("")
        self.loadAunit.setAccessibleDescription("")
        self.loadAunit.setText("")
        self.loadAunit.setObjectName("loadAunit")
        self.gridLayout.addWidget(self.loadAunit, 3, 3, 1, 1)
        self.loadCunit = QtWidgets.QLabel(self.groupBox)
        self.loadCunit.setToolTip("")
        self.loadCunit.setAccessibleDescription("")
        self.loadCunit.setText("")
        self.loadCunit.setObjectName("loadCunit")
        self.gridLayout.addWidget(self.loadCunit, 3, 7, 1, 1)
        self.loadD = QtWidgets.QLabel(self.groupBox)
        self.loadD.setToolTip("")
        self.loadD.setAccessibleDescription("")
        self.loadD.setText("")
        self.loadD.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.loadD.setObjectName("loadD")
        self.gridLayout.addWidget(self.loadD, 3, 8, 1, 1)
        self.duration = QtWidgets.QLabel(self.groupBox)
        self.duration.setToolTip("")
        self.duration.setAccessibleDescription("")
        self.duration.setText("")
        self.duration.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.duration.setObjectName("duration")
        self.gridLayout.addWidget(self.duration, 3, 0, 1, 1)
        self.loadB = QtWidgets.QLabel(self.groupBox)
        self.loadB.setToolTip("")
        self.loadB.setAccessibleDescription("")
        self.loadB.setText("")
        self.loadB.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.loadB.setObjectName("loadB")
        self.gridLayout.addWidget(self.loadB, 3, 4, 1, 1)
        self.loadAlabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        self.loadAlabel.setFont(font)
        self.loadAlabel.setToolTip("")
        self.loadAlabel.setAccessibleDescription("")
        self.loadAlabel.setText("Load A")
        self.loadAlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loadAlabel.setObjectName("loadAlabel")
        self.gridLayout.addWidget(self.loadAlabel, 2, 2, 1, 2)
        self.loadBunit = QtWidgets.QLabel(self.groupBox)
        self.loadBunit.setToolTip("")
        self.loadBunit.setAccessibleDescription("")
        self.loadBunit.setText("")
        self.loadBunit.setObjectName("loadBunit")
        self.gridLayout.addWidget(self.loadBunit, 3, 5, 1, 1)
        self.loadA = QtWidgets.QLabel(self.groupBox)
        self.loadA.setToolTip("")
        self.loadA.setAccessibleDescription("")
        self.loadA.setText("")
        self.loadA.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.loadA.setObjectName("loadA")
        self.gridLayout.addWidget(self.loadA, 3, 2, 1, 1)
        self.loadDunit = QtWidgets.QLabel(self.groupBox)
        self.loadDunit.setToolTip("")
        self.loadDunit.setAccessibleDescription("")
        self.loadDunit.setText("")
        self.loadDunit.setObjectName("loadDunit")
        self.gridLayout.addWidget(self.loadDunit, 3, 9, 1, 1)
        self.loadClabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        self.loadClabel.setFont(font)
        self.loadClabel.setToolTip("")
        self.loadClabel.setAccessibleDescription("")
        self.loadClabel.setText("Load C")
        self.loadClabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loadClabel.setObjectName("loadClabel")
        self.gridLayout.addWidget(self.loadClabel, 2, 6, 1, 2)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 1, 2, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(setMeasureDialog)
        self.buttonBox.setToolTip("")
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(setMeasureDialog)
        self.buttonBox.accepted.connect(setMeasureDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(setMeasureDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(setMeasureDialog)

    def retranslateUi(self, setMeasureDialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setMeasureDialog = QtWidgets.QDialog()
    ui = Ui_setMeasureDialog()
    ui.setupUi(setMeasureDialog)
    setMeasureDialog.show()
    sys.exit(app.exec())
