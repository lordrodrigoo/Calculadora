import sys
from qtpy.QtCore import QCoreApplication, QFile, QTextStream
from main_window import MainWindow
from info import Info
from display import Display
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
import qdarkstyle
from buttons import Button, ButtonsGrid





if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = MainWindow()
 
    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetVLayout(info)

    # Display
    display = Display()
    window.addWidgetVLayout(display)
    
    # Grid
    buttonsGrid = ButtonsGrid(display)
    window.VLayout.addLayout(buttonsGrid)

    # Buttons
    # buttonsGrid.addWidget(Button('7'), 0, 0)
    # buttonsGrid.addWidget(Button('8'), 0, 1)
    # buttonsGrid.addWidget(Button('9'), 0, 2)

    # buttonsGrid.addWidget(Button('4'), 1, 0)
    # buttonsGrid.addWidget(Button('5'), 1, 1)
    # buttonsGrid.addWidget(Button('6'), 1, 2)

    # buttonsGrid.addWidget(Button('1'), 2, 0)
    # buttonsGrid.addWidget(Button('2'), 2, 1)
    # buttonsGrid.addWidget(Button('3'), 2, 2)









    


    # Executa tudo
    window.ajustFixedSize()
    window.show()
    app.exec()