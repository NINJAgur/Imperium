from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.videoplayer import VideoPlayer

from src.Audio_Button import *
from src.Sound_Effect import play_sound
from src.constants import *


class MainMenu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))
        img = Image(source=os.path.join('assets', 'images', 'rome.png'), allow_stretch=True, keep_ratio=False,
                    size=(GetSystemMetrics(0), GetSystemMetrics(1)))
        logo = Image(source=os.path.join('assets', 'images', 'imperium_logo.png'), pos_hint={"x": 0.25, "top": 1.1},
                     allow_stretch=True, size_hint=(0.5, 0.5))
        play_button = Button(size_hint=(0.3, 0.1), pos_hint={"x": 0.35, "top": 0.7},
                             background_normal=os.path.join('assets', 'images', '2_play_u.png'),
                             background_down=os.path.join('assets', 'images', '1_play_d.png'), on_press=play_sound,
                             on_release=self.init_Selection)
        tutorial_button = Button(size_hint=(0.2, 0.08), pos_hint={"x": 0.4, "top": 0.5},
                                 background_normal=os.path.join('assets', 'images', '12_settings_u.png'),
                                 background_down=os.path.join('assets', 'images', '11_settings_d.png'),
                                 on_release=self.init_Tutorial, on_press=play_sound)
        self.audio = MenuAudioButton(size_hint=(0.2, 0.08), pos_hint={"x": 0.4, "top": 0.4},
                                     background_normal=os.path.join('assets', 'images', '22_audio_u.png'),
                                     background_down=os.path.join('assets', 'images', '21_audio_d.png'))
        quit = Button(size_hint=(0.2, 0.08), pos_hint={"x": 0.4, "top": 0.3},
                      background_normal=os.path.join('assets', 'images', '14_quit_u.png'),
                      background_down=os.path.join('assets', 'images', '13_quit_d.png'), on_press=play_sound,
                      on_release=self.exit)
        version = Label(size_hint=(0.2, 0.08), pos_hint={"x": 0.4, "top": 0.8},
                        text='IMPERIUM BETA 0.9 - SOUND AND SOUNDTRACK!')
        self.audio.sound.play()
        self.add_widget(img)
        self.add_widget(logo)
        self.add_widget(version)
        self.add_widget(play_button)
        self.add_widget(tutorial_button)
        self.add_widget(self.audio)
        self.add_widget(quit)

    def init_Selection(self, _):
        self.manager.current = 'Selection screen'
        self.manager.transition.direction = 'left'
        self.audio.sound.stop()

    def init_Tutorial(self, _):
        self.manager.current = 'Tutorial'
        self.manager.transition.direction = 'left'
        self.audio.sound.stop()

    def exit(self, _):
        App.get_running_app().stop()


class Selection(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))
        img = Image(source=os.path.join('assets', 'images', 'rome.png'), allow_stretch=True, keep_ratio=False,
                    size=(GetSystemMetrics(0), GetSystemMetrics(1)))
        self.add_widget(img)
        self.rome_button = ToggleButton(background_normal=os.path.join('assets', 'images', 'rome_symbol.png'),
                                        background_down=os.path.join('assets', 'images', 'rome_symbol_d.png'),
                                        size_hint=(.18, .3),
                                        pos=(GetSystemMetrics(0) / 9, (GetSystemMetrics(1) * 2) / 3),
                                        on_press=play_sound)
        self.rome_button.bind(on_release=self.init_Game)

        self.carthage_button = ToggleButton(background_normal=os.path.join('assets', 'images', 'carthage_symbol.png'),
                                            background_down=os.path.join('assets', 'images', 'carthage_symbol_d.png'),
                                            size_hint=(.18, .3),
                                            pos=(GetSystemMetrics(0) / 2.4, (GetSystemMetrics(1) * 2) / 3),
                                            on_press=play_sound)
        self.carthage_button.bind(on_release=self.init_Game)

        self.egypt_button = ToggleButton(background_normal=os.path.join('assets', 'images', 'egypt_symbol.png'),
                                         background_down=os.path.join('assets', 'images', 'egypt_symbo_d.png'),
                                         size_hint=(.18, .3),
                                         pos=(GetSystemMetrics(0) / 1.4, (GetSystemMetrics(1) * 2) / 3),
                                         on_press=play_sound)
        self.egypt_button.bind(on_release=self.init_Game)

        expl1 = Image(source=os.path.join('assets', 'images', '15_rome.png'), pos_hint={"x": 0.05, "top": 0.6},
                      allow_stretch=True, size_hint=(0.3, 0.5))
        expl2 = Image(source=os.path.join('assets', 'images', '16_carthage.png'), pos_hint={"x": 0.35, "top": 0.6},
                      allow_stretch=True, size_hint=(0.3, 0.5))
        expl3 = Image(source=os.path.join('assets', 'images', '17_egypt.png'), pos_hint={"x": 0.65, "top": 0.6},
                      allow_stretch=True, size_hint=(0.3, 0.5))

        self.add_widget(expl1)
        self.add_widget(expl2)
        self.add_widget(expl3)
        self.add_widget(self.rome_button)
        self.add_widget(self.carthage_button)
        self.add_widget(self.egypt_button)

    def init_Game(self, _):
        game_screen = self.manager.get_screen('Imperium')
        if self.rome_button.state == 'down':
            game_screen.initialize("Rome")
        elif self.carthage_button.state == 'down':
            game_screen.initialize("Carthage")
        else:
            game_screen.initialize("Egypt")

        self.manager.current = 'Imperium'
        self.manager.transition.direction = 'left'


class Tutorial(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))
        img = Image(source=os.path.join('assets', 'images', 'rome.png'), allow_stretch=True, keep_ratio=False,
                    size=(GetSystemMetrics(0), GetSystemMetrics(1)))
        unit_movement = Button(size_hint=(0.3, 0.1), pos_hint={"x": 0.35, "top": 0.8}, text='Unit Movement',
                               background_normal=os.path.join('assets', 'images', '57_header.png'),
                               background_down=os.path.join('assets', 'images', '57_header_d.png'), on_press=play_sound)
        unit_movement.bind(on_release=self.init_Movement)
        diplomacy = Button(size_hint=(0.3, 0.1), pos_hint={"x": 0.35, "top": 0.6}, text='Diplomacy and War',
                           background_normal=os.path.join('assets', 'images', '57_header.png'),
                           background_down=os.path.join('assets', 'images', '57_header_d.png'), on_press=play_sound)
        diplomacy.bind(on_release=self.init_Diplomacy)
        resources = Button(size_hint=(0.3, 0.1), pos_hint={"x": 0.35, "top": 0.4}, text='Resources',
                           background_normal=os.path.join('assets', 'images', '57_header.png'),
                           background_down=os.path.join('assets', 'images', '57_header_d.png'), on_press=play_sound)
        resources.bind(on_release=self.init_Resources)
        quit = Button(size_hint=(0.3, 0.1), pos_hint={"x": 0.35, "top": 0.2},
                      background_normal=os.path.join('assets', 'images', '26_go_back_u.png'),
                      background_down=os.path.join('assets', 'images', '25_go_back_d.png'), on_press=play_sound)
        quit.bind(on_release=self.return_menu)
        self.add_widget(img)
        self.add_widget(unit_movement)
        self.add_widget(diplomacy)
        self.add_widget(resources)
        self.add_widget(quit)

    def return_menu(self, _):
        self.manager.current = 'Menu'
        self.manager.transition.direction = 'right'

    def init_Movement(self, _):
        self.manager.current = 'Movement Screen'
        self.manager.transition.direction = 'left'

    def init_Diplomacy(self, _):
        self.manager.current = 'Diplomacy Screen'
        self.manager.transition.direction = 'left'

    def init_Resources(self, _):
        self.manager.current = 'Resources Screen'
        self.manager.transition.direction = 'left'


class Movement_Screen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))
        img = Image(source=os.path.join('assets', 'images', 'rome.png'), allow_stretch=True, keep_ratio=False,
                    size=(GetSystemMetrics(0), GetSystemMetrics(1)))
        expl1 = Image(source=os.path.join('assets', 'images', '62_explanation1.png'), pos_hint={"x": -0.1, "top": 1.1},
                      allow_stretch=True, size_hint=(0.6, 0.4))
        expl2 = Image(source=os.path.join('assets', 'images', '63_explanation2.png'), pos_hint={"x": -0.1, "top": 0.85},
                      allow_stretch=True, size_hint=(0.6, 0.4))
        expl3 = Image(source=os.path.join('assets', 'images', '64_explanation3.png'), pos_hint={"x": -0.1, "top": 0.6},
                      allow_stretch=True, size_hint=(0.6, 0.4))
        expl4 = Image(source=os.path.join('assets', 'images', '69_explanation8.png'), pos_hint={"x": -0.1, "top": 0.35},
                      allow_stretch=True, size_hint=(0.6, 0.4))

        vid1 = VideoPlayer(source=os.path.join('assets', 'video', 'movement_imperium.mp4'),
                           pos_hint={"x": 0.6, "top": 1.0}, size_hint=(0.3, 0.25), allow_fullscreen=False)
        vid2 = VideoPlayer(source=os.path.join('assets', 'video', 'soldier_ability_imperium.mp4'),
                           pos_hint={"x": 0.6, "top": 0.75}, size_hint=(0.3, 0.25), allow_fullscreen=False)
        vid3 = VideoPlayer(source=os.path.join('assets', 'video', 'worker_ability_imperium.mp4'),
                           pos_hint={"x": 0.6, "top": 0.5}, size_hint=(0.3, 0.25), allow_fullscreen=False)
        vid4 = VideoPlayer(source=os.path.join('assets', 'video', 'warship_ability_imperium.mp4'),
                           pos_hint={"x": 0.6, "top": 0.25}, size_hint=(0.3, 0.25), allow_fullscreen=False)

        quit = Button(size_hint=(0.2, 0.1), pos_hint={"x": 0.35, "top": 0.1},
                      background_normal=os.path.join('assets', 'images', '26_go_back_u.png'),
                      background_down=os.path.join('assets', 'images', '25_go_back_d.png'), on_press=play_sound)
        quit.bind(on_release=self.return_menu)

        self.add_widget(img)
        self.add_widget(expl1)
        self.add_widget(expl2)
        self.add_widget(expl3)
        self.add_widget(expl4)
        self.add_widget(vid1)
        self.add_widget(vid2)
        self.add_widget(vid3)
        self.add_widget(vid4)
        self.add_widget(quit)

    def return_menu(self, _):
        self.manager.current = 'Tutorial'
        self.manager.transition.direction = 'right'


class Diplomacy_Screen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))
        img = Image(source=os.path.join('assets', 'images', 'rome.png'), allow_stretch=True, keep_ratio=False,
                    size=(GetSystemMetrics(0), GetSystemMetrics(1)))
        expl1 = Image(source=os.path.join('assets', 'images', '65_explanation4.png'), pos_hint={"x": -0.2, "top": 1.2},
                      allow_stretch=True, size_hint=(0.9, 0.9))
        expl2 = Image(source=os.path.join('assets', 'images', '66_explanation5.png'), pos_hint={"x": -0.1, "top": 0.65},
                      allow_stretch=True, size_hint=(0.7, 0.7))

        vid1 = VideoPlayer(source=os.path.join('assets', 'video', 'diplomacy_imperium.mp4'),
                           pos_hint={"x": 0.5, "top": 0.95}, size_hint=(0.4, 0.4), allow_fullscreen=False)
        vid2 = VideoPlayer(source=os.path.join('assets', 'video', 'war_imperium.mp4'), pos_hint={"x": 0.5, "top": 0.5},
                           size_hint=(0.4, 0.4), allow_fullscreen=False)

        quit = Button(size_hint=(0.2, 0.1), pos_hint={"x": 0.4, "top": 0.1},
                      background_normal=os.path.join('assets', 'images', '26_go_back_u.png'),
                      background_down=os.path.join('assets', 'images', '25_go_back_d.png'), on_press=play_sound)
        quit.bind(on_release=self.return_menu)

        self.add_widget(img)
        self.add_widget(expl1)
        self.add_widget(expl2)
        self.add_widget(vid1)
        self.add_widget(vid2)
        self.add_widget(quit)

    def return_menu(self, _):
        self.manager.current = 'Tutorial'
        self.manager.transition.direction = 'right'


class Resources_Screen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))
        img = Image(source=os.path.join('assets', 'images', 'rome.png'), allow_stretch=True, keep_ratio=False,
                    size=(GetSystemMetrics(0), GetSystemMetrics(1)))
        expl1 = Image(source=os.path.join('assets', 'images', '67_explanation6.png'), pos_hint={"x": -0.2, "top": 1.2},
                      allow_stretch=True, size_hint=(0.9, 0.9))
        expl2 = Image(source=os.path.join('assets', 'images', '68_explanation7.png'), pos_hint={"x": -0.1, "top": 0.65},
                      allow_stretch=True, size_hint=(0.7, 0.7))

        vid1 = VideoPlayer(source=os.path.join('assets', 'video', 'resources_imperium.mp4'),
                           pos_hint={"x": 0.5, "top": 0.95}, size_hint=(0.4, 0.4), allow_fullscreen=False)
        vid2 = VideoPlayer(source=os.path.join('assets', 'video', 'adding_manpower_imperium.mp4'),
                           pos_hint={"x": 0.5, "top": 0.5}, size_hint=(0.4, 0.4), allow_fullscreen=False)

        quit = Button(size_hint=(0.2, 0.1), pos_hint={"x": 0.4, "top": 0.1},
                      background_normal=os.path.join('assets', 'images', '26_go_back_u.png'),
                      background_down=os.path.join('assets', 'images', '25_go_back_d.png'), on_press=play_sound)
        quit.bind(on_release=self.return_menu)

        self.add_widget(img)
        self.add_widget(expl1)
        self.add_widget(expl2)
        self.add_widget(vid1)
        self.add_widget(vid2)
        self.add_widget(quit)

    def return_menu(self, _):
        self.manager.current = 'Tutorial'
        self.manager.transition.direction = 'right'


class Victory_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))

    def init_scoring(self, empire1, empire2, empire3):
        self.backgound = Image(source=os.path.join('assets', 'images', 'rome.png'), allow_stretch=True,
                               keep_ratio=False, size=(GetSystemMetrics(0), GetSystemMetrics(1)))
        img = Image(source=os.path.join('assets', 'images', 'rome_symbol.png'), allow_stretch=True, keep_ratio=False,
                    size_hint=(.2, .3))
        img2 = Image(source=os.path.join('assets', 'images', 'carthage_symbol.png'), allow_stretch=True,
                     keep_ratio=False, size_hint=(.2, .3))
        img3 = Image(source=os.path.join('assets', 'images', 'egypt_symbol.png'), allow_stretch=True, keep_ratio=False,
                     size_hint=(.2, .3))

        layout = BoxLayout(orientation='horizontal', size_hint=(0.95, 0.6), pos=(Window.width / 40, 50))
        layout1 = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(orientation='vertical')
        layout3 = BoxLayout(orientation='vertical')

        self.props = [empire1.name + 's treasury: ' + str(empire1.treasury),
                      empire1.name + 's stability: ' + str(empire1.stability),
                      empire1.name + 's manpower: ' + str(empire1.manpower),
                      empire1.name + 's units deployed: ' + str(empire1.army),
                      empire1.name + 's slave units: ' + str(empire1.workers),
                      empire1.name + 's farm tiles: ' + str(empire1.farms),
                      empire1.name + 's total territory: ' + str(empire1.tiles) + ' tiles']

        for i in range(len(self.props)):
            layout1.add_widget(Button(text=str(self.props[i])))
        layout.add_widget(layout1)

        if empire1.name == 'Rome':
            img.pos = (Window.width * 0.1, Window.height * 0.7)
            self.add_widget(img)
        elif empire1.name == 'Carthage':
            img2.pos = (Window.width * 0.1, Window.height * 0.7)
            self.add_widget(img2)
        elif empire1.name == 'Egypt':
            img3.pos = (Window.width * 0.1, Window.height * 0.7)
            self.add_widget(img3)

        if empire2 != None:
            self.props2 = [empire2.name + 's treasury: ' + str(empire2.treasury),
                           empire2.name + 's stability: ' + str(empire2.stability),
                           empire2.name + 's manpower: ' + str(empire2.manpower),
                           empire2.name + 's units deployed: ' + str(empire2.army),
                           empire2.name + 's slave units: ' + str(empire2.workers),
                           empire2.name + 's farm tiles: ' + str(empire2.farms),
                           empire2.name + 's total territory: ' + str(empire2.tiles) + ' tiles']

            for i in range(len(self.props2)):
                layout2.add_widget(Button(text=self.props2[i]))
            layout.add_widget(layout2)

            if empire2.name == 'Rome':
                img.pos = (Window.width * 0.4, Window.height * 0.7)
                self.add_widget(img)
            elif empire2.name == 'Carthage':
                img2.pos = (Window.width * 0.4, Window.height * 0.7)
                self.add_widget(img2)
            elif empire2.name == 'Egypt':
                img3.pos = (Window.width * 0.4, Window.height * 0.7)
                self.add_widget(img3)

        if empire3 != None:
            self.props3 = [empire3.name + 's treasury: ' + str(empire3.treasury),
                           empire3.name + 's stability: ' + str(empire3.stability),
                           empire3.name + 's manpower: ' + str(empire3.manpower),
                           empire3.name + 's units deployed: ' + str(empire3.army),
                           empire3.name + 's slave units: ' + str(empire3.workers),
                           empire3.name + 's farm tiles: ' + str(empire3.farms),
                           empire3.name + 's total territory: ' + str(empire3.tiles) + ' tiles']

            for i in range(len(self.props3)):
                layout3.add_widget(Button(text=self.props3[i]))
            layout.add_widget(layout3)

            if empire3.name == 'Rome':
                img.pos = (Window.width * 0.7, Window.height * 0.7)
                self.add_widget(img)
            elif empire3.name == 'Carthage':
                img2.pos = (Window.width * 0.7, Window.height * 0.7)
                self.add_widget(img2)
            elif empire3.name == 'Egypt':
                img3.pos = (Window.width * 0.7, Window.height * 0.7)
                self.add_widget(img3)

        self.add_widget(self.background)
        self.add_widget(layout)
        exit = Button(size_hint=(0.1, 0.05), pos=(Window.width - Window.width / 10, Window.height - Window.height / 20),
                      background_normal=os.path.join('assets', 'images', '26_go_back_u.png'),
                      background_down=os.path.join('assets', 'images', '25_go_back_d.png'), on_press=play_sound)
        exit.bind(on_release=self.return_menu)
        self.add_widget(exit)

    def return_menu(self, _):
        self.manager.current = 'Menu'
        self.manager.transition.direction = 'right'