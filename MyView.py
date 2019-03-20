from PyQt5.QtCore import (QRectF, qsrand, Qt, QTime)
from PyQt5.QtGui import (QBrush, QLinearGradient, QPainter, QPen, QRadialGradient, QColor)
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView)

SCREEN_HEIGHT_BORDER = 160
SCREEN_WIDTH_BORDER = 120


class Field:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.letter = chr(c + ord('A') - 1)


class Board:
    def __init__(self):
        self.fields = []
        for r in range(1, 9):
            fields_row = []
            for c in range(1, 9):
                fields_row.append(Field(r, c))
            self.fields.append(fields_row)


class Node(QGraphicsItem):
    Type = QGraphicsItem.UserType + 1

    def __init__(self, graph_widget):
        super().__init__()

        self.graph = graph_widget

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(1)

    def type(self):
        return Node.Type

    def boundingRect(self):
        # adjust = 2.0
        adjust = 0.0
        ball_size = 50
        return QRectF(-ball_size - adjust, -ball_size - adjust, 2*ball_size + adjust, 2 * ball_size + adjust)

    def paint(self, painter, option, widget):
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGray)
        ball_size = 50
        painter.drawRect(-ball_size, -ball_size, ball_size, ball_size)
        painter.drawEllipse(-7, -7, ball_size, ball_size)

        gradient = QRadialGradient(-3, -3, 10)
        gradient.setColorAt(0, Qt.yellow)
        gradient.setColorAt(1, Qt.darkYellow)

        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(Qt.black, 0))
        painter.drawEllipse(-10, -10, ball_size, ball_size)

    def mousePressEvent(self, event):
        self.update()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.update()
        super().mouseReleaseEvent(event)


class GraphWidget(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.timerId = 0

        size = self.size()
        width_border = SCREEN_HEIGHT_BORDER
        height_border = SCREEN_HEIGHT_BORDER
        board_start_x = 2
        board_start_y = 2
        board_width = (size.width() - width_border) / 4 * 3
        board_height = size.height() - height_border

        x = board_start_x
        y = board_start_y
        x_diff = int((board_width - 2 * x) / 8)
        y_diff = int((board_height - 2 * y) / 8)

        scene = QGraphicsScene(self)
        view = QGraphicsView(scene)
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        # scene.setSceneRect(-900, -900, 900, 900)
        scene.setSceneRect(scene.itemsBoundingRect())
        # scene.setSceneRect(QRectF(0, 0, 3000, 2400))
        view.setSceneRect(scene.sceneRect())
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        corn_silk_color = QColor(255, 248, 220)
        saddle_brown_color = QColor(139, 69, 19)
        antique_white_color = QColor(250, 235, 215)
        scene.addRect(0, 0, 50, 50, corn_silk_color)
        scene.addRect(110, 110, 50, 50, saddle_brown_color)
        scene.addRect(50, 50, 90, 90, saddle_brown_color)
        scene.addRect(x, y, board_width - x, board_height - y, corn_silk_color)
        board = Board()
        for fields_row in reversed(board.fields):
            for field in fields_row:
                field_color = antique_white_color if (field.c + field.r) % 2 else saddle_brown_color
                scene.addRect(x, y, x_diff, y_diff, field_color)
                x += x_diff
            y += y_diff
            x = board_start_x

        node1 = Node(self)
        scene.addItem(node1)
        node1.setPos(-210, -520)

        self.scale(0.8, 0.8)
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Elastic Nodes")

    # def itemMoved(self):
    #     if not self.timerId:
    #         self.timerId = self.startTimer(1000 / 25)

    def keyPressEvent(self, event):
        key = event.key()

        super(GraphWidget, self).keyPressEvent(event)

    # def drawBackground(self, painter, rect):
    #     # Shadow.
    #     sceneRect = self.sceneRect()
    #     rightShadow = QRectF(sceneRect.right(), sceneRect.top() + 5, 5,
    #                          sceneRect.height())
    #     bottomShadow = QRectF(sceneRect.left() + 5, sceneRect.bottom(),
    #                           sceneRect.width(), 5)
    #     if rightShadow.intersects(rect) or rightShadow.contains(rect):
    #         painter.fillRect(rightShadow, Qt.darkGray)
    #     if bottomShadow.intersects(rect) or bottomShadow.contains(rect):
    #         painter.fillRect(bottomShadow, Qt.darkGray)
    #
    #     # Fill.
    #     gradient = QLinearGradient(sceneRect.topLeft(), sceneRect.bottomRight())
    #     gradient.setColorAt(0, Qt.white)
    #     gradient.setColorAt(1, Qt.lightGray)
    #     painter.fillRect(rect.intersected(sceneRect), QBrush(gradient))
    #     painter.setBrush(Qt.NoBrush)
    #     painter.drawRect(sceneRect)

        # Text.
        # textRect = QRectF(sceneRect.left() + 4, sceneRect.top() + 4,
        #                   sceneRect.width() - 4, sceneRect.height() - 4)
        # message = "Click and drag the nodes around, and zoom with the " \
        #           "mouse wheel or the '+' and '-' keys"
        #
        # font = painter.font()
        # font.setBold(True)
        # font.setPointSize(14)
        # painter.setFont(font)
        # painter.setPen(Qt.lightGray)
        # painter.drawText(textRect.translated(2, 2), message)
        # painter.setPen(Qt.black)
        # painter.drawText(textRect, message)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    qsrand(QTime(0, 0, 0).secsTo(QTime.currentTime()))

    widget = GraphWidget()
    widget.show()

    sys.exit(app.exec_())
