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

const int s0 = A0;
const int s1 = A1;
const int s2 = A2;
const int s3 = A3;

// declare outputs pins for the servo motors on top

const int p = 5;  // p = pan servo 
const int t = 6;  // t = tilt servo

// declare output pins for stepper motor control

const int en1 = 7;
const int en2 = 8;
const int dir = 9;
const int pul = 10;

// declare output pins for the linear actuators

const int l_dir = 11;
const int l_en = 12;
const int s_dir = 2;
const int s_en = 3; 


void setup() {
  
  pinMode(s0, INPUT);
  pinMode(s1, INPUT);
  pinMode(s2, INPUT);
  pinMode(s2, INPUT);
  
  pinMode(p, OUTPUT);
  pinMode(t, OUTPUT);
  
  pinMode(en, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(pul, OUTPUT);
  
  pinMode(l_dir, OUTPUT);
  pinMode(s_dir, OUTPUT);
  pinMode(l_en, OUTPUT);
  pinMode(s_en, OUTPUT);
           
  // define defualt position for servo motors
  int x= 90;
  int y= 67;
  
}

void loop()
{
  boolean c0 = digitalRead(s0);
  boolean c1 = digitalRead(s1);
  boolean c2 = digitalRead(s2);
  boolean c3 = digitalRead(s3);
          
  if (c0 == LOW && c1 == LOW && c2 == LOW && c3 == LOW)
  {
    // Stop all motors
            digitalWrite(l_dir, LOW);
            digitalWrite(l_en, LOW);
            digitalWrite(s_dir, LOW);
            digitalWrite(s_en, LOW);
  }
  
  
  if (c0 == LOW && c1 == LOW && c2 == LOW && c3 == LOW)
  {
     // Switch motors to make the arm move up              
            digitalWrite(l_dir, LOW);
            digitalWrite(l_en, HIGH);
            digitalWrite(s_dir, LOW);
            digitalWrite(s_en, LOW);
            delay(1000);
  }
  
  
  if (c0 == LOW && c1 == LOW && c2 == LOW && c3 == LOW)
  {
    // Switch motors to make the arm go down
            digitalWrite(l_dir, HIGH);
            digitalWrite(l_en, HIGH);
            digitalWrite(s_dir, LOW);
            digitalWrite(s_en, LOW);
            delay(1000);
  }
  
  
  if (c0 == LOW && c1 == LOW && c2 == LOW && c3 == LOW)
  {
    // Switch motors to make the arm go left
            
            digitalWrite(l_dir, LOW);
            digitalWrite(l_en, LOW);
            digitalWrite(s_dir, LOW);
            digitalWrite(s_en, LOW);
            delay(1000);
            
            //make bottom stepper motor spin clockwise 100 steps
              
            for (int i=0; i<100; i++)    //Forward 1/16 of complete revolution
            {
                    digitalWrite(dir,HIGH);
                    digitalWrite(en1,HIGH);
                    digitalWrite(pul,HIGH);
                    delayMicroseconds(50);
                    digitalWrite(pul,LOW);
                    delayMicroseconds(50);
            }
            // make servo motor mirror motor in bottom
            analogWrite(p, x+1);
              
  }
  
  
  if (c0 == LOW && c1 == LOW && c2 == LOW && c3 == LOW)
  {
    // Switch motors to make the arm go right
            digitalWrite(l_dir, LOW);
            digitalWrite(l_en, LOW);
            digitalWrite(s_dir, LOW);
            digitalWrite(s_en, LOW);
            delay(1000);
              
              //make bottom stepper motor spin counter-clockwise 100 steps
              
            for (int i=0; i<100; i++)    //Forward 1/16 of complete revolution
            {
                    digitalWrite(dir,LOW);
                    digitalWrite(en1,HIGH);
                    digitalWrite(pul,HIGH);
                    delayMicroseconds(50);
                    digitalWrite(pul,LOW);
                    delayMicroseconds(50);
            }
            // Make servo motor mirror bottom motor
            analogWrite(p, x-1);
              
            
  }
  
  
  if (c0 == LOW && c1 == LOW && c2 == LOW && c3 == LOW)
  {
    // Switch motors to make the arm go forward
            digitalWrite(l_dir, LOW);
            digitalWrite(l_en, HIGH);
            digitalWrite(s_dir, LOW);
            digitalWrite(s_en, LOW);
            delay(1000);
              
            for (int j=0; j<100; j++)    //Forward 1/16 of complete revolution
            {
                    digitalWrite(DIR,LOW);
                    digitalWrite(ENA,HIGH);
                    digitalWrite(PUL,HIGH);
                    delayMicroseconds(50);
                    digitalWrite(PUL,LOW);
                    delayMicroseconds(50);
            }
            // make servo motor mirror bottom angle 
            analogWrite(t, y+1);
            
            
  }


  if (c0 == LOW && c1 == LOW && c2 == LOW && c3 == LOW))
  {
    // Switch motors to make the arm come backward
            digitalWrite(l_dir, HIGH);
            digitalWrite(l_en, HIGH);
            digitalWrite(s_dir, LOW);
            digitalWrite(s_en, LOW);
            delay (1000);
            
            for (int j=0; j<100; j++)    //Forward 1/16 of complete revolution
            {
                    digitalWrite(DIR,HIGH);
                    digitalWrite(ENA,HIGH);
                    digitalWrite(PUL,HIGH);
                    delayMicroseconds(50);
                    digitalWrite(PUL,LOW);
                    delayMicroseconds(50);
            }
            // make servo motor mirror bottom angle 
            analogWrite(t, y-1);
            
  }


  if (c0 == LOW && c1 == LOW && c2 == LOW && c3 == LOW)
  {
            // Use Ultrasonic sensor to measure distance to the button
            long duration, inches, cm;
            digitalWrite(trig, LOW);
            delayMicroseconds(2);
            digitalWrite(trig, HIGH);
            delayMicroseconds(5);
            digitalWrite(trig, LOW);

            duration = pulseIn(echo, HIGH);
  
            inches = microsecondsToInches(duration);
            cm = microsecondsToCentimeters(duration);

            Serial.print(inches);
            Serial.print("in, ");
            Serial.print("\n");
            Serial.print(cm);  
            Serial.print("cm");
            Serial.print("\n");
            Serial.print("\n");
            Serial.print("\n");
              
            // Convert distance to time accounting for the speed of the linear actuator
            int time;
            time= (cm*1000)+500;
            
            // Freeze long actuator 
            digitalWrite(l_dir, LOW);
            digitalWrite(l_en, LOW);
              
            // Make small actuator go forward for measured distance plus travel distance for pressing the button
            digitalWrite(s_dir, LOW);
            digitalWrite(s_en, HIGH);
            delay(time);
              
            // Return Actuator
              
            digitalWrite(s_dir, HIGH);
            digitalWrite(s_en, HIGH);
            delay(time);
              
            
  }
  
}
