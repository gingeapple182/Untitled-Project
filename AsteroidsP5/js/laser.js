function Laser() {
    this.pos = createVector();
    this.vel = createVector();

    this.update = function() {
        this.pos.add(this.vel);
    }

    this.render = function() {
        stroke(255);
        strokeWeight(4);
        point(this.x, this.y);
    }
}