/*
the three input control direction input recieved from thr rasp pi

          S2 S1 S0
          
Nothing   0  0  0
Up        0  0  1
Down      0  1  0
Left      0  1  1
Right     1  0  0
Forward   1  0  1
Back      1  1  0
Press     1  1  1

*/

// declare input pins that recieve data from the Raspberry Pi

const int s0 = 2;
const int s1 = 3;
const int s2 = 4;

// declare outputs pins for the servo motors on top

const int p = 5;  // p = pan servo 
const int t = 6;  // t = tilt servo

// declare output pins for stepper motor control

const int en1 = 7;
const int en2 = 8;
const int dir = 9;
const int pul = 10;

// declare output pins for the linear actuators

const int l_dir = 11
const int l_en = 12
const int s_dir = A0
const int s_en = A1

void setup() {
  
  pinMode(s0, INPUT);
  pinMode(s1, INPUT);
  pinMode(s2, INPUT);
  
  pinMode(p, OUTPUT);
  pinMode(t, OUTPUT);
  
  pinMode(en1, OUTPUT);
  pinMode(en2, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(pul, OUTPUT);
  
  pinMode(l_dir, OUTPUT);
  pinMode(s_dir, OUTPUT);
  pinMode(l_en, OUTPUT);
  pinMode(s_en, OUTPUT);
  
}

void loop()
{
  boolean c0 = digitalRead(s0);
  boolean c1 = digitalRead(s1);
  boolean c2 = digitalRead(s2);
  
  if (s0 == LOW && s1 == LOW && s2 == LOW)
  {
    // Stop all motors
  }
  
  
    if (s0 == HIGH && s1 == LOW && s2 == LOW)
  {
     // Switch motors to make the arm move up
  }
  
  
    if (s0 == LOW && s1 == HIGH && s2 == LOW)
  {
    // Switch motors to make the arm go down
  }
  
  
    if (s0 == HIGH && s1 == HIGH && s2 == LOW)
  {
    // Switch motors to make the arm go left
  }
  
  
    if (s0 == LOW && s1 == LOW && s2 == HIGH)
  {
    // Switch motors to make the arm go right
  }
  
  
    if (s0 == HIGH && s1 == LOW && s2 == HIGH)
  {
    // Switch motors to make the arm go forward
  }


    if (s0 == HIGH && s1 == HIGH && s2 == LOW)
  {
    // Switch motors to make the arm come backward
  }


    if (s0 == HIGH && s1 == HIGH && s2 == HIGH)
  {
    // Use linear actuator to press button in front 
  }
  
}