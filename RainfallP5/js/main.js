var rain = [];

//var speed;

function setup() {
  createCanvas(600, 600);
  for (var i = 0; i < 700; i++) {
    rain[i] = new Rain();
  }
}

function draw() {
  //speed = map(mouseX, 0, width, 10, 50);
  background(100);
  //translate(width / 2, height / 2);
  for (var i = 0; i < stars.length; i++) {
    rain[i].update();
    rain[i].show();
  }
}