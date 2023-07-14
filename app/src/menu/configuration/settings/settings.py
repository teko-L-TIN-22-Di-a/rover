import json

savefile = 'app/src/menu/configuration/settings/settings.json'
settingsjson = savefile

class Settings:
    def __init__(self) -> None:
        self.keys = {}
        self.load()

    def load(self):
        with open(settingsjson, 'r') as sj:
            self.keys = json.load(sj)

    def save(self):
        with open(settingsjson, 'w') as sj:
            json.dump(self.keys, sj, indent=4)

settings = Settings()