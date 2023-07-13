from unittest import TestCase
from app.src.movement.controller import Controller

class Movementtest(TestCase):
    def test_controller(self):
        c = Controller(None, None)
        c.move_directional(50)