int PUL=7; //define Pulse pin
int DIR=6; //define Direction pin
int ENA=5; //define Enable Pin
void setup() {
  pinMode (PUL, OUTPUT);
  pinMode (DIR, OUTPUT);
  pinMode (ENA, OUTPUT);

}

void loop() {

for (int j=0; j<10; j++)  // j is the number of full forward rotations 
{
  for (int i=0; i<1600; i++)    //Forward 1 complete revolution
  {
    digitalWrite(DIR,LOW);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(50);
    digitalWrite(PUL,LOW);
    delayMicroseconds(50);
  }
}
  
  delay(1000);

for (int k=0; k<5; k++)  // k is the number of full forward rotations
{
  for (int i=0; i<1600; i++)   //Backward 1 complete revolution
  {
    digitalWrite(DIR,HIGH);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(50);
    digitalWrite(PUL,LOW);
    delayMicroseconds(50);
  }
  
}
  delay(1000);
}
