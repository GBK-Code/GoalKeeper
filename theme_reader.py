import json
import os


def get_themes():
    themes = {}
    for theme in os.listdir("themes"):
        with open(f"themes/{theme}", "r") as file:
            themes[theme[:-5]] = json.load(file)

    return themes


def set_theme():
    with open("config.json", "r") as config:
        return json.load(config)["theme"]
