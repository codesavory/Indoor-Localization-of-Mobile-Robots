// Includes the Servo library
#include <Servo.h>. 
// Defines Tirg and Echo pins of the Ultrasonic Sensor
const int trigPin = 10;
const int echoPin = 11;
// Variables for the duration and the distance
long duration;
int distance;
Servo myServo; // Creates a servo object for controlling the servo motor
void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600);
  myServo.attach(12); // Defines on which pin is the servo motor attached
  myServo.write(90);
  int flag=0;//miss flag=0
  int ang1,ang2;
}
void loop() {
  
  for(int i=90;i>=15;i--)
  {  
    myServo.write(i);
    delay(30);
    distance = calculateDistance();// Calls a function for calculating the distance measured by the Ultrasonic sensor for each degree
    if(distance<=50 && flag==0)//hit
    {
      flag=1;//hit flag set
      ang1=90 - i;//hit angle
    }
    if(distance>=50 && flag==1)
    {
        flag=0;
        ang2=90-i;
        decide_move(ang1,ang2);
    }
    Serial.print("Right");
    Serial.print(i); // Sends the current degree into the Serial Port
    Serial.print(","); // Sends addition character right next to the previous value needed later in the Processing IDE for indexing
    Serial.print(distance); // Sends the distance value into the Serial Port
    Serial.print(".\n\n"); // Sends addition character right next to the previous value needed later in the Processing IDE for indexing
  }
  for(int i=15;i<=90;i++)
  {  
    myServo.write(i);
    delay(30);
    distance = calculateDistance();
    if(distance<=50 && flag==0)//hit
    {
      flag=1;//hit flag set
      ang1=90-i;//hit angle
    }
    if(distance>=50 && flag==1)
    {
        flag=0;
        ang2=90-i;
        decide_move(ang1,ang2);
    }
    Serial.print("Return Left");
    Serial.print(i);
    Serial.print(",");
    Serial.print(distance);
    Serial.print(".\n\n");
  }
  for(int i=90;i<=165;i++)
  {  
  myServo.write(i);
  delay(30);
  distance = calculateDistance();
  if(distance<=50 && flag==0)//hit
    {
      flag=1;//hit flag set
      ang1=90-i;//hit angle
    }
    if(distance>=50 && flag==1)
    {
        flag=0;
        ang2=90-i;
        decide_move(ang1,ang2);
    }
  Serial.print("Left");
  Serial.print(i);
  Serial.print(",");
  Serial.print(distance);
  Serial.print(".\n\n");
  }
  for(int i=165;i>=90;i--)
  {  
  myServo.write(i);
  delay(30);
  distance = calculateDistance();
  if(distance<=50 && flag==0)//hit
    {
      flag=1;//hit flag set
      ang1=90-i;//hit angle
    }
    if(distance>=50 && flag==1)
    {
        flag=0;
        ang2=90-i;
        decide_move(ang1,ang2);
    }
  Serial.print("Return Right");
  Serial.print(i);
  Serial.print(",");
  Serial.print(distance);
  Serial.print(".\n\n");
  }
  
 // Repeats the previous lines from 165 to 15 degrees
  
  
}
int decide_move(int ang1,int ang2)
{
   int angle=ang2-ang1;
}
// Function for calculating the distance measured by the Ultrasonic sensor
int calculateDistance(){ 
  
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); // Reads the echoPin, returns the sound wave travel time in microseconds
  distance= duration*0.034/2;
  return distance;
}
