# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fergie\Desktop\VM_LAB2\design_last.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 489)
        MainWindow.setMinimumSize(QtCore.QSize(580, 489))
        MainWindow.setMaximumSize(QtCore.QSize(580, 489))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setWindowIcon(QtGui.QIcon('paw.ico'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.Main_list_widget.setEnabled(True)
        self.Main_list_widget.setMinimumSize(QtCore.QSize(571, 489))
        self.Main_list_widget.setMaximumSize(QtCore.QSize(571, 489))
        self.Main_list_widget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Main_list_widget.setStyleSheet("background-color: rgb(255, 229, 230);\n"
"font: 75 11pt \"Comic Sans MS\";\n"
"\n"
"background-color: rgb(255, 235, 243);\n"
"border-color: rgb(255, 185, 223);\n"
"color: rgb(255, 185, 210);\n"
"color: rgb(255, 181, 201);\n"
"color: rgb(255, 162, 199);\n"
"gridline-color: rgb(255, 128, 196);\n"
"\n"
"background-image: url(C:/Users/Fergie/Desktop/VM_LAB2/cats.jpg);")
        self.Main_list_widget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Main_list_widget.setLineWidth(0)
        self.Main_list_widget.setObjectName("Main_list_widget")
        self.ButtonBar = QtWidgets.QFrame(self.centralwidget)
        self.ButtonBar.setGeometry(QtCore.QRect(20, 350, 241, 81))
        self.ButtonBar.setStyleSheet("background-image: url(C:/Users/Fergie/Desktop/VM_LAB2/pink.jpg);")
        self.ButtonBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonBar.setObjectName("ButtonBar")
        self.load_button = QtWidgets.QPushButton(self.ButtonBar)
        self.load_button.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.load_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.load_button.setObjectName("load_button")
        self.Save_button = QtWidgets.QPushButton(self.ButtonBar)
        self.Save_button.setGeometry(QtCore.QRect(80, 50, 71, 21))
        self.Save_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Save_button.setObjectName("Save_button")
        self.Solve_button = QtWidgets.QPushButton(self.ButtonBar)
        self.Solve_button.setGeometry(QtCore.QRect(160, 50, 71, 21))
        self.Solve_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Solve_button.setObjectName("Solve_button")
        self.inp_a = QtWidgets.QLineEdit(self.ButtonBar)
        self.inp_a.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.inp_a.setStyleSheet("background: url(C:/Users/Fergie/Desktop/VM_LAB2/cats.jpg);")
        self.inp_a.setObjectName("inp_a")
        self.inp_b = QtWidgets.QLineEdit(self.ButtonBar)
        self.inp_b.setGeometry(QtCore.QRect(100, 20, 61, 21))
        self.inp_b.setStyleSheet("background: url(C:/Users/Fergie/Desktop/VM_LAB2/cats.jpg);")
        self.inp_b.setObjectName("inp_b")
        self.inp_e = QtWidgets.QLineEdit(self.ButtonBar)
        self.inp_e.setGeometry(QtCore.QRect(180, 20, 51, 21))
        self.inp_e.setStyleSheet("background: url(C:/Users/Fergie/Desktop/VM_LAB2/cats.jpg);")
        self.inp_e.setObjectName("inp_e")
        self.label_prompt = QtWidgets.QLabel(self.ButtonBar)
        self.label_prompt.setGeometry(QtCore.QRect(10, 0, 301, 16))
        self.label_prompt.setStyleSheet("background-image: url(C:/Users/Fergie/Desktop/pink.jpg);")
        self.label_prompt.setObjectName("label_prompt")
        self.prompt_a = QtWidgets.QLabel(self.ButtonBar)
        self.prompt_a.setGeometry(QtCore.QRect(6, 20, 16, 20))
        self.prompt_a.setStyleSheet("background-image: url(C:/Users/Fergie/Desktop/pink.jpg);")
        self.prompt_a.setObjectName("prompt_a")
        self.prompt_b = QtWidgets.QLabel(self.ButtonBar)
        self.prompt_b.setGeometry(QtCore.QRect(90, 20, 16, 20))
        self.prompt_b.setStyleSheet("background-image: url(C:/Users/Fergie/Desktop/pink.jpg);")
        self.prompt_b.setObjectName("prompt_b")
        self.prompt_c = QtWidgets.QLabel(self.ButtonBar)
        self.prompt_c.setGeometry(QtCore.QRect(170, 20, 16, 16))
        self.prompt_c.setStyleSheet("background-image: url(C:/Users/Fergie/Desktop/pink.jpg);")
        self.prompt_c.setObjectName("prompt_c")
        self.menu_box = QtWidgets.QGroupBox(self.centralwidget)
        self.menu_box.setGeometry(QtCore.QRect(20, 60, 241, 281))
        self.menu_box.setStyleSheet("background-image: url(C:/Users/Fergie/Desktop/VM_LAB2/pink.jpg);")
        self.menu_box.setTitle("")
        self.menu_box.setObjectName("menu_box")
        self.choise_factory_label = QtWidgets.QLabel(self.menu_box)
        self.choise_factory_label.setGeometry(QtCore.QRect(30, 10, 231, 41))
        self.choise_factory_label.setStyleSheet("font: 50 20pt \"Comic Sans MS\";\n"
"color:rgb(255, 162, 199);\n"
"")
        self.choise_factory_label.setObjectName("choise_factory_label")
        self.system_eq_1 = QtWidgets.QRadioButton(self.menu_box)
        self.system_eq_1.setGeometry(QtCore.QRect(10, 280, 201, 31))
        self.system_eq_1.setText("")
        self.system_eq_1.setObjectName("system_eq_1")
        self.stackedWidget = QtWidgets.QStackedWidget(self.menu_box)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 50, 201, 221))
        self.stackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.stackedWidget.setObjectName("stackedWidget")
        self.eq_type_page = QtWidgets.QWidget()
        self.eq_type_page.setObjectName("eq_type_page")
        self.choose_equation_type_label = QtWidgets.QLabel(self.eq_type_page)
        self.choose_equation_type_label.setGeometry(QtCore.QRect(10, 20, 191, 21))
        self.choose_equation_type_label.setStyleSheet("font: 70 11pt \"Comic Sans MS\";\n"
"color:rgb(255, 162, 199);")
        self.choose_equation_type_label.setObjectName("choose_equation_type_label")
        self.single_button = QtWidgets.QPushButton(self.eq_type_page)
        self.single_button.setGeometry(QtCore.QRect(0, 70, 201, 41))
        self.single_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.single_button.setObjectName("single_button")
        self.system_button = QtWidgets.QPushButton(self.eq_type_page)
        self.system_button.setGeometry(QtCore.QRect(0, 140, 201, 41))
        self.system_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.system_button.setObjectName("system_button")
        self.stackedWidget.addWidget(self.eq_type_page)
        self.single_eq_page = QtWidgets.QWidget()
        self.single_eq_page.setObjectName("single_eq_page")
        self.choose_equation = QtWidgets.QLabel(self.single_eq_page)
        self.choose_equation.setGeometry(QtCore.QRect(20, 10, 191, 21))
        self.choose_equation.setStyleSheet("font: 70 11pt \"Comic Sans MS\";\n"
"color:rgb(255, 162, 199);")
        self.choose_equation.setObjectName("choose_equation")
        self.single_eq_1 = QtWidgets.QRadioButton(self.single_eq_page)
        self.single_eq_1.setGeometry(QtCore.QRect(10, 40, 171, 17))
        self.single_eq_1.setObjectName("single_eq_1")
        self.single_eq_2 = QtWidgets.QRadioButton(self.single_eq_page)
        self.single_eq_2.setGeometry(QtCore.QRect(10, 70, 141, 17))
        self.single_eq_2.setObjectName("single_eq_2")
        self.single_eq_3 = QtWidgets.QRadioButton(self.single_eq_page)
        self.single_eq_3.setGeometry(QtCore.QRect(10, 100, 111, 17))
        self.single_eq_3.setObjectName("single_eq_3")
        self.back_to_method_button = QtWidgets.QPushButton(self.single_eq_page)
        self.back_to_method_button.setGeometry(QtCore.QRect(0, 130, 201, 31))
        self.back_to_method_button.setObjectName("back_to_method_button")
        self.pushButton_2 = QtWidgets.QPushButton(self.single_eq_page)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 180, 201, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.single_eq_page)
        self.sys_eq_page = QtWidgets.QWidget()
        self.sys_eq_page.setObjectName("sys_eq_page")
        self.choose_equation_2 = QtWidgets.QLabel(self.sys_eq_page)
        self.choose_equation_2.setGeometry(QtCore.QRect(20, 10, 191, 21))
        self.choose_equation_2.setStyleSheet("font: 70 11pt \"Comic Sans MS\";\n"
"color:rgb(255, 162, 199);")
        self.choose_equation_2.setObjectName("choose_equation_2")
        self.system_eq_2 = QtWidgets.QRadioButton(self.sys_eq_page)
        self.system_eq_2.setGeometry(QtCore.QRect(20, 30, 171, 51))
        self.system_eq_2.setObjectName("system_eq_2")
        self.back_to_method_button_2 = QtWidgets.QPushButton(self.sys_eq_page)
        self.back_to_method_button_2.setGeometry(QtCore.QRect(0, 130, 201, 31))
        self.back_to_method_button_2.setObjectName("back_to_method_button_2")
        self.pushButton = QtWidgets.QPushButton(self.sys_eq_page)
        self.pushButton.setGeometry(QtCore.QRect(0, 182, 201, 31))
        self.pushButton.setObjectName("pushButton")
        self.system_eq_3 = QtWidgets.QRadioButton(self.sys_eq_page)
        self.system_eq_3.setGeometry(QtCore.QRect(20, 70, 171, 51))
        self.system_eq_3.setObjectName("system_eq_3")
        self.stackedWidget.addWidget(self.sys_eq_page)
        self.method_page = QtWidgets.QWidget()
        self.method_page.setObjectName("method_page")
        self.choose_equation_method = QtWidgets.QLabel(self.method_page)
        self.choose_equation_method.setEnabled(True)
        self.choose_equation_method.setGeometry(QtCore.QRect(20, 10, 191, 21))
        self.choose_equation_method.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.choose_equation_method.setMouseTracking(False)
        self.choose_equation_method.setStyleSheet("font: 80 11pt \"Comic Sans MS\";\n"
"color:rgb(255, 162, 199);")
        self.choose_equation_method.setObjectName("choose_equation_method")
        self.back_to_type_button = QtWidgets.QPushButton(self.method_page)
        self.back_to_type_button.setGeometry(QtCore.QRect(0, 180, 201, 31))
        self.back_to_type_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.back_to_type_button.setObjectName("back_to_type_button")
        self.chorde_btn = QtWidgets.QRadioButton(self.method_page)
        self.chorde_btn.setGeometry(QtCore.QRect(10, 40, 181, 17))
        self.chorde_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chorde_btn.setObjectName("chorde_btn")
        self.newton_btn = QtWidgets.QRadioButton(self.method_page)
        self.newton_btn.setGeometry(QtCore.QRect(10, 70, 151, 17))
        self.newton_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newton_btn.setObjectName("newton_btn")
        self.simple_it_btn = QtWidgets.QRadioButton(self.method_page)
        self.simple_it_btn.setGeometry(QtCore.QRect(10, 100, 151, 17))
        self.simple_it_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.simple_it_btn.setObjectName("simple_it_btn")
        self.next_btn = QtWidgets.QPushButton(self.method_page)
        self.next_btn.setGeometry(QtCore.QRect(0, 130, 201, 31))
        self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.next_btn.setObjectName("next_btn")
        self.stackedWidget.addWidget(self.method_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.choose_equation_method_2 = QtWidgets.QLabel(self.page)
        self.choose_equation_method_2.setEnabled(True)
        self.choose_equation_method_2.setGeometry(QtCore.QRect(20, 10, 191, 21))
        self.choose_equation_method_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.choose_equation_method_2.setMouseTracking(False)
        self.choose_equation_method_2.setStyleSheet("font: 80 11pt \"Comic Sans MS\";\n"
"color:rgb(255, 162, 199);")
        self.choose_equation_method_2.setObjectName("choose_equation_method_2")
        self.simple_iterations_button_2 = QtWidgets.QPushButton(self.page)
        self.simple_iterations_button_2.setGeometry(QtCore.QRect(0, 50, 201, 31))
        self.simple_iterations_button_2.setObjectName("simple_iterations_button_2")
        self.back_to_type_button_2 = QtWidgets.QPushButton(self.page)
        self.back_to_type_button_2.setGeometry(QtCore.QRect(0, 170, 201, 31))
        self.back_to_type_button_2.setObjectName("back_to_type_button_2")
        self.stackedWidget.addWidget(self.page)
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(210, 10, 201, 41))
        self.header_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.header_label.setStyleSheet("font: 75 25pt \"Comic Sans MS\";\n"
"color:rgb(255, 162, 199);\n"
"")
        self.header_label.setObjectName("header_label")
        self.answer_box = QtWidgets.QGroupBox(self.centralwidget)
        self.answer_box.setGeometry(QtCore.QRect(270, 60, 291, 371))
        self.answer_box.setStyleSheet("background-image: url(C:/Users/Fergie/Desktop/VM_LAB2/pink.jpg);")
        self.answer_box.setTitle("")
        self.answer_box.setObjectName("answer_box")
        self.answer_widget = QtWidgets.QFrame(self.answer_box)
        self.answer_widget.setGeometry(QtCore.QRect(20, 250, 251, 101))
        self.answer_widget.setStyleSheet("background-image: url(C:/Users/Fergie/Desktop/VM_LAB2/white.jpg);")
        self.answer_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.answer_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.answer_widget.setObjectName("answer_widget")
        self.answer_label = QtWidgets.QLabel(self.answer_widget)
        self.answer_label.setGeometry(QtCore.QRect(30, 0, 231, 101))
        self.answer_label.setObjectName("answer_label")
        self.graph_widget = QtWidgets.QWidget(self.answer_box)
        self.graph_widget.setGeometry(QtCore.QRect(10, 50, 271, 191))
        self.graph_widget.setObjectName("graph_widget")
        self.choise_factory_label_2 = QtWidgets.QLabel(self.answer_box)
        self.choise_factory_label_2.setGeometry(QtCore.QRect(70, 10, 161, 41))
        self.choise_factory_label_2.setStyleSheet("font: 50 20pt \"Comic Sans MS\";\n"
"color:rgb(255, 162, 199);\n"
"")
        self.choise_factory_label_2.setObjectName("choise_factory_label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit_X = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/paw.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit_X.setIcon(icon)
        self.actionExit_X.setObjectName("actionExit_X")
        self.menuFile.addAction(self.actionExit_X)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PawSolver ♥️"))
        self.load_button.setText(_translate("MainWindow", "Load file"))
        self.Save_button.setText(_translate("MainWindow", "Save to"))
        self.Solve_button.setText(_translate("MainWindow", "Solve"))
        self.label_prompt.setText(_translate("MainWindow", "Please enter the values [a, b] and epsion e"))
        self.prompt_a.setText(_translate("MainWindow", "a"))
        self.prompt_b.setText(_translate("MainWindow", "b"))
        self.prompt_c.setText(_translate("MainWindow", "e"))
        self.choise_factory_label.setText(_translate("MainWindow", "ChoiceFactory "))
        self.choose_equation_type_label.setText(_translate("MainWindow", "Choose the equation type:"))
        self.single_button.setText(_translate("MainWindow", "Single"))
        self.system_button.setText(_translate("MainWindow", "System"))
        self.choose_equation.setText(_translate("MainWindow", "Choose the equation:"))
        self.single_eq_1.setText(_translate("MainWindow", "x^3 + 2*x^2 - 5*x"))
        self.single_eq_2.setText(_translate("MainWindow", "3*x^2 + 5*x + 4"))
        self.single_eq_3.setText(_translate("MainWindow", "1 - 3*x + .sin(x)"))
        self.back_to_method_button.setText(_translate("MainWindow", "I wanna go back ^^"))
        self.pushButton_2.setText(_translate("MainWindow", "I wanna go home :c"))
        self.choose_equation_2.setText(_translate("MainWindow", "Choose the equation:"))
        self.system_eq_2.setText(_translate("MainWindow", "0.3 - 0.1x^2- 0.2y^2\n"
"0.7 -0.2x^2 - 0.1xy"))
        self.back_to_method_button_2.setText(_translate("MainWindow", "I wanna go back ^^"))
        self.pushButton.setText(_translate("MainWindow", "I wanna go home :c"))
        self.system_eq_3.setText(_translate("MainWindow", "3y^2+0.5x^2\n"
"sin(x)^2"))
        self.choose_equation_method.setText(_translate("MainWindow", "Choose the  meowthod:"))
        self.back_to_type_button.setText(_translate("MainWindow", "I wanna go back ^^"))
        self.chorde_btn.setText(_translate("MainWindow", "Chorde method"))
        self.newton_btn.setText(_translate("MainWindow", "Newton method"))
        self.simple_it_btn.setText(_translate("MainWindow", "Simple Iterations method"))
        self.next_btn.setText(_translate("MainWindow", "Next!"))
        self.choose_equation_method_2.setText(_translate("MainWindow", "Choose the  meowthod:"))
        self.simple_iterations_button_2.setText(_translate("MainWindow", "Simple Iterations method"))
        self.back_to_type_button_2.setText(_translate("MainWindow", "I wanna go back ^^"))
        self.header_label.setText(_translate("MainWindow", "PawSolver"))
        self.answer_label.setText(_translate("MainWindow", " Answer will be here.. Maybe.. later?.. ♥"))
        self.choise_factory_label_2.setText(_translate("MainWindow", "Solution"))
        self.menuFile.setTitle(_translate("MainWindow", "File(&F)"))
        self.actionExit_X.setText(_translate("MainWindow", "Exit(&X)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
