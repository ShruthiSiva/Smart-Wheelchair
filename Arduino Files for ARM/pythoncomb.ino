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
int lin21 =6;
int lin22 = 7;

void setup() {
  // put your setup code here, to run once:
  pinMode(lin11,OUTPUT);
  pinMode(lin12,OUTPUT);
  pinMode(dir,OUTPUT);
  pinMode(en,OUTPUT);
  pinMode(pul,OUTPUT);
  pinMode(sv,OUTPUT);
  servov.attach(sv);
  servoh.attach(sh);
  servol.attach(sl);
  delay(20);

  servov.write(iniv);
  servoh.write(inih);
  servol.write(inil);
  delay(2000);
  servoh.detach();
  servol.detach();
  servov.detach();
  Serial.begin(9600);
}

int vertical;
int horizontal;
int reachout;
int pressing;

void loop() {
  if (Serial.available() > 0) {
    //----------------------------get to the default position-------------
    if (Serial.peek() == 'a') { 
      for (int j=0;j<60;j++){
        for (int i=0;i<80;i++){
          digitalWrite(dir, LOW);
          digitalWrite(en, HIGH);
          digitalWrite(pul, HIGH);
          delayMicroseconds(50);
          digitalWrite(pul, LOW);
          delayMicroseconds(1000);}
      }
      servov.attach(sv);
      delay(20);
      for (int j=0;j<60;j++){
          int x=servov.read();
          servov.write(x-1);
          iniv = x - 1;
          delay(50);
        }
       servov.detach();       
    }   //----------------------------obtain coordinates----------------------

      if (Serial.peek() == 'b') {//----------------set vertical value-------------------
        //Serial.read();
        vertical = Serial.parseInt();
        
      }
      if (Serial.peek() == 'c') {//--------------set horizontal value-------------------
        horizontal = Serial.parseInt();
      }

      if (Serial.peek() == 'd') {//----------------set reachout value-------------------
        reachout = Serial.parseInt();
      }

      if (Serial.peek() == 'e') {//----------------set pressing value-------------------
        pressing = Serial.parseInt();
      }

        if (Serial.peek() == 'f') {//---------------------operating!------------
          int ver;//----------------------vertical movement----------------
          if (vertical > 90){
            ver = vertical-90;
            for (int j=0;j<ver;j++){
              for (int i=0;i<80;i++){
                digitalWrite(dir, HIGH);
                digitalWrite(en, HIGH);
                digitalWrite(pul, HIGH);
                delayMicroseconds(50);
                digitalWrite(pul, LOW);
                delayMicroseconds(1000);
              }
            }
            servov.attach(sv);
            delay(20);
            for (int i=0;i<ver;i++){
              int x=servov.read();
              servov.write(x+1);
              iniv = x + 1;
              delay(50);
            }
            servov.detach();
          }
          else{
            ver = 90-vertical;
            for (int j=0;j<ver;j++){
              for (int i=0;i<80;i++){
                digitalWrite(dir, LOW);
                digitalWrite(en, HIGH);
                digitalWrite(pul, HIGH);
                delayMicroseconds(50);
                digitalWrite(pul, LOW);
                delayMicroseconds(1000);
              }
            }
            servov.attach(sv);
            delay(20);
            for (int i=0;i<ver;i++){
              int x=servov.read();
              servov.write(x-1);
              iniv = x - 1;
              delay(50);
            }
            servov.detach();           
          }
          int hor;//---------------horizontal movement--------------------
          if (horizontal>90){
            servoh.attach(sh);
            for (int i=0;i<hor;i++){
              delay(20);
              int y=servoh.read();
              servoh.write(y+1);
              delay(50);
              inih = y +1;
            }
            servoh.detach();
            digitalWrite(lin22, HIGH);
            digitalWrite(lin21,LOW);
            delay(500*ver);
            digitalWrite(lin22,LOW);
            digitalWrite(lin21,LOW);
          }
          else{
            ver = 90-vertical;
            servoh.attach(sh);
            for (int i=0;i<hor;i++){
              delay(20);
              int y=servoh.read();
              servoh.write(y-1);
              delay(50);
              inih = y -1;
            }
            servoh.detach();
            digitalWrite(lin22, LOW);
            digitalWrite(lin21,HIGH);
            delay(500*ver);
            digitalWrite(lin22,LOW);
            digitalWrite(lin21,LOW);            
          }
          for (int i=0;i<reachout;i++){//----------reaching out----------
            digitalWrite(lin12, HIGH);
            digitalWrite(lin11,LOW);
            delay(500);
            digitalWrite(lin12,LOW);
            digitalWrite(lin11,LOW); 
          }
          servol.attach(sl);
          for (int i=0;i<pressing;i++){//--------pressing----------------
            int u = servol.read();
            servol.write(u+1);
            delay(50);
            inil = u+1;
          }
          servol.detach();
          delay(500);///////////////////////////get back to default position///////////////////////
          servol.attach(sl);
          for (int i=0;i<pressing;i++){
            int u = servol.read();
            servol.write(u-1);
            delay(50);
            inil = u-1;
          }
          servol.detach();
          for (int i=0;i<reachout;i++){
            digitalWrite(lin12, LOW);
            digitalWrite(lin11,HIGH);
            delay(500);
            digitalWrite(lin12,LOW);
            digitalWrite(lin11,LOW); 
          }
          if (horizontal>90){
            servoh.attach(sh);
            for (int i=0;i<hor;i++){
              delay(20);
              int y=servoh.read();
              servoh.write(y-1);
              delay(50);
              inih = y -1;
            }
            servoh.detach();
            digitalWrite(lin22, LOW);
            digitalWrite(lin21,HIGH);
            delay(500*ver);
            digitalWrite(lin22,LOW);
            digitalWrite(lin21,LOW);
          }
          else{
            ver = 90-vertical;
            servoh.attach(sh);
            for (int i=0;i<hor;i++){
              delay(20);
              int y=servoh.read();
              servoh.write(y+1);
              delay(50);
              inih = y +1;
            }
            servoh.detach();
            digitalWrite(lin22, HIGH);
            digitalWrite(lin21,LOW);
            delay(500*ver);
            digitalWrite(lin22,LOW);
            digitalWrite(lin21,LOW);            
          }
          if (vertical > 90){
            ver = vertical-90;
            for (int j=0;j<ver;j++){
              for (int i=0;i<80;i++){
                digitalWrite(dir, LOW);
                digitalWrite(en, HIGH);
                digitalWrite(pul, HIGH);
                delayMicroseconds(50);
                digitalWrite(pul, LOW);
                delayMicroseconds(1000);
              }
            }
            servov.attach(sv);
            delay(20);
            for (int i=0;i<ver;i++){
              int x=servov.read();
              servov.write(x-1);
              iniv = x - 1;
              delay(50);
            }
            servov.detach();
          }
          else{
            ver = 90-vertical;
            for (int j=0;j<ver;j++){
              for (int i=0;i<80;i++){
                digitalWrite(dir, HIGH);
                digitalWrite(en, HIGH);
                digitalWrite(pul, HIGH);
                delayMicroseconds(50);
                digitalWrite(pul, LOW);
                delayMicroseconds(1000);
              }
            }
            servov.attach(sv);
            delay(20);
            for (int i=0;i<ver;i++){
              int x=servov.read();
              servov.write(x+1);
              iniv = x + 1;
              delay(50);
            }
            servov.detach();           
          }
          delay(30);
        }
     if (Serial.peek() == 'g') { //----------get back to vertical position-----------
      for (int j=0;j<60;j++){
        for (int i=0;i<80;i++){
          digitalWrite(dir,HIGH);
          digitalWrite(en, HIGH);
          digitalWrite(pul, HIGH);
          delayMicroseconds(50);
          digitalWrite(pul, LOW);
          delayMicroseconds(1000);}
      }
      servov.attach(sv);
      delay(20);
      for (int j=0;j<60;j++){
          int x=servov.read();
          servov.write(x+1);
          iniv = x + 1;
          delay(50);
        }
       servov.detach();       
    }

      while (Serial.available() > 0) {
        Serial.read();
      }
    }
  }



