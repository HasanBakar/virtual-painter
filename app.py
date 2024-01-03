import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QHBoxLayout, QVBoxLayout,QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QProcess


class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Our Final Year Project at uctc created by Abu Bakar and Md. Didarul Alam")
        self.setGeometry(100, 100,1200, 720)
       
        self.center_window()
        self.init_ui()
    

    def center_window(self):
        # Get information about the desktop
        desktop = QDesktopWidget().screenGeometry()

        # Calculate the center position for the window
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2

        # Set the window position
        self.move(x, y)
    
    def init_ui(self):
        # Create a widget to hold the two overlay images
        overlay_widget = QWidget(self)

        # Create QLabel for the first overlay image
        overlay1_label = QLabel(overlay_widget)
        overlay1_pixmap = QPixmap("Header/abu-bakar.jpg")  # Replace with the path to your first overlay image
        overlay1_label.setPixmap(overlay1_pixmap)

        # Create QLabel for the second overlay image
        overlay2_label = QLabel(overlay_widget)
        overlay2_pixmap = QPixmap("Header/abu-bakar.jpg")  # Replace with the path to your second overlay image
        overlay2_label.setPixmap(overlay2_pixmap)

        # Create a QLabel for the heading
        heading_label = QLabel("Welcome to the Virtual Painter using Computer Vision.", self)

        # Set font and styling for the heading label
        font = QFont()
        font.setPointSize(20)  # Adjust the font size as needed
        font.setBold(True)
        heading_label.setFont(font)
        heading_label.setStyleSheet("color: #333;")  # Set the text color using CSS

        # Set alignment to bottom-right for both overlay labels
        overlay1_label.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        overlay2_label.setAlignment(Qt.AlignBottom | Qt.AlignRight)

        # Create a horizontal layout for the overlay labels
        overlay_layout = QHBoxLayout(overlay_widget)
        overlay_layout.addWidget(overlay1_label)
        overlay_layout.addWidget(overlay2_label)
        overlay_layout.setContentsMargins(0, 0, 0, 0)

        # Set the overlay widget's layout
        overlay_widget.setLayout(overlay_layout)

        # Create a QLabel for the background image
        background_label = QLabel(self)
        background_pixmap = QPixmap("Header/uctc-head-logo.jpg")  # Replace with the path to your background image
        background_label.setPixmap(background_pixmap)
        background_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Create "Run" button
        run_button = QPushButton("Run Script", self)
        run_button.clicked.connect(self.run_script)
        run_button.setStyleSheet("background-color: green; color: white;")
        run_button.setFixedSize(300, 60)
        

        # Create "Stop" button
        stop_button = QPushButton("Stop Script", self)
        stop_button.clicked.connect(self.stop_script)
        stop_button.setStyleSheet("background-color: red; color: white;")
        stop_button.setFixedSize(300, 60)
       

        # Initialize QProcess for script execution
        self.process = QProcess(self)

        # Create a vertical layout for the main window
        layout = QVBoxLayout(self)
        layout.addWidget(background_label)
        layout.addWidget(heading_label)
        # Create a layout and add the buttons to it
        layout.addWidget(run_button)
        layout.addWidget(stop_button)
        layout.addWidget(overlay_widget, alignment=Qt.AlignRight | Qt.AlignBottom)

        self.setLayout(layout)
    
    def run_script(self):
        # Define the path to your Python script
        script_path = "main.py"

        # Set the script path as the program to execute
        self.process.start("python", [script_path])

    def stop_script(self):
        # Terminate the running script
        self.process.terminate()
        sys.exit()

    def show_window(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApplication()
    my_app.show_window()
    sys.exit(app.exec_())
