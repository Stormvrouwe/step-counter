input.onGesture(Gesture.Shake, function () {
    Stappen += 1
})
let Stappen = 0
led.stopAnimation()
basic.forever(function () {
    basic.showNumber(Stappen)
})
