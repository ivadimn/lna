from PyQt6.QtCore import QObject
from PyQt6.QtGui import QAction, QIcon
from resources.main_res import Event


class Action(QAction):

    def __init__(self, event: Event, parent: QObject) -> None:
        super().__init__(QIcon(event.icon), event.title, parent)
        self.setStatusTip(event.status_tip)



