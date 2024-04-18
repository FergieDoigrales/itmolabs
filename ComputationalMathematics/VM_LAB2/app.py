import design1
import sys
import numpy  as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import solver
import system_solver
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtWidgets


def f1_y_positive(x, system):
    if system == 1:
        argument = (0.3 - x - 0.1 * x * x) / 0.2
        return np.sqrt(argument) if argument >= 0 else np.nan
    elif system == 2:
        argument = (x - 0.5 * x * x) / 3
        return np.sqrt(argument) if argument >= 0 else np.nan

def f1_y_negative(x, system):
    if system == 1:
        argument = (0.3 - x - 0.1 * x * x) / 0.2
        return -np.sqrt(argument) if argument >= 0 else np.nan
    elif system == 2:
        argument = (x - 0.5 * x * x) / 3
        return -np.sqrt(argument) if argument >= 0 else np.nan

def f2_y_positive(x, system):
    if system == 1:
        argument = (0.7 - 0.2 * x * x) / (1 + 0.1 * x)
        return argument
    elif system == 2:
        return np.abs(np.sin(x))

def f2_y_negative(x, system):
    if system == 1:
        argument = (0.7 - 0.2 * x * x) / (1 + 0.1 * x)
        return argument
    elif system == 2:
        return np.abs(np.sin(x))


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=55):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.updateGeometry()
    
    def plot(self, equation, a, b, param):
        if param == 1:
            equations = {
                1: "2*x^3 + 4*x^2 + 5*x",
                2: "3*x^2 + 5*x - 4",
                3:  "1 - 3*x + sin(x)",
            }
            self.x_values = np.linspace(a, b, 100)
            self.y_values = solver.f(equation, self.x_values)

            self.axes.clear()

            self.axes.plot(self.x_values, self.y_values, color='pink', label=equations.get(equation))

            self.axes.set_xlabel('x')
            self.axes.set_ylabel('f(x)')

            self.axes.grid(True)

            self.axes.axhline(0, color='black', linewidth=0.5)
            self.axes.axvline(0, color='black', linewidth=0.5)

            self.axes.legend()

            self.draw()
        elif param == 2:
            system = equation
            x_values = np.linspace(a, b, 1000)
            y1_pos = np.array([f1_y_positive(x, system) for x in x_values])
            y1_neg = np.array([f1_y_negative(x, system) for x in x_values])
            y2_pos = np.array([f2_y_positive(x, system) for x in x_values])
            y2_neg = np.array([f2_y_negative(x, system) for x in x_values])

            self.axes.clear()
            self.axes.plot(x_values, y1_pos, color='r')
            self.axes.plot(x_values, y1_neg,  color='r')
            self.axes.plot(x_values, y2_pos,  color='pink')
            self.axes.plot(x_values, y2_neg,  color='pink')
            self.axes.set_xlabel('x')
            self.axes.set_ylabel('y')
            self.axes.axhline(0, color='black', linewidth=1.5)
            self.axes.axvline(0, color='black', linewidth=1.5)
            self.axes.set_title(f'System {system}')
            self.axes.grid(True)
            self.axes.legend()  
            self.draw()


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = design1.Ui_MainWindow()
        self.main_ui.setupUi(self)  


        #получение данных
        self.a = self.main_ui.inp_a.text()
        self.b =  self.main_ui.inp_b.text()
        self.e = self.main_ui.inp_e.text()

        
        # Если графика еще нет, то создать слой
        if self.main_ui.graph_widget.layout() is None:
            layout = QtWidgets.QVBoxLayout(self.main_ui.graph_widget)  # QVBoxLayout can be changed as needed
            self.main_ui.graph_widget.setLayout(layout)
        
        self.canvas = PlotCanvas(self.main_ui.graph_widget)
        self.main_ui.graph_widget.layout().addWidget(self.canvas)  # Add the canvas to the graph_widget's layout
        

        #обработать случай нажатия на кнопку plot без выбора радиокнопки

        self.main_ui.Solve_button.clicked.connect(self.get_solve)

        
        self.main_ui.load_button.clicked.connect(self.loadFromFile)

        def connect_button(button, index):
            button.clicked.connect(lambda: self.main_ui.stackedWidget.setCurrentIndex(index))

        self.single_btn = self.main_ui.single_button
        self.system_btn = self.main_ui.system_button
        self.go_back_type_btn_2 = self.main_ui.back_to_type_button_2


        self.main_ui.next_btn.clicked.connect(lambda: self.main_ui.stackedWidget.setCurrentIndex(1))
        self.main_ui.simple_iterations_button_2.clicked.connect(lambda: self.main_ui.stackedWidget.setCurrentIndex(2))
        self.main_ui.back_to_method_button_2.clicked.connect(self.reset_radio_buttons_system_eq)
        self.main_ui.back_to_method_button.clicked.connect(self.reset_radio_buttons_single_eq)
        self.main_ui.back_to_type_button.clicked.connect(self.reset_radio_buttons_method)
        self.main_ui.pushButton_2.clicked.connect(lambda: self.main_ui.stackedWidget.setCurrentIndex(0)) #backhome
        self.main_ui.pushButton.clicked.connect(lambda: self.main_ui.stackedWidget.setCurrentIndex(0))#backhome

        connect_button(self.single_btn, 3)
        connect_button(self.system_btn, 4)
        connect_button(self.go_back_type_btn_2, 0)

    def reset_radio_buttons_single_eq(self):
        self.main_ui.single_eq_1.setChecked(False)
        self.main_ui.single_eq_2.setChecked(False)
        self.main_ui.single_eq_3.setChecked(False)
        self.main_ui.system_eq_2.setChecked(False)
        self.main_ui.system_eq_3.setChecked(False)
        self.main_ui.newton_btn.setChecked(False)
        self.main_ui.chorde_btn.setChecked(False)
        self.main_ui.simple_it_btn.setChecked(False)
        self.main_ui.stackedWidget.setCurrentIndex(3)

    def reset_radio_buttons_system_eq(self):
        self.main_ui.system_eq_2.setChecked(False)
        self.main_ui.system_eq_3.setChecked(False)
        self.main_ui.newton_btn.setChecked(False)
        self.main_ui.chorde_btn.setChecked(False)
        self.main_ui.simple_it_btn.setChecked(False)
        self.main_ui.stackedWidget.setCurrentIndex(4)

    def reset_radio_buttons_method(self):
        self.main_ui.newton_btn.setChecked(False)
        self.main_ui.chorde_btn.setChecked(False)
        self.main_ui.simple_it_btn.setChecked(False)
        self.main_ui.stackedWidget.setCurrentIndex(0)
    

    def get_selected_radio_value_single(self):
        if self.main_ui.single_eq_1.isChecked():
            self.main_ui.single_eq_1.setChecked(False)
            return '11'
        elif self.main_ui.single_eq_2.isChecked():
            self.main_ui.single_eq_2.setChecked(False)
            return '21'
        elif self.main_ui.single_eq_3.isChecked():
            self.main_ui.single_eq_3.setChecked(False)
            return '31'
        else:
            return None
        
    def get_selected_radio_value_system(self):
        if self.main_ui.system_eq_2.isChecked():
            self.main_ui.system_eq_2.setChecked(False)
            return '12'
        elif self.main_ui.system_eq_3.isChecked():
            self.main_ui.system_eq_3.setChecked(False)
            return '22'
        else:
            return None
        

    def get_selected_radio_value_method_single(self):
        if self.main_ui.chorde_btn.isChecked():
            answer = solver.chorde_method(float(self.main_ui.inp_a.text()), float(self.main_ui.inp_b.text()), int((self.get_selected_radio_value_single())[0]), float(self.main_ui.inp_e.text()))
        elif self.main_ui.newton_btn.isChecked():
            answer = solver.newton_method(float(self.main_ui.inp_a.text()), float(self.main_ui.inp_b.text()), int((self.get_selected_radio_value_single())[0]), float(self.main_ui.inp_e.text()))
        elif self.main_ui.simple_it_btn.isChecked():
            answer = solver.iteration_method_single(float(self.main_ui.inp_a.text()), float(self.main_ui.inp_b.text()), int((self.get_selected_radio_value_single())[0]), float(self.main_ui.inp_e.text()))
        
        if len(answer) == 3:
            self.main_ui.answer_label.setText("Vector х: " + str(answer[0]) + "\n\n" + "Derivative f'(х): " + str(answer[1]) + "\n\n" + "Iterations: " + str(answer[2]))
        else:
            self.main_ui.answer_label.setText(str(answer))

    def get_selected_radio_value_method_system(self):
        if self.main_ui.system_eq_2.isChecked():
            answer = system_solver.simple_iteration_method(float(self.main_ui.inp_a.text()), float(self.main_ui.inp_b.text()), int((self.get_selected_radio_value_system())[0]), float(self.main_ui.inp_e.text()))
        elif self.main_ui.system_eq_3.isChecked():
            answer = system_solver.simple_iteration_method(float(self.main_ui.inp_a.text()), float(self.main_ui.inp_b.text()), int((self.get_selected_radio_value_system())[0]), float(self.main_ui.inp_e.text()))

            self.main_ui.answer_label.setText("Vector х: " + str(answer[0]) + "\n\n" + "Derivative f'(х): " + str(answer[1]) + "\n\n" + "Iterations: " + str(answer[2]))
        
        if len(answer) == 5:
            self.main_ui.answer_label.setText("Vector х: " + str(answer[0]) + "\n" + "Vector y: " + str(answer[1]) + "\n" + "Iterations: " + str(answer[2]) + "\n" + "Inaccuracy х: " + str(answer[3]) + "\n" + "Inaccuracy у: " + str(answer[4]))
        else:
            self.main_ui.answer_label.setText(str(answer))

    def get_solve(self):
        try:
            if (self.main_ui.single_eq_1.isChecked() or self.main_ui.single_eq_2.isChecked() or self.main_ui.single_eq_3.isChecked() or self.main_ui.system_eq_2.isChecked() or self.main_ui.system_eq_3.isChecked()) and ( len(self.main_ui.inp_a.text()) > 0 and len(self.main_ui.inp_b.text()) > 0 and len(self.main_ui.inp_e.text()) > 0 ):
            
                if self.main_ui.stackedWidget.indexOf(self.main_ui.stackedWidget.currentWidget()) == 2:
                    self.get_selected_radio_value_method_system()
                    self.update_graph(int((self.get_selected_radio_value_system())[0]), float(self.main_ui.inp_a.text()), float(self.main_ui.inp_b.text()), int((self.get_selected_radio_value_system())[1]))
                else: 
                    self.get_selected_radio_value_method_single()
                    self.update_graph(int((self.get_selected_radio_value_single())[0]), float(self.main_ui.inp_a.text()), float(self.main_ui.inp_b.text()), int((self.get_selected_radio_value_single())[1]))
            elif not (self.main_ui.single_eq_1.isChecked() or self.main_ui.single_eq_2.isChecked() or self.main_ui.single_eq_3.isChecked() or self.main_ui.system_eq_2.isChecked() or self.main_ui.system_eq_3.isChecked()):
                error_message = "Choose the equation radio button!"
                QMessageBox.critical(self, "Paw has error :c", error_message)
            elif not (self.main_ui.simple_it_btn.isChecked() or self.main_ui.chorde_btn.isChecked() or self.main_ui.simple_iterations_button_2.isChecked() or self.main_ui.newton_btn.isChecked()):
                error_message_method = "Choose the method radio button!"
                QMessageBox.critical(self, "Paw has an error :c", error_message_method)
            elif len(self.main_ui.inp_a.text()) < 1:
                error_message1 = "Enter value 'a'!"
                QMessageBox.critical(self, "Paw has an error :c", error_message1)      
            elif len(self.main_ui.inp_b.text()) < 1:
                error_message2 = "Enter value 'b'!"
                QMessageBox.critical(self, "Paw has an error :c", error_message2)  
            elif len(self.main_ui.inp_e.text()) < 1:
                error_message3 = "Enter value 'e'!"
                QMessageBox.critical(self, "Paw has an error :c", error_message3)  
        except:
            error_message_global = "Something went wrong.. Try again."
            QMessageBox.critical(self, "Paw has an error :c", error_message_global)

    def saveToFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "All Files (*);;Text Files (*.txt)")  # Открываем диалоговое окно для выбора файла
        if file_path:
            # Здесь можно выполнить действия с загруженным файлом, например, прочитать его содержимое
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
            # print("Выбранный файл:", file_path)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                try:
                    a, b, e = map(float, lines[:3])
                    self.main_ui.inp_a.setText(str(a))
                    self.main_ui.inp_b.setText(str(b))
                    self.main_ui.inp_e.setText(str(e))
                except ValueError:
                        error_message_value = 'Failed to read values ​​from file...'
                        QMessageBox.critical(self, "Paw has an error :c", error_message_value)


    def move_to_method(self):
        button = self.sender
        clckd_btn_info = self.menu_buttons[button]

    def update_graph(self, equation_number, a, b, param):
        self.canvas.plot(equation_number, a, b, param)


        
    

# Setup PyQt application
app = QtWidgets.QApplication(sys.argv)
main = App()
main.show()
sys.exit(app.exec_())

