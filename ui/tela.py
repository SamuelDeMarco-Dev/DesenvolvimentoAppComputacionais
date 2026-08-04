# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLCDNumber, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 400)
        self.lcdNumber = QLCDNumber(Dialog)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(13, 20, 361, 91))
        self.btn_decrementar = QPushButton(Dialog)
        self.btn_decrementar.setObjectName(u"btn_decrementar")
        self.btn_decrementar.setGeometry(QRect(10, 120, 161, 251))
        self.btn_incrementar = QPushButton(Dialog)
        self.btn_incrementar.setObjectName(u"btn_incrementar")
        self.btn_incrementar.setGeometry(QRect(210, 120, 161, 251))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_decrementar.setText(QCoreApplication.translate("Dialog", u"Decrementar", None))
        self.btn_incrementar.setText(QCoreApplication.translate("Dialog", u"Incrementar", None))
    # retranslateUi

