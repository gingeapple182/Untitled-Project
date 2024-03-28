function Star() {
    this.x = random(width);
    this.y = random(-height, height); // Change this line
    this.z = random(width);
    this.speed = random(1, 5);
    this.gravity = 0.01;
    this.length = map(this.speed, 0, 20, 10, 20);
  
    this.update = function() {
      this.y = this.y + this.speed;
      this.speed = this.speed + this.gravity;
  
      if (this.y > height) {
        this.y = random(-height, 0);
        this.speed = random(1, 5);
      }
    }
  
    this.show = function() {
      var thick = map(this.speed, 0, 20, 4, 5);
      strokeWeight(thick);
      stroke(155, 255, 255, 50);
      line(this.x, this.y, this.x, this.y+this.length);
    }
  }
  