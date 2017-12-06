#include<Servo.h>

Servo servov;
Servo servoh;
Servo servol;
int lin11 = 8;
int lin12 = 9;
int dir = 2;
int en = 13;
int pul = 4;
int sv = 12;
int sh = 10;
int sl = 11;
int inih = 90;
int iniv = 79;
int inil = 40;

void setup() {
  // put your setup code here, to run once:
  pinMode(lin11,OUTPUT);
  pinMode(lin12,OUTPUT);
  pinMode(dir,OUTPUT);
  pinMode(en,OUTPUT);
  pinMode(pul,OUTPUT);
  Serial.begin(9600);
  servov.attach(sv);
  servoh.attach(sh);
  servol.attach(sl);

  servov.write(iniv);
  servoh.write(inih);
  servol.write(inil);

  
}

void loop() {
  // put your main code here, to run repeatedly:
     int inByte = Serial.read();
    switch (inByte) {
      
      case 'a':// reach out 0001
        servov.write(iniv);
        servoh.write(inih);
        servol.write(inil);
        digitalWrite(lin12, HIGH);
        digitalWrite(lin11,LOW);
        delay(500);
        digitalWrite(lin12,LOW);
        digitalWrite(lin11,LOW);
        serialWrite('Done');
        break;
        
      case 'b': //back  0010
        servov.write(iniv);
        servoh.write(inih);
        servol.write(inil);
        digitalWrite(lin12, LOW);
        digitalWrite(lin11, HIGH);
        delay(500);
        digitalWrite(lin12, LOW);
        digitalWrite(lin11, LOW);
        serialWrite('Done');
        break;
      
      case 'c'://rotating down 0011
        servoh.write(inih);
        servol.write(inil);
        for (int i=0;i<80;i++){
          digitalWrite(dir, HIGH);
          digitalWrite(en, HIGH);
          digitalWrite(pul, HIGH);
          delayMicroseconds(50);
          digitalWrite(pul, LOW);
          delayMicroseconds(150);
          if (i==79){
          int x=servov.read();
          servov.write(x + 10);
          iniv = x + 10;
          delay(50);
          }
        }
        delay(1000);
        serialWrite('Done');
        break;
      
      case 'd': //rotating up 0100
        servov.write(iniv);
        servoh.write(inih);
        servol.write(inil);
        for (int i=0;i<80;i++){
          digitalWrite(dir, LOW);
          digitalWrite(en, HIGH);
          digitalWrite(pul, HIGH);
          delayMicroseconds(50);
          digitalWrite(pul, LOW);
          delayMicroseconds(150);
          if (i==79){
            int x=servov.read();
            servov.write(x - 1);
            delay(50);
            iniv = x - 1;
          }
          delay(15);
        }
        delay(1000);
        serialWrite('Done');
        break;
      
      case 'e': // turning left 0101
        servov.write(iniv);
        servol.write(inil);
        for (int i=0;i<10;i++){
        int y=servoh.read();
        servoh.write(y + 1);
        delay(50);
        inih = y + 1;}
        serialWrite('Done');
        break;
      
      case 'f': // turning right 0110
        servov.write(iniv);
        servol.write(inil);
        for (int i=0;i<10;i++){
        int z=servoh.read();
        servoh.write(z-1);
        delay(50);
        inih = z - 1;}
        serialWrite('Done');
        break;
        
      case 'g': //press 1001
        servov.write(iniv);
        servoh.write(inih);
        for (int i=0;i<10;i++){
          int u = servol.read();
          servol.write(u+1);
          delay(50);
          inil = u+10;
        }
        serialWrite('Done');
        break;
        
      case 'h': //move back 1010
        servoh.write(inih);
        servov.write(iniv);
        for (int i=0;i<10;i++){
          int v = servol.read();
          servol.write(v-1);
          inil = v-1;
          delay(50);
        }
        serialWrite('Done');
        break;
        
    }
    
}
