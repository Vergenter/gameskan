from reader.Ireader import Ireader
from model.image import Image
from structure.screen import Screen, ScreenResult


class SimpleReader(Ireader):
    def read(
            self, img: Image, screens: list[Screen]) -> list[ScreenResult]:
        return [screen.map(img) for screen in screens if screen.indentify(img)]
