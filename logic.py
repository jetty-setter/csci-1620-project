from PyQt6.QtWidgets import *
from gui import *


class Television(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 25
    MIN_CHANNEL = 0
    MAX_CHANNEL = 10

    def __init__(self) -> None:
        """ Initializes the application
        :parameters: None """
        super().__init__()
        self.setupUi(self)
        self.status = False
        self.muted = False
        self.muted_volume = 0
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL
        self.slider_volume.setMaximum(25)
        self.slider_volume.setMinimum(0)
        self.view_channel.setPixmap(QtGui.QPixmap("0x0"))
        self.label_power.setPixmap(QtGui.QPixmap("images/power_off.jpg"))
        self.button_power.clicked.connect(self.power)
        self.button_volup.clicked.connect(self.button_volup_action)
        self.button_voldown.clicked.connect(self.button_voldown_action)
        self.button_chanup.clicked.connect(self.button_chanup_action)
        self.button_chandown.clicked.connect(self.button_chandown_action)
        self.button_mute.clicked.connect(self.mute)
        self.slider_volume.setEnabled(False)
        self.slider_volume.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)  # Hide ticks
        self.slider_volume.sliderMoved.connect(self.slider_moved)
        self.slider_volume.sliderPressed.connect(self.slider_pressed)

    def power(self) -> None:
        """ Turns the TV on and off depending on the status
        :parameters: None """
        if self.status:
            self.status = False
            self.label_power.setPixmap(QtGui.QPixmap("images/power_off.jpg"))
            self.label_channel.setText(f'')
            self.slider_volume.setValue(self.MIN_VOLUME)
            self.view_channel.setPixmap(QtGui.QPixmap("0x0.jpg"))
            self.disable_slider()
        else:
            self.status = True
            self.label_power.setPixmap(QtGui.QPixmap("0x0.jpg"))
            self.slider_volume.setValue(self.volume)
            self.enable_slider()
            self.channel = self.channel
            self.label_channel.setText(f'{self.channel}')
            if self.channel == 0:
                self.view_channel.setPixmap(QtGui.QPixmap('images/abc.jpg'))
            elif self.channel == 1:
                self.view_channel.setPixmap(QtGui.QPixmap('images/animalplanet.jpg'))
            elif self.channel == 2:
                self.view_channel.setPixmap(QtGui.QPixmap('images/cbs.jpg'))
            elif self.channel == 3:
                self.view_channel.setPixmap(QtGui.QPixmap('images/discovery.jpg'))
            elif self.channel == 4:
                self.view_channel.setPixmap(QtGui.QPixmap('images/ESPN.jpg'))
            elif self.channel == 5:
                self.view_channel.setPixmap(QtGui.QPixmap('images/hbo.jpg'))
            elif self.channel == 6:
                self.view_channel.setPixmap(QtGui.QPixmap('images/history.jpg'))
            elif self.channel == 7:
                self.view_channel.setPixmap(QtGui.QPixmap('images/mtv.jpg'))
            elif self.channel == 8:
                self.view_channel.setPixmap(QtGui.QPixmap('images/Nickelodeon.jpg'))
            elif self.channel == 9:
                self.view_channel.setPixmap(QtGui.QPixmap('images/Showtime.jpg'))
            elif self.channel == 10:
                self.view_channel.setPixmap(QtGui.QPixmap('images/vice.jpg'))

    def enable_slider(self) -> None:
        """ Enables the slider volume depending on the status
        :parameters: None """
        if self.status:
            self.slider_volume.setEnabled(True)

    def disable_slider(self) -> None:
        """ Disables the slider volume depending on the status
        :parameters: None """
        self.slider_volume.setEnabled(False)

    def slider_moved(self) -> None:
        """ Updates the volume slider position to match the current volume value.
        :parameters: None """
        if self.slider_volume.isEnabled():
            self.slider_volume.setValue(self.volume)

    def slider_pressed(self) -> None:
        """ Updates the volume slider position to match the current volume value when the slider is pressed.
        :parameters: None """
        if self.slider_volume.isEnabled():
            self.slider_volume.setValue(self.volume)

    def button_volup_action(self) -> None:
        """ Increases the volume depending on the status
        :parameters: None """
        if self.status and self.volume < Television.MAX_VOLUME:
            self.volume += 1
            self.slider_volume.setValue(self.volume)

    def button_voldown_action(self) -> None:
        """Decreases the volume depending on the status
        :parameters: None """
        if self.status and self.volume > Television.MIN_VOLUME:
            self.volume -= 1
            self.slider_volume.setValue(self.volume)

    def mute(self) -> None:
        """ Mutes the volume depending on the status
        :parameters: None """
        if self.status:
            if not self.muted:
                self.muted = True
                self.muted_volume = self.volume
                self.volume = Television.MIN_VOLUME
            else:
                self.muted = False
                self.volume = self.muted_volume

            self.slider_volume.setValue(self.volume)

    def button_chanup_action(self) -> None:
        """ Increases the channel depending on the status
        :parameters: None """
        if not self.status:
            return
        if self.channel < Television.MAX_CHANNEL:
            self.channel += 1
            if self.channel == 1:
                self.view_channel.setPixmap(QtGui.QPixmap('images/animalplanet.jpg'))
            elif self.channel == 2:
                self.view_channel.setPixmap(QtGui.QPixmap('images/cbs.jpg'))
            elif self.channel == 3:
                self.view_channel.setPixmap(QtGui.QPixmap('images/discovery.jpg'))
            elif self.channel == 4:
                self.view_channel.setPixmap(QtGui.QPixmap('images/ESPN.jpg'))
            elif self.channel == 5:
                self.view_channel.setPixmap(QtGui.QPixmap('images/hbo.jpg'))
            elif self.channel == 6:
                self.view_channel.setPixmap(QtGui.QPixmap('images/history.jpg'))
            elif self.channel == 7:
                self.view_channel.setPixmap(QtGui.QPixmap('images/mtv.jpg'))
            elif self.channel == 8:
                self.view_channel.setPixmap(QtGui.QPixmap('images/Nickelodeon.jpg'))
            elif self.channel == 9:
                self.view_channel.setPixmap(QtGui.QPixmap('images/Showtime.jpg'))
            elif self.channel == 10:
                self.view_channel.setPixmap(QtGui.QPixmap('images/vice.jpg'))
        else:
            self.channel = Television.MIN_CHANNEL
        self.label_channel.setText(f'{self.channel}')
        if self.channel == 0:
            self.view_channel.setPixmap(QtGui.QPixmap('images/abc.jpg'))

    def button_chandown_action(self) -> None:
        """ Decreases the channel depending on the status
        :parameters: None """
        if not self.status:
            return
        if self.channel > Television.MIN_CHANNEL:
            self.channel -= 1
            if self.channel == 0:
                self.view_channel.setPixmap(QtGui.QPixmap('images/abc.jpg'))
            elif self.channel == 1:
                self.view_channel.setPixmap(QtGui.QPixmap('images/animalplanet.jpg'))
            elif self.channel == 2:
                self.view_channel.setPixmap(QtGui.QPixmap('images/cbs.jpg'))
            elif self.channel == 3:
                self.view_channel.setPixmap(QtGui.QPixmap('images/discovery.jpg'))
            elif self.channel == 4:
                self.view_channel.setPixmap(QtGui.QPixmap('images/ESPN.jpg'))
            elif self.channel == 5:
                self.view_channel.setPixmap(QtGui.QPixmap('images/hbo.jpg'))
            elif self.channel == 6:
                self.view_channel.setPixmap(QtGui.QPixmap('images/history.jpg'))
            elif self.channel == 7:
                self.view_channel.setPixmap(QtGui.QPixmap('images/mtv.jpg'))
            elif self.channel == 8:
                self.view_channel.setPixmap(QtGui.QPixmap('images/Nickelodeon.jpg'))
            elif self.channel == 9:
                self.view_channel.setPixmap(QtGui.QPixmap('images/Showtime.jpg'))
        else:
            self.channel = Television.MAX_CHANNEL
        self.label_channel.setText(f'{self.channel}')
        if self.channel == 10:
            self.view_channel.setPixmap(QtGui.QPixmap('images/vice.jpg'))