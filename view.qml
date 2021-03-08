import QtQuick 2.0
import QtQuick.Window 2.2

Window {
    Image {
        id: background
        source: "background.jpg"
    }
    Image {
        id: dice
        anchors.bottom
        source: "dice.jpg"
    }

    }
visible: true
width: background.width
height: background.height
}