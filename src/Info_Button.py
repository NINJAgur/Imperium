import os
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

class Info_Button(Button):
    def __init__(self, parent_widget, **kwargs):
        super(Info_Button, self).__init__(**kwargs)
        self.scrlv_info =ScrollView(size_hint=(0.5, 0.5), pos=(parent_widget.width / 3, parent_widget.height / 3))
        self.parent_widget = parent_widget
        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

    def on_press(self):
        sound = SoundLoader.load('assets/audio/scrollview_click.mp3')
        sound.play()

    def on_release(self):
        if self.layout.children == [] :
            self.scrlv_info.clear_widgets()

            self.layout.add_widget(Button(size_hint_y=None, height=500, background_normal= os.path.join('assets', 'images', '62_explanation1.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=500, background_normal= os.path.join('assets', 'images', '63_explanation2.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=500, background_normal= os.path.join('assets', 'images', '64_explanation3.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=800, background_normal= os.path.join('assets', 'images', '65_explanation4.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=600, background_normal= os.path.join('assets', 'images', '66_explanation5.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=800, background_normal= os.path.join('assets', 'images', '67_explanation6.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=500, background_normal= os.path.join('assets', 'images', '68_explanation7.png')))
            self.layout.add_widget(Button(size_hint_y=None, height=500, background_normal= os.path.join('assets', 'images', '69_explanation8.png')))
            self.scrlv_info.add_widget(self.layout)
            self.parent_widget.add_widget(self.scrlv_info)

        else :
            self.parent_widget.remove_widget(self.scrlv_info)
            self.layout.clear_widgets()

    def scroll_change(self, scrlv, instance, value):
        scrlv.scroll_y = value

    def slider_change(self, s, instance, value):
        if value >= 0:  # this to avoid 'maximum recursion depth exceeded' error
            s.value = value