from typing import Optional

from src.gui.guiactions import Clickable, Drawable
from src.utility.drawutil import DrawUtil
from src.utility.fontfactory import FontFactory, FontType


class Button(Drawable, Clickable):
    def __init__(self, text: str, x: float, y: float, width: Optional[float], height: Optional[float], centered: bool, action, size: int = 24):
        self.text = text
        self.width = width
        self.height = height
        width, height = FontFactory().font(FontType.ARIAL, size).size(self.text)
        self.x = x - width / 2 if centered else x
        self.y = y - height / 2 if centered else y
        self.action = action
        self.size = size

    def draw_screen(self, mouse_x: int, mouse_y: int, partial_ticks: float):
        width, height = FontFactory().font(FontType.ARIAL, self.size).size(self.text)
        hover_color = 0xff424242 if self._is_hovered(mouse_x, mouse_y) else 0xff212121
        if self.width and self.height:
            DrawUtil().draw_box(self.x, self.y, self.width, self.height, color=hover_color)
            DrawUtil().draw_centered_string(self.text, self.x + self.width / 2, self.y + self.height / 2, 0xffffffff, size=self.size)
        else:
            DrawUtil().draw_box(self.x, self.y, width + 20, height * 1.5, color=hover_color)
            DrawUtil().draw_centered_string(self.text, self.x + width / 2 + 10, self.y + height / 2 + 2, 0xffffffff, size=self.size)

    def mouse_clicked(self, mouse_x: int, mouse_y: int, mouse_button: int):
        if self._is_hovered(mouse_x, mouse_y):
            self.action()

    def _is_hovered(self, mouse_x, mouse_y) -> bool:
        width, height = FontFactory().font(FontType.ARIAL, self.size).size(self.text)
        if self.width and self.height:
            return DrawUtil().is_hovered(mouse_x, mouse_y, self.x, self.y, self.width, self.height)
        else:
            return DrawUtil().is_hovered(mouse_x, mouse_y, self.x, self.y, width + 20, height * 1.5)
