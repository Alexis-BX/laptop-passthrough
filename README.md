Hardware
------------
- Arduino based on the 32U4 chip (recommended: Arduino Micro Pro)
- USB to TTY
- HDMI to USB capture card


Keyboard passthrough setup
------------
### Arduino setup
1. Flash the file `key_passthrough/key_passthrough.ino` onto the Arduino.
2. Unplug the Arduino.
3. Connect the following:

| Arduino | USB-TTY |
| ------- | ------- |
| Pin 9   | Tx      |
| Pin 10  | RX      |
| GND     | GND     |

4. Plug the USB-TTY into the laptop
5. Plug the Arduino into the device to control

### Laptop setup
Prerequisit: python 3.8

    pip install pygame==2.5.2

### Starting the passthrough

    python3 passthrough.py [port]
The `port` argument is `/dev/ttyUSB0` by default. `test_ports.py` can be used to help find the correct port.

Once the game window opens, select it and start typing!

Notes:
- You may need to run in sudo to access the ports. In which case make sure to `sudo pip install pygame`
- On Windows these are the COM ports
- If you are running in WSL, you need to activate your graphics and tell Windows to pass you the USB device: [https://learn.microsoft.com/en-us/windows/wsl/connect-usb#attach-a-usb-device](https://learn.microsoft.com/en-us/windows/wsl/connect-usb#attach-a-usb-device)


Video passthrough
-----
### VLC setup
- Connect the capture card to the device by HDMI and to the laptop by USB. 
- `Media` -> `Open Capture Device`
- Select `Show more options`
- Caching: `0`
- MLR: `dshow://`
- Edit Options: `:dshow-vdev="USB Video" :dshow-adev= :dshow-aspect-ratio="16:9" :dshow-audio-samplerate=48000 :dshow-audio-channels=2 :live-caching=0 :dshow-fps=60 :dshow-size=1920x1080`

Note: `dshow-vdev` may need to be adjusted, check the `Video device name` dropdown for exact name.

To open this automatically you can create a VLC shortcup with target: `"C:\Program Files\VideoLAN\VLC\vlc.exe" dshow:// :dshow-vdev="USB Video" :dshow-adev= :dshow-aspect-ratio="16:9" :dshow-audio-samplerate=48000 :dshow-audio-channels=2 :live-caching=0 :dshow-fps=60 :dshow-size=1920x1080`


References
-----
Original keyboard passthrough and inspiration:
[https://euer.krebsco.de/a-software-kvm-switch.html](https://euer.krebsco.de/a-software-kvm-switch.html)

