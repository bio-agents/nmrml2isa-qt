# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/contact.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 320)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 270, 181, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(20, 220, 131, 25))
        self.label_20.setObjectName("label_20")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(150, 20, 71, 16))
        self.label_15.setScaledContents(False)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(20, 120, 131, 25))
        self.label_18.setObjectName("label_18")
        self.last_name = QtWidgets.QLineEdit(Dialog)
        self.last_name.setGeometry(QtCore.QRect(235, 40, 195, 25))
        self.last_name.setObjectName("last_name")
        self.roles = QtWidgets.QLineEdit(Dialog)
        self.roles.setEnabled(True)
        self.roles.setGeometry(QtCore.QRect(20, 240, 195, 25))
        self.roles.setStyleSheet("color: rgb(0, 0, 0);")
        self.roles.setFrame(False)
        self.roles.setObjectName("roles")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(235, 120, 131, 25))
        self.label_21.setObjectName("label_21")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(20, 70, 131, 25))
        self.label_16.setObjectName("label_16")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_13.setObjectName("label_13")
        self.first_name = QtWidgets.QLineEdit(Dialog)
        self.first_name.setGeometry(QtCore.QRect(20, 40, 130, 25))
        self.first_name.setObjectName("first_name")
        self.adress = QtWidgets.QPlainTextEdit(Dialog)
        self.adress.setGeometry(QtCore.QRect(235, 139, 195, 131))
        self.adress.setObjectName("adress")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(235, 90, 195, 25))
        self.email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email.setObjectName("email")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(235, 70, 131, 25))
        self.label_17.setObjectName("label_17")
        self.affiliation = QtWidgets.QLineEdit(Dialog)
        self.affiliation.setGeometry(QtCore.QRect(20, 190, 195, 25))
        self.affiliation.setObjectName("affiliation")
        self.fax = QtWidgets.QLineEdit(Dialog)
        self.fax.setGeometry(QtCore.QRect(20, 140, 195, 25))
        self.fax.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.fax.setObjectName("fax")
        self.combo_roles = QtWidgets.QComboBox(Dialog)
        self.combo_roles.setEnabled(False)
        self.combo_roles.setGeometry(QtCore.QRect(20, 240, 195, 25))
        self.combo_roles.setObjectName("combo_roles")
        self.label_pro = QtWidgets.QLabel(Dialog)
        self.label_pro.setGeometry(QtCore.QRect(30, 240, 241, 25))
        self.label_pro.setWordWrap(True)
        self.label_pro.setObjectName("label_pro")
        self.mid = QtWidgets.QLineEdit(Dialog)
        self.mid.setGeometry(QtCore.QRect(170, 40, 45, 25))
        self.mid.setObjectName("mid")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(235, 20, 131, 16))
        self.label_14.setObjectName("label_14")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(20, 170, 131, 25))
        self.label_23.setObjectName("label_23")
        self.phone = QtWidgets.QLineEdit(Dialog)
        self.phone.setGeometry(QtCore.QRect(20, 90, 195, 25))
        self.phone.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.phone.setObjectName("phone")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.first_name, self.mid)
        Dialog.setTabOrder(self.mid, self.last_name)
        Dialog.setTabOrder(self.last_name, self.phone)
        Dialog.setTabOrder(self.phone, self.email)
        Dialog.setTabOrder(self.email, self.fax)
        Dialog.setTabOrder(self.fax, self.affiliation)
        Dialog.setTabOrder(self.affiliation, self.combo_roles)
        Dialog.setTabOrder(self.combo_roles, self.adress)
        Dialog.setTabOrder(self.adress, self.roles)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Contact"))
        self.label_20.setText(_translate("Dialog", "Role"))
        self.label_15.setText(_translate("Dialog", "Mid Initials"))
        self.label_18.setText(_translate("Dialog", "Fax"))
        self.label_21.setText(_translate("Dialog", "Adress"))
        self.label_16.setText(_translate("Dialog", "Telephone"))
        self.label_13.setText(_translate("Dialog", "First Name"))
        self.label_17.setText(_translate("Dialog", "Mail"))
        self.label_pro.setText(_translate("Dialog", "connecting to PRO <...>"))
        self.label_14.setText(_translate("Dialog", "Last Name"))
        self.label_23.setText(_translate("Dialog", "Affiliation"))

