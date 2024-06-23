serial.redirectToUSB()
basic.forever(function on_forever() {
    serial.writeValue("digital signal", pins.digitalReadPin(DigitalPin.P12))
    basic.pause(1000)
})
