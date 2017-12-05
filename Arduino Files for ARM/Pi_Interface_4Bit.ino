/*
the three input control direction input recieved from thr rasp pi

          S3 S2 S1 S0
          
Nothing    0  0  0  0
Up         0  0  0  1
Down       0  0  1  0
Left       0  0  1  1
Right      0  1  0  0
Forward    0  1  0  1
Back       0  1  1  0
Look left  0  1  1  1
Look Right 1  0  0  0
Press      1  0  0  1
Back       1  0  1  0
Reset      1  0  1  1

*/

// declare input pins that recieve data from the Raspberry Pi

const int c0 = A0;
const int c1 = A1;
const int c2 = A2;
const int c3 = A3;


// declare outputs pins for the servo motors on top

Servo p;  // p = pan servo 
Servo t;  // t = tilt servo
Servo l;  // l = linear servo

// declare output pins for stepper motor control

const int en = 3;
const int dir = 2;
const int pul = 4;

// declare output pins for the linear actuator

const int l_in1 = 8;
const int l_in2 = 11;


void setup() {
  
  pinMode(c0, INPUT);
  pinMode(c1, INPUT);
  pinMode(c2, INPUT);
  pinMode(c3, INPUT);
  
  p.attach(5);
  int pos_p;
  t.attach(6);
  int pos_t;
  l.attach(7);
  int pos_l;

  pinMode(en, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(pul, OUTPUT);
  
  pinMode(l_in1, OUTPUT);
  pinMode(l_in2, OUTPUT);
  
   // define defualt position for sero motors
  int p= 90;
  int t= 67;
          
  
}

void loop()
{
  boolean s0 = digitalRead(c0);
  boolean s1 = digitalRead(c1);
  boolean s2 = digitalRead(c2);
  boolean s3 = digitalRead(c3);
  
  if (s3 == LOW && s2 == LOW && s1 == LOW && s0 == LOW)
  {
    digitalWrite = (l_in1, LOW);
    digitalWrite = (l_in2, LOW);
    
    pos_l=pos_l;
    l.write(pos_l);
    
    pos_t=pos_t;
    t.write(pos_t);
    
    pos_p=pos_p;
    p.write(pos_p);
    
    
  }
  
  
  if (s3 == LOW && s2 == LOW && s1 == LOW && s0 == HIGH)  // Switch motors to make the long linear actuator go up
  {
     digitalWrite = (l_in1, HIGH); // Switch motors to make the arm move up
     digitalWrite = (l_in2, LOW);
  }
  
  
  if (s3 == LOW && s2 == LOW && s1 == HIGH && s0 == LOW)  // Switch motors to make the long linear actuator go down
  {
    digitalWrite = (l_in1, LOW);
    digitalWrite = (l_in2, HIGH);
  }
  
  
  if (s3 == LOW && s2 == LOW && s1 == HIGH && s0 == HIGH)
  {
    // Switch motors to make the arm go left
  }
  
  
  if (s3 == LOW && s2 == HIGH && s1 == LOW && s0 == LOW)
  {
    // Switch motors to make the arm go right
  }
  
  
  if (s3 == LOW && s2 == HIGH && s1 == LOW && s0 == HIGH)  // Change angle by +1 degree and mirror on servo
  {
    for (int i=0; i<80; i++)
    {
      digitalWrite(dir,LOW);
      digitalWrite(en,HIGH);
      digitalWrite(pul,HIGH);
      delayMicroseconds(50);
      digitalWrite(pul,LOW);
      delayMicroseconds(50);
      delayMicroseconds(100);
      
      
    }
  }


    if (s3 == LOW && s2 == HIGH && s1 == HIGH && s0 == LOW)  // Change angle by -1 degree and mirror on servo
  {
    for (int i=0; i<80; i++)
    {
      digitalWrite(dir,LOW);
      digitalWrite(en,HIGH);
      digitalWrite(pul,HIGH);
      delayMicroseconds(50);
      digitalWrite(pul,LOW);
      delayMicroseconds(50);
      delayMicroseconds(100);
    }
      pos_t = 90;
      pos_t ++;
      t.write(pos_t);
      delay(15); 
   }


    if (s3 == LOW && s2 == HIGH && s1 == HIGH && s0 == HIGH)  // Look left
  {
    for(pos_p=pos_p; pos_p <= 179; pos_p++)
    {
      p.write(pos_p);
      delay(15);
    }      
  }
  
    if (s3 == HIGH && s2 == LOW && s1 == LOW && s0 == LOW)  //Look Right
  {
    for(pos_p=pos_p; pos_p >= 1; pos_p--)
    {
      p.write(pos_p);
      delay(15);
    } 
  }
  
    if (s3 == HIGH && s2 == LOW && s1 == LOW && s0 == HIGH)  // Press button
  {
    pos_l = pos_l;
    pos_l ++;
    l.write(pos_l);
    delay(15);
  }
  
    if (s3 == HIGH && s2 == LOW && s1 == HIGH && s0 == LOW)   // Retract button pressing actuator
  {
    for(pos_l=pos_l; pos_l >= 41; pos_l--)
    {
      p.write(pos_l);
      delay(15);
    }
  }
  
    if (s3 == HIGH && s2 == LOW && s1 == HIGH && s0 == HIGH)
  {
    // Reset Code
  }
  
}
