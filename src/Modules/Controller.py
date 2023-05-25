from Resources.Root import root

class Controller:
    def __init__(self):
        return

    def set_key(self,window : str, key : str, method : str):
        keyphrase = f"<{key}>"
        window.bind(keyphrase, method)

    def set_default_keys(self, sprite :str):
        self.set_key(root, 'w', lambda  event: sprite.move_directional(-10))
        self.set_key(root, 's', lambda  event: sprite.move_directional(10))
        self.set_key(root, 'a', lambda  event: sprite.rotate(10))
        self.set_key(root, 'd', lambda  event: sprite.rotate(-10))