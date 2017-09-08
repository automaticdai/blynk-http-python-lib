# blynk-http-python-lib
A python library for exchanging data with Blynk using RESTful APIs.

## Usage

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
