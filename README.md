# blynk-http-python-lib
This is a python library for exchanging data with Blynk using RESTful APIs. This library is much simpler and more straight-forward to use, compared with the official non-RESTful APIs.


## Blynk
Blynk is a IoT platform that eases the steps for building fast IoT prototypes with an UI on mobile phones (Android/iOS).


## Usage
clone the git project:

```bash
git clone https://github.com/automaticdai/blynk-http-python-lib
cd blynk-http-python-lib
```

create a python script with an editor in your favor (VIM for example):

```bash
vim main.py
```

include the library header:

```python
import blynk_http
```

init the library with your Blynk auth token:

```python
blynk_http.init('your_blynk_token')
```

write a value to a virtual pin:

```python
blynk_http.write('V0', '1000')
```

or read a value from a virtual pin:

```python
value = blynk_http.read('V1')
print(value)
```


## Supported Blynk Widgets
Supported input widgets:
- None

Supported output widgets:
- (Labeled) Value Display
- LED
- Gauge
- Level H/L
- Terminal
- LCD
- Send Email
- Push Notification

Not supported yet:
- Graph
- History Graph
- Button
- Slider
- Timer
- Joystick
- Step
- Twitter


## Todo List
Todo:
- Function parameter types are not checked
- Read pin history data
- Returned value from 'get_project_property()' API need to be parsed
- Widget Terminal can't be flushed which is supported by the official API.

Known issues:
- Network status APIs are not implemented as I think they have limited utilities.
- Widgets zeRGBa, Bridge, RT clock, BLE, Music Player and WebHook are not implemented as I do not know what there are for.
