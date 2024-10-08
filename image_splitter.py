import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QFileDialog, QScrollArea
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QRect

class ImageSplitter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Сравнение изображений')
        self.setGeometry(100, 100, 1000, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.scroll_area.setWidget(self.image_label)
        main_layout.addWidget(self.scroll_area)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.update_image)
        main_layout.addWidget(self.slider)

        button_layout = QHBoxLayout()
        self.open_left_button = QPushButton('Открыть левое изображение', self)
        self.open_left_button.clicked.connect(lambda: self.open_image('left'))
        button_layout.addWidget(self.open_left_button)

        self.open_right_button = QPushButton('Открыть правое изображение', self)
        self.open_right_button.clicked.connect(lambda: self.open_image('right'))
        button_layout.addWidget(self.open_right_button)

        main_layout.addLayout(button_layout)

        self.left_image = None
        self.right_image = None

    def open_image(self, side):
        file_name, _ = QFileDialog.getOpenFileName(self, f'Открыть {"левое" if side == "left" else "правое"} изображение', '', 'Image Files (*.png *.jpg *.bmp)')
        if file_name:
            if side == 'left':
                self.left_image = QPixmap(file_name)
            else:
                self.right_image = QPixmap(file_name)
            self.update_image()

    def update_image(self):
        if self.left_image and self.right_image:
            max_width = max(self.left_image.width(), self.right_image.width())
            max_height = max(self.left_image.height(), self.right_image.height())
            result = QPixmap(max_width, max_height)
            result.fill(Qt.transparent)
            painter = QPainter(result)

            split_position = int(self.slider.value() * max_width / 100)

            # Отрисовка левого изображения
            painter.drawPixmap(QRect(0, 0, split_position, self.left_image.height()), self.left_image, 
                               QRect(0, 0, split_position, self.left_image.height()))

            # Отрисовка правого изображения
            painter.drawPixmap(QRect(split_position, 0, max_width - split_position, self.right_image.height()),
                               self.right_image,
                               QRect(split_position, 0, self.right_image.width() - split_position, self.right_image.height()))

            # Отрисовка разделительной линии
            painter.setPen(Qt.white)
            painter.drawLine(split_position, 0, split_position, max_height)

            painter.end()
            self.image_label.setPixmap(result)
            self.image_label.setFixedSize(result.size())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageSplitter()
    ex.show()
    sys.exit(app.exec_())