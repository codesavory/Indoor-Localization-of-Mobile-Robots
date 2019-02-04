/*
Test code for the Arduino control device
The pwPin's may change depending on the Arduino hardware, and the pins being utilized.
Written by Tom Bonar for testing
Sensors being used for this code are the XL-MaxSonar Sensors from MaxBotix
*/
const int pwPin1 = 3;
const int pwPin2 = 5;
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
  delay(1);
  digitalWrite(triggerPin1,LOW);
}

//This section of code is if you want to print the range readings to your computer too remove this from the code put /* before the code section and */ after the code
void printall(){         
  Serial.print("S1");
  Serial.print("-");
  Serial.print(d1);
  Serial.print(" ");
  Serial.print("S2");
  Serial.print("-");
  Serial.print(d2); 
  Serial.println();
}

void loop () {
  start_sensor();
  read_sensor();
  printall();
  /*if(d1 <=50 && d2<=50)
  {
    Serial.write('d');//turn right
  }
  else if(d1 <=50 && d2>=50)
  {
    Serial.write('a');//turn left
  }
  else if(d1 >=50 && d2<=50)
  {
    Serial.write('d');//turn right
  }
  else if(d1 >=50 && d2>=50)
  {
    Serial.write('w');//go straight
  }*/
  delay(210);  //delay before the void loop starts the section again.  Make this match the refresh rate times how ever many sensors are in the chain.  I typically add 10 to help with any secondary reflections
}
