serial.redirect_to_usb()

def on_forever():
    serial.write_value("digital signal", pins.digital_read_pin(DigitalPin.P12))
    basic.pause(1000)
basic.forever(on_forever)
