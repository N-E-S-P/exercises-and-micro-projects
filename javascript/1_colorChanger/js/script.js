// Every time the button is clicked, the background changes color.

const colorList = ["red", "green", "yellow", "purple", "blue", "pink", "white"]

document.getElementById("btn1").addEventListener("click", colorChange);

function colorChange() {
    var randomElement = colorList[Math.floor(Math.random() * colorList.length)]
    document.getElementById("body").style.backgroundColor = randomElement;
    while (randomElement == true) {
        document.getElementById("butt").addEventListener("click", colorChange);
    }
}
