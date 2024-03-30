var ship;
var asteroids = [];
var lasers = [];

function setup() {
    createCanvas(windowWidth, windowHeight);
    ship = new Ship();
    for (var i = 0; i < 10; i++) {
    asteroids.push(new Asteroid());
    }
}

function draw() {
    background(0);
    ship.render();
    ship.turn();
    ship.update();
    ship.edges();

    for (var i = 0; i < asteroids.length; i++) {
        asteroids[i].render();
        asteroids[i].update();
        asteroids[i].edges();
    }
    for (var i = 0; i < lasers.length; i++) {
        lasers[i].render();
        lasers[i].update();
    }

}

