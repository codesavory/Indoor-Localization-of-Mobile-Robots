#include <DistanceGP2Y0A41SK.h>

const int pwPin1 = 3;      //Declaration for ultrasonic //right
const int pwPin2 = 5;                                   //left
int triggerPin1 = 2;
long sensor1, sensor2, d1, d2;

void setup () {
  Serial.begin(9600);
  pinMode(pwPin1, INPUT);
  pinMode(pwPin2, INPUT);
  pinMode(triggerPin1, OUTPUT);
}


void read_sensor(){
  sensor1 = pulseIn(pwPin1, HIGH);
  d1 = sensor1/58; //makes the reported range the distance in centimeters
  delay(10); //helped make the range readings more stable
  sensor2 = pulseIn(pwPin2, HIGH);
  d2 = sensor2/58;
}

void start_sensor(){
  digitalWrite(triggerPin1,HIGH);
  delay(10);
  digitalWrite(triggerPin1,LOW);
}


char inByte = ' ';
void loop () 
{
  start_sensor();
  read_sensor();
  if(d1<100 && d2>100)
  {
    while(d1<100)
    {
      Serial.write('a');//turn left
      start_sensor();
      read_sensor();
      delay(210);
    }
  }
  else if(d1>100 && d2<100)
  {
    while(d2<100)
    {
      Serial.write('d');//turn right
      start_sensor();
      read_sensor();
      delay(210);
    }
  }
  else if(d1>100 && d2>100)
  {
    Serial.write('w');//go straight
  }
  else if (d1<100 && d2<100)
  {
    if (d1<d2)
    {
      while(d1<100)
      {
        Serial.write('a');//turn left
        start_sensor();
        read_sensor();
        delay(210);
      }
    }
    else if (d1>=d2)
    {
      while(d2<100)
      {
        Serial.write('d');//turn right
        start_sensor();
        read_sensor();
        delay(210);
      }
    }
  }
  delay(210);
}
