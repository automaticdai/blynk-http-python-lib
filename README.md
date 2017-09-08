# blynk-http-python-lib
This is a python library for exchanging data with Blynk using RESTful APIs. This library is much simpler and more straight-forward to use, compared with the official non-RESTful APIs.


## Blynk
Blynk is a IoT platform that eases the steps for building fast IoT prototypes with an UI on mobile phones (Android/iOS).


## Usage
`git clone https://github.com/automaticdai/blynk-http-python-lib`

```python
import blynk_http

blynk_http.init()
blynk_http.read()
# or
blynk_http.write()
```


## Supported Blynk Widgets

- (Labeled) Value Display
- LED
- Terminal


Not supported yet:

- Gauge
- LCD
- Graph
- History Graph
- Level H/L
- Notification
- Button
- Slider
- Timer
- Joystick
- Step


## Known Issues

- Terminal: can't flush the terminal
