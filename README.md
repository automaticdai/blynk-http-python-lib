# blynk-http-python-lib
This is a python library for exchanging data with Blynk using RESTful APIs. This library is much simpler and more straight-forward to use, compared with the official non-RESTful APIs.


## Blynk
Blynk is a IoT platform that eases the steps for building fast IoT prototypes with an UI on mobile phones (Android/iOS).


## Usage
```bash
git clone https://github.com/automaticdai/blynk-http-python-lib
cd blynk-http-python-lib
```

Create a `demo.py` file with your favored editor:

```python
import blynk_http

blynk_http.init('your_blynk_token')
blynk_http.read('pin_name', 'value')
value = blynk_http.write('pin_name')
print(value)
```


## Supported Blynk Widgets
Supported widgets list:
- (Labeled) Value Display
- LED
- Terminal
- LCD
- Send Email
- Push Notification

Not supported yet:
- Gauge
- Graph
- History Graph
- Level H/L
- Button
- Slider
- Timer
- Joystick
- Step


## Todo List
Todo:
- Function parameter types are not checked
- Read pin history data
- Parse the returned value from 'Get_Project' API

Known issues:
- Terminal widget: can't flush
- Network status APIs are not implemented as I think they have limited utilities.
