var ship;
var asteroids = [];
var lasers = [];
var gameOver = false;
var victory = false;
var score = 0;
var difficulty = 5;

function setup() {
    createCanvas(windowWidth, windowHeight);
    ship = new Ship();
    for (var i = 0; i < difficulty; i++) {
    asteroids.push(new Asteroid());
    }
}

function draw() {
    background(0);
    if (!gameOver && !victory) {
        for (var i = 0; i < asteroids.length; i++) {
            if (ship.hits(asteroids[i])) {
                console.log('goddamnit lana');
                gameOver = true;
            }
            asteroids[i].render();
            asteroids[i].update();
            asteroids[i].edges();
        }
        for (var i = lasers.length - 1; i >= 0; i--) {
            lasers[i].render();
            lasers[i].update();
            if (lasers[i].offScreen()) {
                lasers.splice(i, 1);
            } else {
                for (var j = asteroids.length - 1; j >= 0; j--) {
                    if (lasers[i].hits(asteroids[j])) {
                        if (asteroids[j].r > 15) {
                            var newAsteroids = asteroids[j].breakup();
                            asteroids = asteroids.concat(newAsteroids);
                        } 
                        asteroids.splice(j, 1);
                        lasers.splice(i, 1);
                        score++;
                        break;
                    }
                }
            }
        }
        if (asteroids.length === 0) {
            victory = true;
        }
        ship.render();
        ship.turn();
        ship.update();
        ship.edges();

        
        console.log('score: ' + score);
        console.log(asteroids.length);

    } else if (gameOver) {
        screenDisplay('Game over')
    } else if (victory) {
        screenDisplay('Victory')
    }
}

function screenDisplay(winCondition) {
    textAlign(CENTER, CENTER);
    textSize(64);
    fill(255);
    text(winCondition, width / 2, height / 3);
    textSize(32);
    text('Score: ' + score, width / 2, height / 2);
    if (gameOver || victory) {
        text('Press Enter to restart', width / 2, height * 2 / 3);
    }
}

function restartGame() {
    gameOver = false;
    victory = false;
    ship = new Ship();
    asteroids = [];
    lasers = [];
    score = 0;
    for (var i = 0; i < difficulty; i++) {
        asteroids.push(new Asteroid());
    }
}

function keyPressed() {
    if (key == ' ') {
        console.log('pew! ')
        lasers.push(new Laser(ship.pos, ship.heading));
    } else if (keyCode == RIGHT_ARROW) {
        ship.setRotation(0.1);
    } else if (keyCode == LEFT_ARROW) {
        ship.setRotation(-0.1);
    } else if (keyCode == UP_ARROW) {
        ship.boosting(true);
    } else if (keyCode == ENTER && (gameOver == true || victory == true)) {
        restartGame();
    }
}

function keyReleased() {
    ship.setRotation(0);
    ship.boosting(false);
}
