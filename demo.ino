#include<Servo.h>
Servo servo1;
Servo servo2;
Servo linservo;

int s1 = 9;
int s2 =10;
int ste_dir = 2;
int ste_en = 3;
int ste_pul = 4;
int lins = 5;
int lin11 = 7;
int lin12 = 8;
int trig = 11;
int echo = 12;

void setup() {
  // put your setup code here, to run once:
  pinMode(s1,OUTPUT);
  pinMode(s2,OUTPUT);
  pinMode(ste_dir,OUTPUT);
  pinMode(ste_en,OUTPUT);
  pinMode(ste_pul,OUTPUT);
  pinMode(lin11,OUTPUT);
  pinMode(lin12,OUTPUT);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  pinMode(lins,OUTPUT);

  servo1.attach(s1);
  servo2.attach(s2);
  linservo.attach(lins);
  
}

long microsecondsToCentimeters(long microseconds)
{
  return microseconds / 29 / 2;
}

void loop() 
{
  // put your main code here, to run repeatedly:
  for (int j=0; j<3; j++)  // j is the number of full forward rotations 
  {
    for (int i=0; i<1600; i++)    //Forward 1 complete revolution
    {
      digitalWrite(ste_dir,LOW);
      digitalWrite(ste_en,HIGH);
      digitalWrite(ste_pul,HIGH);
      delayMicroseconds(50);
      digitalWrite(ste_pul,LOW);
      delayMicroseconds(50);
      delay(1);
    }
  }
  delay(500);

  servo1.write(60);              // tell servo to go to position in variable 'pos'
  delay(200); 
  servo2.write(180);
  delay(800);

  digitalWrite(lin11, HIGH);
  digitalWrite(lin12, LOW);
  delay(5000);

  //for linear unknown：measure distance, reach out, and get back
  double cm,angle,duration;
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(5);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH);
  cm = microsecondsToCentimeters(duration);
  angle = cm*9/7;
  linservo.write(angle);
  delay(1000);

  // undo everything from now on
  linservo.write(0);
  delay(1000);
  
  digitalWrite(lin11,LOW);
  digitalWrite(lin12,HIGH);
  delay(5000);

  servo1.write(0);              
  delay(200); 
  servo2.write(0);
  delay(800);

  for (int j=0; j<3; j++)
  {
    for (int i=0; i<1600; i++)
    {
      digitalWrite(ste_dir,HIGH);
      digitalWrite(ste_en,HIGH);
      digitalWrite(ste_pul,HIGH);
      delayMicroseconds(50);
      digitalWrite(ste_pul,LOW);
      delayMicroseconds(50);
      delay(1);
    }
  }
}
