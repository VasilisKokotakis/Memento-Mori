from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.animation import Animation
from random import choice

# List of inspirational quotes
QUOTES = [
    "\"The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well.\" — Ralph Waldo Emerson",
    "\"Life is what happens when you're busy making other plans.\" — John Lennon",
    "\"Time is the coin of your life. It is the only coin you have, and only you can determine how it will be spent.\" — Carl Sandburg",
    "\"Your time is limited, so don't waste it living someone else's life.\" — Steve Jobs",
    "\"In the end, it's not the years in your life that count. It's the life in your years.\" — Abraham Lincoln",
    "\"Life isn't about finding yourself. Life is about creating yourself.\" — George Bernard Shaw",
    "\"Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did.\" — Mark Twain",
    "\"The most important thing is to enjoy your life—to be happy—it's all that matters.\" — Audrey Hepburn",
    "\"The journey of a thousand miles begins with one step.\" — Lao Tzu",
    "\"Life is 10% what happens to us and 90% how we react to it.\" — Charles R. Swindoll"
]

# Quotes specifically for seniors (60+)
SENIOR_QUOTES = [
    "\"Age is an issue of mind over matter. If you don't mind, it doesn't matter.\" — Mark Twain",
    "\"You are never too old to set another goal or to dream a new dream.\" — C.S. Lewis",
    "\"The longer I live, the more beautiful life becomes.\" — Frank Lloyd Wright",
    "\"It's not how old you are, it's how you are old.\" — Jules Renard",
    "\"Beautiful young people are accidents of nature, but beautiful old people are works of art.\" — Eleanor Roosevelt",
    "\"The older I get, the more I see there are these crevices in life where things fall in and you just can't reach them to pull them back out.\" — Robert Duvall",
    "\"Getting old is like climbing a mountain; you get a little out of breath, but the view is much better!\" — Ingrid Bergman",
    "\"Today is the oldest you've ever been and the youngest you'll ever be again.\" — Eleanor Roosevelt",
    "\"The great thing about getting older is that you don't lose all the other ages you've been.\" — Madeleine L'Engle",
    "\"Those who love deeply never grow old; they may die of old age, but they die young.\" — Benjamin Franklin"
]

# Quotes for those who have reached or exceeded life expectancy
WISDOM_QUOTES = [
    "\"You don't stop laughing when you grow old, you grow old when you stop laughing.\" — George Bernard Shaw",
    "\"The best classroom in the world is at the feet of an elderly person.\" — Andy Rooney",
    "\"None are so old as those who have outlived enthusiasm.\" — Henry David Thoreau",
    "\"Do not regret growing older. It is a privilege denied to many.\" — Unknown",
    "\"Aging is not lost youth but a new stage of opportunity and strength.\" — Betty Friedan",
    "\"With age comes wisdom, with wisdom comes balance, with balance comes perspective.\" — Toba Beta",
    "\"The longer I live, the more beautiful life becomes.\" — Frank Lloyd Wright",
    "\"To know how to grow old is the master work of wisdom, and one of the most difficult chapters in the great art of living.\" — Henri Frederic Amiel",
    "\"In the end, it's not the years in your life that count. It's the life in your years.\" — Abraham Lincoln",
    "\"We don't stop playing because we grow old; we grow old because we stop playing.\" — George Bernard Shaw"
]

class BackgroundScreen(Screen):
    def __init__(self, **kwargs):
        super(BackgroundScreen, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.9, 0.95, 1, 1)  # Light blue background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

class StylishButton(Button):
    def __init__(self, **kwargs):
        super(StylishButton, self).__init__(**kwargs)
        self.background_color = get_color_from_hex('#3498db')  # Nice blue color
        self.background_normal = ''  # Remove default button background
        self.color = [1, 1, 1, 1]  # White text
        self.bold = True
        self.font_size = '18sp'
        self.size_hint_y = None
        self.height = 60
        self.border = (10, 10, 10, 10)

class IntroScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super(IntroScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=[20, 20])
        self.layout.opacity = 0  # Start invisible for fade-in animation
        
        # Create spacer to center content vertically
        self.layout.add_widget(BoxLayout(size_hint_y=0.3))
        
        # Add app title
        title_box = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
        app_title = Label(
            text='LIFE IN WEEKS',
            font_size='36sp',
            bold=True,
            color=get_color_from_hex('#2c3e50'),
            opacity=0
        )
        subtitle = Label(
            text='Make every week count',
            font_size='20sp',
            color=get_color_from_hex('#7f8c8d'),
            opacity=0
        )
        title_box.add_widget(app_title)
        title_box.add_widget(BoxLayout(size_hint_y=None, height=20))  # Spacer
        title_box.add_widget(subtitle)
        
        self.layout.add_widget(title_box)
        self.layout.add_widget(BoxLayout(size_hint_y=0.3))  # Spacer for bottom
        
        self.add_widget(self.layout)
        
        # Store references for animations
        self.app_title = app_title
        self.subtitle = subtitle
        
        # Schedule animations after screen appears
        Clock.schedule_once(self.start_animations, 0.5)
    
    def start_animations(self, dt):
        # First fade in layout
        anim = Animation(opacity=1, duration=1)
        anim.start(self.layout)
        
        # Then fade in title
        anim1 = Animation(opacity=0, duration=0) + Animation(opacity=1, duration=1.0)
        anim1.start(self.app_title)
        
        # Then fade in subtitle
        anim2 = Animation(opacity=0, duration=0.8) + Animation(opacity=1, duration=1.0)
        anim2.bind(on_complete=self.show_next_screen)
        anim2.start(self.subtitle)
    
    def show_next_screen(self, animation, widget):
        # Wait 1.5 seconds then show age input screen
        Clock.schedule_once(self.transition_to_age_input, 1.5)
        
    def transition_to_age_input(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'age_input'

class AgeInputScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super(AgeInputScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=[20, 20])
        
        # Create spacer to center content vertically
        self.layout.add_widget(BoxLayout(size_hint_y=0.2))
        
        # Input container with animation properties
        self.input_container = BoxLayout(orientation='vertical', 
                                   size_hint_y=None, 
                                   height=200,
                                   opacity=0)  # Start invisible
        
        # Add app title
        app_title = Label(
            text='LIFE IN WEEKS',
            font_size='24sp',
            bold=True,
            color=get_color_from_hex('#2c3e50'),
            size_hint_y=None,
            height=40
        )
        
        # Input section
        input_section = GridLayout(cols=1, spacing=15, size_hint_y=None, height=160)
        
        age_label = Label(
            text='Enter your age:',
            font_size='20sp',
            color=get_color_from_hex('#2c3e50'),
            size_hint_y=None,
            height=40,
            halign='center'
        )
        age_label.bind(size=lambda s, w: setattr(s, 'text_size', w))
        
        self.input = TextInput(
            hint_text='Age in years',
            multiline=False,
            input_filter='float',
            font_size='24sp',
            size_hint_y=None,
            height=70,
            padding=[15, 20],
            background_color=get_color_from_hex('#ffffff'),
            halign='center'
        )
        
        # Button
        self.button = StylishButton(text='SEE MY REMAINING TIME')
        self.button.bind(on_press=self.on_calculate)
        
        input_section.add_widget(age_label)
        input_section.add_widget(self.input)
        input_section.add_widget(self.button)
        
        self.input_container.add_widget(app_title)
        self.input_container.add_widget(input_section)
        
        self.layout.add_widget(self.input_container)
        self.layout.add_widget(BoxLayout(size_hint_y=0.3))  # Spacer for bottom
        
        self.add_widget(self.layout)
        
        # Schedule animation after screen appears
        Clock.schedule_once(self.start_animations, 0.2)
    
    def start_animations(self, dt):
        # Float up and fade in animation
        anim = Animation(opacity=0, pos_hint={'center_y': 0.3}, duration=0) + \
               Animation(opacity=1, pos_hint={'center_y': 0.5}, duration=1.2, 
                        transition='out_back')
        anim.start(self.input_container)
    
    def on_calculate(self, instance):
        try:
            age = float(self.input.text)
            if age < 0 or age > 150:
                # Show error popup or message
                return
                
            # Store the age in the app for the result screen
            app = App.get_running_app()
            app.user_age = age
            
            # Transition to result screen
            self.manager.transition = SlideTransition(direction='left')
            self.manager.current = 'result'
            
        except ValueError:
            # Show error popup or message
            pass

class ResultScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=[20, 20])
        
        # All elements start invisible for animation
        self.title_label = Label(
            text='YOUR REMAINING TIME',
            font_size='24sp',
            bold=True,
            color=get_color_from_hex('#2c3e50'),
            size_hint_y=None,
            height=60,
            opacity=0
        )
        
        # Weeks lived container
        self.lived_container = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=100,
            opacity=0
        )

        self.lived_label = Label(
            text='',
            font_size='28sp',
            bold=True,
            color=get_color_from_hex('#2980b9'),
            size_hint_y=None,
            height=60
        )

        self.lived_subtitle = Label(
            text='WEEKS LIVED',
            font_size='16sp',
            color=get_color_from_hex('#7f8c8d'),
            size_hint_y=None,
            height=30
        )

        self.lived_container.add_widget(self.lived_label)
        self.lived_container.add_widget(self.lived_subtitle)

        # Weeks remaining container
        self.result_container = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=150,
            opacity=0
        )
        
        self.weeks_label = Label(
            text='',
            font_size='50sp',
            bold=True,
            color=get_color_from_hex('#27ae60'),
            size_hint_y=None,
            height=80
        )
        
        self.weeks_subtitle = Label(
            text='WEEKS REMAINING',
            font_size='18sp',
            color=get_color_from_hex('#7f8c8d'),
            size_hint_y=None,
            height=40
        )
        
        self.result_container.add_widget(self.weeks_label)
        self.result_container.add_widget(self.weeks_subtitle)
        
        # Quote container
        self.quote_container = BoxLayout(
            orientation='vertical',
            padding=[10, 30],
            size_hint_y=None,
            height=200,
            opacity=0
        )
        
        self.quote_divider_top = Label(
            text='— — —',
            font_size='24sp',
            color=get_color_from_hex('#bdc3c7'),
            size_hint_y=None,
            height=30
        )
        
        self.quote_text = Label(
            text='',
            font_size='16sp',
            color=get_color_from_hex('#2c3e50'),
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=140,
            text_size=(Window.width - 80, None)
        )
        
        self.quote_divider_bottom = Label(
            text='— — —',
            font_size='24sp',
            color=get_color_from_hex('#bdc3c7'),
            size_hint_y=None,
            height=30
        )
        
        self.quote_container.add_widget(self.quote_divider_top)
        self.quote_container.add_widget(self.quote_text)
        self.quote_container.add_widget(self.quote_divider_bottom)
        
        # Restart button
        self.restart_button = StylishButton(
            text='START OVER',
            size_hint=(0.7, None),
            height=60,
            pos_hint={'center_x': 0.5},
            opacity=0
        )
        self.restart_button.bind(on_press=self.go_to_intro)
        
        # Add widgets to layout
        self.layout.add_widget(BoxLayout(size_hint_y=0.05))  # Top spacer
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(BoxLayout(size_hint_y=0.05))  # Spacer
        self.layout.add_widget(self.lived_container)
        self.layout.add_widget(BoxLayout(size_hint_y=0.05))  # Spacer
        self.layout.add_widget(self.result_container)
        self.layout.add_widget(BoxLayout(size_hint_y=0.05))  # Spacer
        self.layout.add_widget(self.quote_container)
        self.layout.add_widget(BoxLayout(size_hint_y=0.1))  # Spacer
        self.layout.add_widget(self.restart_button)
        self.layout.add_widget(BoxLayout(size_hint_y=0.1))  # Bottom spacer
        
        self.add_widget(self.layout)
    
    def on_pre_enter(self):
        app = App.get_running_app()
        age = getattr(app, 'user_age', 30)  # Default to 30
        
        life_expectancy = 90
        weeks_lived = int(age * 52.1775)
        self.lived_label.text = f"{weeks_lived:,}"
        
        if age >= life_expectancy:
            self.title_label.text = 'LIFE WELL LIVED'
            self.weeks_label.text = 'BONUS TIME'
            self.weeks_label.color = get_color_from_hex('#8e44ad')
            self.weeks_subtitle.text = 'EVERY DAY IS A GIFT'
            self.quote_text.text = choice(WISDOM_QUOTES)
        elif age >= 60:
            weeks_left = int((life_expectancy - age) * 52.1775)
            self.weeks_label.text = f"{weeks_left:,}"
            self.weeks_label.color = get_color_from_hex('#e67e22')
            self.title_label.text = 'YOUR GOLDEN YEARS'
            self.quote_text.text = choice(SENIOR_QUOTES)
        else:
            weeks_left = int((life_expectancy - age) * 52.1775)
            self.weeks_label.text = f"{weeks_left:,}"
            self.weeks_label.color = get_color_from_hex('#27ae60')
            self.quote_text.text = choice(QUOTES)
        
        Clock.schedule_once(self.start_animations, 0.2)
    
    def start_animations(self, dt):
        anim1 = Animation(opacity=1, duration=0.8)
        anim1.start(self.title_label)
        
        anim_lived = Animation(opacity=0, duration=0.4) + Animation(opacity=1, duration=1.0)
        Clock.schedule_once(lambda dt: anim_lived.start(self.lived_container), 0.2)
        
        anim2 = Animation(opacity=0, duration=0.6) + Animation(opacity=1, duration=1.0)
        Clock.schedule_once(lambda dt: anim2.start(self.result_container), 0.6)
        
        anim3 = Animation(opacity=0, duration=1.2) + Animation(opacity=1, duration=1.0)
        Clock.schedule_once(lambda dt: anim3.start(self.quote_container), 1.0)
        
        anim4 = Animation(opacity=0, duration=1.8) + Animation(opacity=1, duration=0.8)
        Clock.schedule_once(lambda dt: anim4.start(self.restart_button), 1.4)
    
    def go_to_intro(self, instance):
        self.manager.transition = FadeTransition(duration=0.5)
        self.manager.current = 'intro'

class LifeInWeeksApp(App):
    def build(self):
        self.title = 'Life in Weeks'
        Window.size = (400, 600)
        Window.clearcolor = get_color_from_hex('#f0f5ff')
        
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(IntroScreen(name='intro'))
        sm.add_widget(AgeInputScreen(name='age_input'))
        sm.add_widget(ResultScreen(name='result'))
        
        return sm

if __name__ == '__main__':
    LifeInWeeksApp().run()
