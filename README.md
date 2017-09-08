# blynk-http-python-lib
This is a python library for exchanging data with Blynk using RESTful APIs. This library is much simpler and more straight-forward to use, compared with the official non-RESTful APIs.


## Blynk
Blynk is a IoT platform that eases the steps for building fast IoT prototypes with an UI on mobile phones (Android/iOS).


## Usage
`git clone https://github.com/automaticdai/blynk-http-python-lib`

```python
import blynk_http

blynk_http.init('your_blynk_token')
blynk_http.read('pin_name', 'value')
# or
blynk_http.write('pin_name')
```


## Supported Blynk Widgets
Supported list:

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
- Send Email
- Push Notification

## Todo List
Todo:
- Function parameter types are not checked
- Read pin history data
- Analyse the returned value from the 'Get_Project' API

Known issues:
- Terminal widget: can't flush
- Network status APIs not implemented as I think they have limited utilities.
