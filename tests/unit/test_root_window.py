from unittest import TestCase
from spacerover import root_window_pygame

class TestSpacerover(TestCase):
    def setUp(self):
        self.root_window_pygame = root_window_pygame.RootWindowPyGame("space rover")
        
        
class TestInit(TestSpacerover):
    def test_initialize(self):
        self.assertEqual(self.root_window_pygame.window_title, "space rover")

class TestAccelerate(TestSpacerover):
    def test_accelerate_from_zero(self):
        0

class TestBrake(TestSpacerover):
    0