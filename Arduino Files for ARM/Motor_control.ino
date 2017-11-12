// Motor A
int dir1PinA = 13; 
int dir2PinA = 12;
int speedPinA = 10;//Link to ENA

// Motor B
int dir1PinB = 11;
int dir2PinB = 8;
int speedPinB = 9;//Link to ENB

int speed;
int dir;//1 for forward, 0 for backward

void setup() {
  pinMode(dir1PinA, OUTPUT);
  pinMode(dir2PinA, OUTPUT);
  pinMode(speedPinA, OUTPUT);
  pinMode(dir1PinB, OUTPUT);
  pinMode(dir2PinB, OUTPUT);
  pinMode(speedPinB, OUTPUT);

  speed = 0;
  dir = 1;
}

void loop() {
  analogWrite(speedPinA, speed);//Output PWM to ENA
  analogWrite(speedPinB, speed);//Output PWM to ENB
  if (1 == dir) {
    digitalWrite(dir1PinA, LOW);
    digitalWrite(dir2PinA, HIGH);
    digitalWrite(dir1PinB, LOW);
    digitalWrite(dir2PinB, HIGH);
  } else { 
    digitalWrite(dir1PinA, HIGH);
    digitalWrite(dir2PinA, LOW);
    digitalWrite(dir1PinB, HIGH);
    digitalWrite(dir2PinB, LOW);
  }
  speed += 20;          //speed up
  if (speed &gt; 255) { 
    speed = 0;          
  }
  if (1 == dir) {
    dir = 0;
  } else {
    dir =1;
  }
  delay(15000);
｝
