var ship;


function setup() {
    createCanvas(windowWidth, windowHeight);
    ship = new Ship();
}

function draw() {
    background(0);
    ship.render();
    ship.turn();
    ship.update();
    ship.edges();
}

