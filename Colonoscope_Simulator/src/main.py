import sys
import time
import serial

from PySide6.QtWidgets import QApplication, QGraphicsView
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, Signal, QObject

from pynput import keyboard

from scene import ColonoscopeScene
from controller import Controller


# --------------------------------------------------
# THREAD-SAFE SIGNAL BRIDGE
# --------------------------------------------------
class InputBridge(QObject):
    key_signal = Signal(str)


class MainWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        # -----------------------------
        # Visualization setup
        # -----------------------------
        self.scene = ColonoscopeScene()
        self.setScene(self.scene)

        self.controller = Controller(self.scene)

        self.setWindowTitle("Colonoscope Simulator")
        self.setFixedSize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)

        # -----------------------------
        # Serial connection
        # -----------------------------
        self.arduino = serial.Serial("COM3", 115200, timeout=1)
        time.sleep(2)  # allow Arduino reset
        print("Arduino connected")

        # -----------------------------
        # Thread-safe input bridge
        # -----------------------------
        self.bridge = InputBridge()
        self.bridge.key_signal.connect(self.handle_input)

        # -----------------------------
        # Global keyboard listener
        # -----------------------------
        self.listener = keyboard.Listener(on_press=self.on_global_key)
        self.listener.start()
        print("Global keyboard listener started")

    # --------------------------------------------------
    # CENTRAL INPUT HANDLER (Qt main thread)
    # --------------------------------------------------
    def handle_input(self, key_char):
        """
        This function is ALWAYS executed in the Qt main thread.
        It safely updates:
        - visualization
        - Arduino hardware
        """

        if key_char == 'a':
            self.controller.rotate_left()
            self.arduino.write(b'a')
            print("LEFT")

        elif key_char == 'd':
            self.controller.rotate_right()
            self.arduino.write(b'd')
            print("RIGHT")

        elif key_char == 'r':
            self.arduino.write(b'r')
            print("RESET")

    # --------------------------------------------------
    # Global keyboard callback (background thread)
    # --------------------------------------------------
    def on_global_key(self, key):
        try:
            char = key.char.lower()
            self.bridge.key_signal.emit(char)
        except AttributeError:
            pass  # ignore special keys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
