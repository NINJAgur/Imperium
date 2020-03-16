from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.togglebutton import ToggleButton


def play_sound(event) :
    sound = ObjectProperty(None, allownone=True)
    volume = NumericProperty(1.0)
    if type(event) != ToggleButton :
        sound = SoundLoader.load('../assets/audio/button_click.mp3')
        sound.play()
    else :
        sound = SoundLoader.load('../assets/audio/empire_select.mp3')
        sound.play()





