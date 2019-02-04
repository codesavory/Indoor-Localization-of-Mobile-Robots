#include <DistanceGP2Y0A41SK.h>

DistanceGP2Y0A41SK Dist;    //Declaration for IR
DistanceGP2Y0A41SK Dist2;

const int pwPin1 = 3;      //Declaration for ultrasonic //right
const int pwPin2 = 5;                                   //left
int triggerPin1 = 2;
int count=0;

void setup () {
  Serial.begin(9600);
  pinMode(pwPin1, INPUT);
  pinMode(pwPin2, INPUT);
  pinMode(triggerPin1, OUTPUT);
  Dist.begin(A0);                //right
  Dist2.begin(A1);              //left
}



void loop () 
{
 
  if(count<6)
    {
      Serial.write('a');
      count=count+1;
    }
}
      
  
