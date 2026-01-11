class Controller:
    def __init__(self, scene):
        self.scene = scene
        self.angle = 0
        self.MAX_ANGLE = 180          # maximum allowed rotation
        self.ANGLE_STEP = 2           # degrees per key press

    def rotate_left(self):
        if self.angle > -self.MAX_ANGLE:
            self.angle -= self.ANGLE_STEP
            self.update_segments()

    def rotate_right(self):
        if self.angle < self.MAX_ANGLE:
            self.angle += self.ANGLE_STEP
            self.update_segments()

    def update_segments(self):
        # update displayed angle
        self.scene.angle_text.setPlainText(f"Angle: {self.angle:.1f}°")

        # apply rotation to each segment
        for seg in self.scene.segments:
            seg.apply_rotation(self.angle)

        # reposition seg5 above seg6
        seg6_bottom = self.scene.seg6.mapToScene(
            self.scene.seg6.rect().center().x(), 0
        )
        self.scene.seg5.setPos(
            seg6_bottom.x() - self.scene.seg5.rect().width() / 2,
            seg6_bottom.y() - self.scene.seg5.rect().height()
        )

        # reposition seg4 above seg5
        seg5_bottom = self.scene.seg5.mapToScene(
            self.scene.seg5.rect().center().x(), 0
        )
        self.scene.seg4.setPos(
            seg5_bottom.x() - self.scene.seg4.rect().width() / 2,
            seg5_bottom.y() - self.scene.seg4.rect().height()
        )

        # reposition seg3 above seg4
        seg4_bottom = self.scene.seg4.mapToScene(
            self.scene.seg4.rect().center().x(), 0
        )
        self.scene.seg3.setPos(
            seg4_bottom.x() - self.scene.seg3.rect().width() / 2,
            seg4_bottom.y() - self.scene.seg3.rect().height()
        )

        # reposition seg2 above seg3
        seg3_bottom = self.scene.seg3.mapToScene(
            self.scene.seg3.rect().center().x(), 0
        )
        self.scene.seg2.setPos(
            seg3_bottom.x() - self.scene.seg2.rect().width() / 2,
            seg3_bottom.y() - self.scene.seg2.rect().height()
        )

        # reposition seg1 above seg2
        seg2_bottom = self.scene.seg2.mapToScene(
            self.scene.seg2.rect().center().x(), 0
        )
        self.scene.seg1.setPos(
            seg2_bottom.x() - self.scene.seg1.rect().width() / 2,
            seg2_bottom.y() - self.scene.seg1.rect().height()
        )
