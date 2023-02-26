# PyQt
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetricsF
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar7(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar7, self).__init__(str(Path(__file__)))
        self.setFixedSize(80, 80)
        self.setRange(0, 100)
        self.setValue(80)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        offset = 20
        arc_rect = QRectF(self.rect().left() + offset / 2, self.rect().top() + offset / 2, self.rect().width() - offset, self.rect().height() - offset)

        arc_pen = QPen(Qt.SolidLine)
        arc_pen.setColor(QColor("#7f6ad1"))
        arc_pen.setWidth(18)
        painter.setPen(arc_pen)
        percent = self.value() / self.maximum() if self.maximum() != 0 else 0
        painter.drawArc(arc_rect, 90*16, int(percent*360*16))

        font = QFont()
        font.setPixelSize(15)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width(self.text())
        painter.drawText(int(self.width()/2-text_width/2), 45, self.text())
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRectF
# from PySide2.QtWidgets import QProgressBar
# from PySide2.QtGui import QPainter, QColor, QPen, QFont, QFontMetricsF


# class QtBoxStyleProgressBar7(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar7, self).__init__()
#         self.setFixedSize(80, 80)
#         self.setRange(0, 100)
#         self.setValue(80)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         offset = 20
#         arc_rect = QRectF(self.rect().left() + offset / 2, self.rect().top() + offset / 2, self.rect().width() - offset, self.rect().height() - offset)

#         arc_pen = QPen(Qt.SolidLine)
#         arc_pen.setColor(QColor("#7f6ad1"))
#         arc_pen.setWidth(18)
#         painter.setPen(arc_pen)
#         percent = self.value() / self.maximum() if self.maximum() != 0 else 0
#         painter.drawArc(arc_rect, 90*16, int(percent*360*16))

#         font = QFont()
#         font.setPixelSize(15)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width(self.text())
#         painter.drawText(int(self.width()/2-text_width/2), 45, self.text())
# PySide