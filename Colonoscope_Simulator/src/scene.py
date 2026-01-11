from PySide6.QtWidgets import QGraphicsScene, QGraphicsTextItem
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from segments import Segment

class ColonoscopeScene(QGraphicsScene):
    def __init__(self):
        super().__init__(0, 0, 800, 600)

        # base segment (does not rotate)
        self.seg6 = Segment(380, 440, 40, 80, "black", angle_factor=0)

        # mid segments (increasing flexibility upward)
        self.seg5 = Segment(380, 360, 40, 80, "black", angle_factor=0.2)
        self.seg4 = Segment(380, 280, 40, 80, "black", angle_factor=0.4)
        self.seg3 = Segment(380, 200, 40, 80, "black", angle_factor=0.6)
        self.seg2 = Segment(380, 120, 40, 80, "black", angle_factor=0.8)

        # tip segment (rotates the most)
        self.seg1 = Segment(380, 40, 40, 80, "gray", angle_factor=1.0)

        # list for easy iteration
        self.segments = [self.seg6, self.seg5, self.seg4, self.seg3, self.seg2, self.seg1]

        # angle display text
        self.angle_text = QGraphicsTextItem("Angle: 0°")
        self.angle_text.setDefaultTextColor(Qt.white)
        self.angle_text.setFont(QFont("Arial", 16))
        self.angle_text.setPos(10, 10)
        self.addItem(self.angle_text)

        # add all segment graphics to scene
        for seg in self.segments:
            self.addItem(seg)
