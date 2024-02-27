import QtQuick
import QtQuick.Controls.Basic

ApplicationWindow {
    visible: true
    width: 800
    height: 400
    title: "project-python"

    Rectangle{
        anchors.fill: parent

        Image{
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./images/example.jpg"
            fillMode: Image.PreserveAspectCrop
        }

        Rectangle{
            anchors.fill: parent
            color: "transparent"

            Text {
                anchors{
                    bottom: parent.bottom
                    bottomMargin: 16
                    left: parent.left
                    leftMargin: 16
                }
                text: "A GERMAN FORD"
                font.pixelSize: 32
                color: "white"
            }
        }
    }
}