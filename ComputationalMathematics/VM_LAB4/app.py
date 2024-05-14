import design1
import sys
import numpy  as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import solver
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtWidgets
import validator
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QLabel, QMessageBox, QFileDialog
import data_manager
import matplotlib.pyplot as plt

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=10, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.updateGeometry()

    def plot(self,
        pairs,
        linear_answer,
        sqr_answer,
        cubic_answer,
        log_answer,
        exp_answer,
        gradual_answer,
    ):
        self.axes.clear()
        min = 99999
        max = -99999
        x_values_dots = [pair[0] for pair in pairs]
        y_values_dots = [pair[1] for pair in pairs]
        for pair in pairs:
            if pair[0] <= min:
                min = pair[0]
            if pair[0] >= max:
                max = pair[0]
        x = np.linspace(min - min * 0.3, max + max * 0.3, 400)
        try:
            y_values_linear = linear_answer[7] * x + linear_answer[8]
            self.axes.plot(x, y_values_linear, label=linear_answer[2], color="#461d9f")
        except TypeError:
            pass

        try:
            y_values_sqr = sqr_answer[6] * x**2 + sqr_answer[7] * x + sqr_answer[8]
            self.axes.plot(x, y_values_sqr, label=sqr_answer[2], color="#FF5733")
        except TypeError:
            pass

        try:
            y_values_cubic = (
                cubic_answer[5] * x**3
                + cubic_answer[6] * x**2
                + cubic_answer[7] * x
                + cubic_answer[8]
            )
            plt.plot(x, y_values_cubic, label=cubic_answer[2], color="#6C5CE7")
        except TypeError:
            pass

        try:
            y_values_log = log_answer[7] * np.log(x) + log_answer[8]
            self.axes.plot(x, y_values_log, label=log_answer[2], color="#F08A5B")
        except TypeError:
            pass

        try:
            y_values_exp = exp_answer[7] * x + np.log(exp_answer[8])
            self.axes.plot(x, y_values_exp, label=exp_answer[2], color="#5F27CD")
        except TypeError:
            pass

        try:
            y_values_grad = gradual_answer[7] * np.log(x) + np.log(gradual_answer[8])
            self.axes.plot(x, y_values_grad, label=gradual_answer[2], color="000")
        except TypeError:
            pass

        self.axes.scatter(x_values_dots, y_values_dots, color="red", linewidths=1, s=4)
        # self.axes.set_title("График функций")
        self.axes.set_xlabel("x")
        self.axes.set_ylabel("f(x)")
        self.axes.grid(True)
        self.axes.axhline(0, color="black", linewidth=0.5)
        self.axes.axvline(0, color="black", linewidth=0.5)
        self.axes.legend(fontsize=4)
        self.axes.tick_params(axis='both', which='major', labelsize=4)

        self.draw()
        # if param == 1:
        #     equations = {
        #         1: "2*x^3 + 4*x^2 + 5*x",
        #         2: "3*x^2 + 5*x - 4",
        #         3:  "1 - 3*x + sin(x)",
        #     }
        #     self.x_values = np.linspace(a, b, 100)
        #     self.y_values = solver.f(equation, self.x_values)

        #     self.axes.clear()

        #     self.axes.plot(self.x_values, self.y_values, color='pink', label=equations.get(equation))

        #     self.axes.set_xlabel('x')
        #     self.axes.set_ylabel('f(x)')

        #     self.axes.grid(True)

        #     self.axes.axhline(0, color='black', linewidth=0.5)
        #     self.axes.axvline(0, color='black', linewidth=0.5)

        #     self.axes.legend()

        #     self.draw()
        # elif param == 2:
        #     system = equation
        #     x_values = np.linspace(a, b, 1000)
        #     # y1_pos = np.array([f1_y_positive(x, system) for x in x_values])
        #     # y1_neg = np.array([f1_y_negative(x, system) for x in x_values])
        #     # y2_pos = np.array([f2_y_positive(x, system) for x in x_values])
        #     # y2_neg = np.array([f2_y_negative(x, system) for x in x_values])

        #     # self.axes.clear()
        #     # self.axes.plot(x_values, y1_pos, color='r')
        #     # self.axes.plot(x_values, y1_neg,  color='r')
        #     # self.axes.plot(x_values, y2_pos,  color='pink')
        #     # self.axes.plot(x_values, y2_neg,  color='pink')
        #     self.axes.set_xlabel('x')
        #     self.axes.set_ylabel('y')
        #     self.axes.axhline(0, color='black', linewidth=1.5)
        #     self.axes.axvline(0, color='black', linewidth=1.5)
        #     self.axes.set_title(f'System {system}')
        #     self.axes.grid(True)
        #     self.axes.legend()  
        #     self.draw()


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = design1.Ui_MainWindow()
        self.main_ui.setupUi(self)  

        # self.pair_values = [[getattr(self.main_ui, f'pair_{i}').text(), getattr(self.main_ui, f'pair_{i+1}').text()] for i in range(1, 13, 2)]


        
        # Если графика еще нет, то создать слой
        if self.main_ui.graph_widget.layout() is None:
            layout = QtWidgets.QVBoxLayout(self.main_ui.graph_widget)  # QVBoxLayout can be changed as needed
            self.main_ui.graph_widget.setLayout(layout)
        
        self.canvas = PlotCanvas(self.main_ui.graph_widget)
        self.main_ui.graph_widget.layout().addWidget(self.canvas)  # Add the canvas to the graph_widget's layout


        self.main_ui.Solve_button.clicked.connect(self.get_solve)

        self.main_ui.load_button.clicked.connect(self.loadFromFile)
        self.main_ui.Save_button.clicked.connect(self.saveToFile)



    def get_solve(self):
        try:         
            self.pair_values = [getattr(self.main_ui, f'pair_{i}').text() for i in range(1, 13)]
            self.pairs = data_manager.get_pairs(self.pair_values) #если значение не числовое - строка удаляется.
            # print(self.pair_values)
            # print(self.pairs)
            if self.pairs == "There are less than 8 valid pairs, cannot solve approximation":
                QMessageBox.critical(self, "Paw has an error :c", "There are less than 8 valid pairs, cannot solve approximation")
            else:
                answer = solver.approximation(self.pairs)
                best_answer  = answer[0]  
                answer_total = f"delta: {best_answer[0]}\nS: {best_answer[1]}\nphi(x): {best_answer[2]}\nP(x): {best_answer[3]}\nei: {best_answer[4]}\nR: {best_answer[5]}\np_i: {best_answer[6]}\na: {best_answer[7]}  b: {best_answer[8]}"
                self.main_ui.answer_label.setText(answer_total)
                self.canvas.plot(self.pairs, answer[0], answer[1], answer[2], answer[3], answer[4], answer[5])
            # if len(answer) == 3:
            #     self.main_ui.answer_label.setText("S: " + str(answer[0]) + "\n\n" + "Parts: " + str(answer[1]) + "\n\n" + "Inaccuracy: " + str(answer[2]))
            # else:
            #     self.main_ui.answer_label.setText(str(answer))

            # if len(self.pairs):
                
            #     a = float(self.main_ui.inp_a.text().replace(',','.'))
            #     b = float(self.main_ui.inp_b.text().replace(',','.'))
            #     e = float(self.main_ui.inp_e.text().replace(',','.'))
            #     p = int(float(self.main_ui.inp_p.text().replace(',','.')))
                
            #     if validator.check_range(a, b) == False:
            #         QMessageBox.critical(self, "Paw has an error :c", "Enter valid range (a, b)!")
            #     elif validator.check_epsilon(e) == False:
            #         QMessageBox.critical(self, "Paw has an error :c", "Enter valid epsilon value (e)!")
            #     elif validator.check_parts(p) == False:
            #         QMessageBox.critical(self, "Paw has an error :c", "Enter valid parts value (p)!")
            #     else:
            #         self.get_selected_radio_value_method()
            # else:
            #     if not (self.main_ui.eq_1.isChecked() or self.main_ui.eq_2.isChecked() or self.main_ui.eq_3.isChecked()):
            #         QMessageBox.critical(self, "Paw has error :c", "Choose the equation radio button!")
            #     elif not (self.main_ui.left_rect_btn.isChecked() or self.main_ui.center_rect_btn.isChecked() \
            #             or self.main_ui.right_rect_btn.isChecked() or self.main_ui.simpson_btn.isChecked() \
            #             or self.main_ui.trapezoidal_btn.isChecked()):
            #         QMessageBox.critical(self, "Paw has an error :c", "Choose the method radio button!")
            #     elif len(self.main_ui.inp_a.text().replace(',','.')) < 1:
            #         QMessageBox.critical(self, "Paw has an error :c", "Enter value 'a'!")
            #     elif len(self.main_ui.inp_b.text().replace(',','.')) < 1:
            #         QMessageBox.critical(self, "Paw has an error :c", "Enter value 'b'!")
            #     elif len(self.main_ui.inp_e.text().replace(',','.')) < 1:
            #         QMessageBox.critical(self, "Paw has an error :c", "Enter value 'e'!")
            #     elif len(self.main_ui.inp_p.text().replace(',','.')) < 1:
            #         QMessageBox.critical(self, "Paw has an error :c", "Enter value 'p'!")
        except Exception as e:
            QMessageBox.critical(self, "Paw has an error :c", "Something went wrong.. Try again.")
            print(e)


    def saveToFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "All Files (*);;Text Files (*.txt)")  # Открываем диалоговое окно для выбора файла
        if file_path:
            print("Выбранный файл:", file_path)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.main_ui.answer_label.text())

    # def loadFromFile(self):
    #     reply = QMessageBox()
    #     reply.setIcon(QMessageBox.Information)
    #     reply.setText('The values ​​must be written line by line in the file.')
    #     reply.setWindowTitle('Attention!')
    #     reply.setStandardButtons(QMessageBox.Ok)
    #     reply.exec_()
    #     file_path, _ = QFileDialog.getOpenFileName(self, "Choose the file", "", "All Files (*);;Text Files (*.txt)")  # Открываем диалоговое окно для выбора файла
    #     if file_path:
    #         with open(file_path, 'r', encoding='utf-8') as file:
    #             lines = file.readlines()
    #             try:
    #                 a, b, e, p = map(lambda x: float(x.replace(',', '.')), lines[:4])
    #                 self.main_ui.inp_a.setText(str(a))
    #                 self.main_ui.inp_b.setText(str(b))
    #                 self.main_ui.inp_e.setText(str(e))
    #                 self.main_ui.inp_p.setText(str(p))
    #             except ValueError:
    #                 error_message_value = 'Failed to read values ​​from file...'
    #                 QMessageBox.critical(self, "Paw has an error :c", error_message_value)
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
                    pairs = [list(map(lambda x: float(x.replace(',', '.')), line.split())) for line in lines[:12]]
                    for i, pair in enumerate(pairs, 1):
                        getattr(self.main_ui, f'pair_{i}').setText(' '.join(map(str, pair)))
                except ValueError:
                    error_message_value = 'Failed to read values ​​from file...'
                    QMessageBox.critical(self, "Paw has an error :c", error_message_value)




        

app = QtWidgets.QApplication(sys.argv)
main = App()
main.show()
sys.exit(app.exec_())
