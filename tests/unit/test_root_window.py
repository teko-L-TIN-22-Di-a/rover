from unittest import TestCase
from spacerover import level_one

class TestSpacerover(TestCase):
    def setUp(self):
        self.root_window_pygame = level_one.LevelOne("space rover")
        
        
class TestInit(TestSpacerover):
    def test_initialize(self):
        self.assertEqual(self.root_window_pygame.window_title, "space rover")
