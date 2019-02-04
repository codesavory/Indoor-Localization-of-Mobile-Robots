//#include <DistanceGP2Y0A41SK.h>

//DistanceGP2Y0A41SK Dist;    //Declaration for IR
//int distance;

const int pwPin1 = 3;      //Declaration for ultrasonic
const int pwPin2 = 5;
int triggerPin1 = 2;
long sensor1, sensor2, d1, d2;

void setup () {
  Serial.begin(9600);
  pinMode(pwPin1, INPUT);
  pinMode(pwPin2, INPUT);
  pinMode(triggerPin1, OUTPUT);
  //Dist.begin(A0);
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

/*void ir_read(){
  distance = Dist.getDistanceCentimeter();
  Serial.print("Distance in centimeters: ");
  Serial.println(distance);
  delay(500);
}*/

char inByte = ' ';
void loop () {
  start_sensor();
  read_sensor();
  //ir_read();
  //Serial.write(d1);
  //Serial.write(d2);
  
  if(d1<=60 && d2>=60)
  {
    Serial.write('a');//turn left
  }
  else if(d2<=60 && d1>=60)
  {
    Serial.write('d');//turn right
  }
  else if(d1>=60 && d2>=60)
  {
    Serial.write('w');//go straight
  }
  else if(d1<=60 && d2<=60)
  {
    if(d1>d2)
    {
      Serial.write('d');//turn right
    }
    else if(d1=d2)
    {
      Serial.write('d');//turn right
    }
    else if(d1<d2)
    {
      Serial.write('a');//turn left
    }
  }
  delay(210);
}

