import design
import solver
import validator
import sys
from PyQt5 import QtWidgets
import numpy  as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.optimize import fsolve
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout



class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = design.Ui_MainWindow()
        self.main_ui.setupUi(self)  # Initialize the GUI design setup from design.py


        #получение данных
        self.a = self.main_ui.inp_a.text().replace(',','.')
        self.b =  self.main_ui.inp_b.text().replace(',','.')
        self.e = self.main_ui.inp_e.text().replace(',','.')
        self.p = self.main_ui.inp_p.text().replace(',','.')

    
        #equ = self.get_selected_radio_value_method()
        
    

        
        # # Если графика еще нет, то создать слой
        # if self.main_ui.giph_widget.layout() is None:
        #     layout = QtWidgets.QVBoxLayout(self.main_ui.giph_widget)  # QVBoxLayout can be changed as needed
        #     self.main_ui.giph_widget.setLayout(layout)

        # self.movie = QMovie("C:\Users\Fergie\Desktop\VM_LAB3\resources")
        # self.label = QLabel(self)
        # self.label.setAlignment(Qt.AlignCenter)
        # self.label.setMovie(self.movie)
        # self.movie.start()

        # self.main_ui.giph_widget.layout().addWidget(self.movie)  # Add the canvas to the graph_widget's layout
        
        if self.main_ui.giph_widget.layout() is None:
            layout = QtWidgets.QVBoxLayout(self.main_ui.giph_widget)  # QVBoxLayout можно изменить по необходимости
            self.main_ui.giph_widget.setLayout(layout)

        self.movie = QMovie("resources/dance.gif")
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMovie(self.movie)
        self.movie.start()
        self.main_ui.giph_widget.layout().addWidget(self.label)


        self.main_ui.Solve_button.clicked.connect(self.get_solve)

        self.main_ui.load_button.clicked.connect(self.loadFromFile)
        self.main_ui.Save_button.clicked.connect(self.saveToFile)

        self.main_ui.next_btn.clicked.connect(lambda: self.main_ui.stackedWidget.setCurrentIndex(1))
        self.main_ui.back_btn.clicked.connect(lambda: self.main_ui.stackedWidget.setCurrentIndex(0))

        

    def get_selected_equation_value(self):
        if self.main_ui.eq_1.isChecked():
            self.main_ui.eq_1.setChecked(False)
            return '1'
        elif self.main_ui.eq_2.isChecked():
            self.main_ui.eq_2.setChecked(False)
            return '2'
        elif self.main_ui.eq_3.isChecked():
            self.main_ui.eq_3.setChecked(False)
            return '3'
        else:
            return None

        

    def get_selected_radio_value_method(self):
        if self.main_ui.left_rect_btn.isChecked():
            answer = solver.rectangle_method_left(int(self.get_selected_equation_value()), float(self.main_ui.inp_a.text().replace(',','.')), float(self.main_ui.inp_b.text().replace(',','.')), float(self.main_ui.inp_e.text().replace(',','.')), int(float(self.main_ui.inp_p.text().replace(',','.'))))
        elif self.main_ui.center_rect_btn.isChecked():
            answer = solver.rectangle_method_centre(int(self.get_selected_equation_value()), float(self.main_ui.inp_a.text().replace(',','.')), float(self.main_ui.inp_b.text().replace(',','.')), float(self.main_ui.inp_e.text().replace(',','.')), int(float(self.main_ui.inp_p.text().replace(',','.'))))
        elif self.main_ui.right_rect_btn.isChecked():
            answer = solver.rectangle_method_right(int(self.get_selected_equation_value()), float(self.main_ui.inp_a.text().replace(',','.')), float(self.main_ui.inp_b.text().replace(',','.')), float(self.main_ui.inp_e.text().replace(',','.')), int(float(self.main_ui.inp_p.text().replace(',','.'))))
        
        elif self.main_ui.trapezoidal_btn.isChecked():
            answer = solver.trapezoidal_method(int(self.get_selected_equation_value()), float(self.main_ui.inp_a.text().replace(',','.')), float(self.main_ui.inp_b.text().replace(',','.')), float(self.main_ui.inp_e.text().replace(',','.')), int(float(self.main_ui.inp_p.text().replace(',','.'))))
        elif self.main_ui.simpson_btn.isChecked():
            answer = solver.simpson_method(int(self.get_selected_equation_value()), float(self.main_ui.inp_a.text().replace(',','.')), float(self.main_ui.inp_b.text().replace(',','.')), float(self.main_ui.inp_e.text().replace(',','.')), int(float(self.main_ui.inp_p.text().replace(',','.'))))

        if len(answer) == 3:
            self.main_ui.answer_label.setText("S: " + str(answer[0]) + "\n\n" + "Parts: " + str(answer[1]) + "\n\n" + "Inaccuracy: " + str(answer[2]))
        else:
            self.main_ui.answer_label.setText(str(answer))


    def get_solve(self):
        try:
            if (self.main_ui.eq_1.isChecked() or self.main_ui.eq_2.isChecked() or self.main_ui.eq_3.isChecked()) \
                    and (len(self.main_ui.inp_a.text().replace(',','.')) > 0 and len(self.main_ui.inp_b.text().replace(',','.')) > 0 \
                    and len(self.main_ui.inp_e.text().replace(',','.')) > 0  and len(self.main_ui.inp_p.text().replace(',','.')) > 0) \
                    and (self.main_ui.left_rect_btn.isChecked() or self.main_ui.center_rect_btn.isChecked() \
                    or self.main_ui.right_rect_btn.isChecked() or self.main_ui.simpson_btn.isChecked() \
                    or self.main_ui.trapezoidal_btn.isChecked()):
                
                a = float(self.main_ui.inp_a.text().replace(',','.'))
                b = float(self.main_ui.inp_b.text().replace(',','.'))
                e = float(self.main_ui.inp_e.text().replace(',','.'))
                p = int(float(self.main_ui.inp_p.text().replace(',','.')))
                
                if validator.check_range(a, b) == False:
                    QMessageBox.critical(self, "Paw has an error :c", "Enter valid range (a, b)!")
                elif validator.check_epsilon(e) == False:
                    QMessageBox.critical(self, "Paw has an error :c", "Enter valid epsilon value (e)!")
                elif validator.check_parts(p) == False:
                    QMessageBox.critical(self, "Paw has an error :c", "Enter valid parts value (p)!")
                else:
                    self.get_selected_radio_value_method()
            else:
                if not (self.main_ui.eq_1.isChecked() or self.main_ui.eq_2.isChecked() or self.main_ui.eq_3.isChecked()):
                    QMessageBox.critical(self, "Paw has error :c", "Choose the equation radio button!")
                elif not (self.main_ui.left_rect_btn.isChecked() or self.main_ui.center_rect_btn.isChecked() \
                        or self.main_ui.right_rect_btn.isChecked() or self.main_ui.simpson_btn.isChecked() \
                        or self.main_ui.trapezoidal_btn.isChecked()):
                    QMessageBox.critical(self, "Paw has an error :c", "Choose the method radio button!")
                elif len(self.main_ui.inp_a.text().replace(',','.')) < 1:
                    QMessageBox.critical(self, "Paw has an error :c", "Enter value 'a'!")
                elif len(self.main_ui.inp_b.text().replace(',','.')) < 1:
                    QMessageBox.critical(self, "Paw has an error :c", "Enter value 'b'!")
                elif len(self.main_ui.inp_e.text().replace(',','.')) < 1:
                    QMessageBox.critical(self, "Paw has an error :c", "Enter value 'e'!")
                elif len(self.main_ui.inp_p.text().replace(',','.')) < 1:
                    QMessageBox.critical(self, "Paw has an error :c", "Enter value 'p'!")
        except Exception as e:
            QMessageBox.critical(self, "Paw has an error :c", "Something went wrong.. Try again.")
            print(e)

    def saveToFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "All Files (*);;Text Files (*.txt)")  # Открываем диалоговое окно для выбора файла
        if file_path:
            print("Выбранный файл:", file_path)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.main_ui.answer_label.text())

    def loadFromFile(self):
        reply = QMessageBox()
        reply.setIcon(QMessageBox.Information)
        reply.setText('The values ​​must be written line by line in the file.')
        reply.setWindowTitle('Attention!')
        reply.setStandardButtons(QMessageBox.Ok)
        reply.exec_()
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose the file", "", "All Files (*);;Text Files (*.txt)")  # Открываем диалоговое окно для выбора файла
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                try:
                    a, b, e, p = map(lambda x: float(x.replace(',', '.')), lines[:4])
                    self.main_ui.inp_a.setText(str(a))
                    self.main_ui.inp_b.setText(str(b))
                    self.main_ui.inp_e.setText(str(e))
                    self.main_ui.inp_p.setText(str(p))
                except ValueError:
                    error_message_value = 'Failed to read values ​​from file...'
                    QMessageBox.critical(self, "Paw has an error :c", error_message_value)




        
    

# Setup PyQt application
app = QtWidgets.QApplication(sys.argv)
main = App()
main.show()
sys.exit(app.exec_())

