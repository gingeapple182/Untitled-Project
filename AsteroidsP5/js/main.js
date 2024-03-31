var ship;
var asteroids = [];
var lasers = [];
var gameOver = false;

function setup() {
    createCanvas(windowWidth, windowHeight);
    ship = new Ship();
    for (var i = 0; i < 10; i++) {
    asteroids.push(new Asteroid());
    }
}

function keyPressed() {
    if (key == ' ') {
        lasers.push(new Laser(ship.pos, ship.heading));
    }else if (keyCode == RIGHT_ARROW) {
        ship.setRotation(0.1);
    } else if (keyCode == LEFT_ARROW) {
        ship.setRotation(-0.1);
    } else if (keyCode == UP_ARROW) {
        ship.boosting(true);
    }
}

function keyReleased() {
    ship.setRotation(0);
    ship.boosting(false);
}

function gameOver() {
    document.getElementById('overlay').style.display = 'block';
}

function restartGame() {
    document.getElementById('overlay').style.display = 'none';
}

document.getElementById('restartButton').addEventListener('click', restartGame);

function draw() {
    background(0);
    for (var i = 0; i < asteroids.length; i++) {
        if (ship.hits(asteroids[i])) {
            console.log('goddamnit lana');
            gameOver();
        }
        asteroids[i].render();
        asteroids[i].update();
        asteroids[i].edges();
    }
    for (var i = lasers.length - 1; i >= 0; i--) {
        lasers[i].render();
        lasers[i].update();
        for (var j = asteroids.length - 1; j >= 0; j--) {
            if (lasers[i].hits(asteroids[j])) {
                if (asteroids[j].r > 15) {
                    var newAsteroids = asteroids[j].breakup();
                    asteroids = asteroids.concat(newAsteroids);
                } 
                asteroids.splice(j, 1);
                lasers.splice(i, 1);
                break;
            }
        }
    }

    ship.render();
    ship.turn();
    ship.update();
    ship.edges();

}
