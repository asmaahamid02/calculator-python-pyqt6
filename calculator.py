from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit,QVBoxLayout, QMainWindow, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt
import sys

class Calculator(QMainWindow):      
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 450)
        self.setMinimumHeight(450)
        self.setMinimumWidth(400)

        self.central_widget = QWidget()
        self.central_widget.setStyleSheet('background-color: #000000;')
        self.setCentralWidget(self.central_widget)

        self.app_layout = QVBoxLayout()
        self.central_widget.setLayout(self.app_layout)

        self.create_input()
        self.create_buttons()

    def create_input(self):
        self.input = QLineEdit()
        self.input.setReadOnly(True)
        self.input.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input.setFixedHeight(100)    
        self.input.setPlaceholderText('0')
        self.input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.input.setStyleSheet('font-size: 36px; padding: 10px 5px; font-weight: bold;border:none')
        self.app_layout.addWidget(self.input)

    def create_buttons(self):    
        buttons = [
            'C' , 'Del', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='                    
        ]            

        grid_layout = QGridLayout()

        row = 0
        col = 0
        rowSpan = 1
        colSpan = 1

        for button_text in buttons:
            style = 'font-size: 20px; padding: 10px; border-radius: 20px; margin: 3px 2px; background-color: #313131; color: white;'
            button = QPushButton(button_text)

            if button_text in  ['/', '*', '-', '+', '=']:
                button.setStyleSheet(f'{style} background-color: #F78E01; color: white;')
            elif button_text in ['C', 'Del']:
                button.setStyleSheet(f'{style} background-color: #A1A1A1; color: black;')
            else:
                button.setStyleSheet(style)    
                
            button.clicked.connect(self.click_handler)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

            if button_text in ['C', '=']:
                colSpan = 2
            else:
                colSpan = 1

            grid_layout.addWidget(button, row, col, rowSpan, colSpan)

            col += colSpan

            if col >= 4:
                col = 0
                row += 1

        self.app_layout.addLayout(grid_layout)
        

    def click_handler(self):
        button_instance = self.sender()
        button_text =  button_instance.text()
        input_text = self.input.text()

        if input_text == 'Error':
            self.input.clear()
            input_text = ''

        #validation

        #prevent adding some operators at the beginning
        if input_text == '' and button_text in ['/', '*', 'C', 'Del', '.', '=', '+']:
            return
        
        #prevent adding multiple operators
        if button_text in ['/', '*', '-', '+', '=', '.'] and input_text and input_text[-1] in ['/', '*', '-', '+', '.']:
            return   

        if button_text == '=':
            try:
                result = eval(input_text)
                self.input.setText(str(result))
            except Exception as error:
                self.input.setText(f"Error") 
        elif button_text == 'C':
            self.input.clear()
        elif button_text == 'Del':
           self.input.setText(input_text[:-1])
        else:
            self.input.setText(input_text + button_text)   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()

    sys.exit(app.exec())


