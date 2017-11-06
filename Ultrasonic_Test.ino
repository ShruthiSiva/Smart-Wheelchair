int trig = 10; // attach pin 10 to Trig
int echo = 11; //attach pin 11 to Echo
int led = 13; //Pin 13 is an LED

void setup()
{
pinMode(12, OUTPUT); // declare pin 12 as ground
pinMode(9, OUTPUT); // declare pin 9 as Vcc
digitalWrite(12, LOW);
digitalWrite(9, HIGH);
pinMode(led, OUTPUT);

Serial.begin(9600);  // initialize serial communication:
}

long microsecondsToInches(long microseconds)
{
return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds)
{
return microseconds / 29 / 2;
}

void loop()
{
// establish variables for duration of the ping,
// and the distance result in inches and centimeters:

long duration, inches, cm;

// The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
// Give a short LOW pulse beforehand to ensure a clean HIGH pulse:

pinMode(trig, OUTPUT);
digitalWrite(trig, LOW);
delayMicroseconds(2);
digitalWrite(trig, HIGH);
delayMicroseconds(5);
digitalWrite(trig, LOW);

pinMode(echo,INPUT);
duration = pulseIn(echo, HIGH);

// convert the echo time into distance

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


delay(100); // Adds 100 ms delay for stability
  
}
