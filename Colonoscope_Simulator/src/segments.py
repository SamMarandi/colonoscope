from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtGui import QBrush, QColor, QLinearGradient

class Segment(QGraphicsRectItem):
    def __init__(self, x, y, width, height, color, angle_factor=1.0):
        # Initialize the rectangle shape (segment of the colonoscope)
        super().__init__(0, 0, width, height)

        # Create a horizontal gradient to make the segment look cylindrical
        gradient = QLinearGradient(0, 0, width, 0)

        # Black = camera head section, otherwise grey = body tube
        if color == "black":
            gradient.setColorAt(0.0, QColor(10, 10, 10))
            gradient.setColorAt(0.5, QColor(70, 70, 70))
            gradient.setColorAt(1.0, QColor(10, 10, 10))
        else:  # Grey flexible tube
            gradient.setColorAt(0.0, QColor(120, 120, 120))
            gradient.setColorAt(0.5, QColor(230, 230, 230))
            gradient.setColorAt(1.0, QColor(120, 120, 120))

        # Apply the gradient as a brush so the segment renders with shading
        self.setBrush(QBrush(gradient))

        # Position this segment in the scene
        self.setPos(x, y)

        # Set rotation pivot at the *bottom center* of the segment
        # This makes segments bend like a real scope
        self.setTransformOriginPoint(width / 2, height)

        # Store current rotation angle and sensitivity multiplier
        self.angle = 0
        self.angle_factor = angle_factor

    def apply_rotation(self, angle):
        """
        Applies rotation to this segment.
        angle_factor scales the movement so farther segments rotate less.
        """
        self.angle = angle * self.angle_factor
        self.setRotation(self.angle)
