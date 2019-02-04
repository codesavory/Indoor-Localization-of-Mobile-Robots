#include <DistanceGP2Y0A41SK.h>

DistanceGP2Y0A41SK Dist;    //Declaration for IR
DistanceGP2Y0A41SK Dist2;
int distance1;
int distance2;

const int pwPin1 = 3;      //Declaration for ultrasonic //right
const int pwPin2 = 5;                                   //left
int triggerPin1 = 2;
long sensor1, sensor2, d1, d2;
int flag=0;

void setup () {
  Serial.begin(9600);
  pinMode(pwPin1, INPUT);
  pinMode(pwPin2, INPUT);
  pinMode(triggerPin1, OUTPUT);
  Dist.begin(A0);                //right
  Dist2.begin(A1);              //left
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

void ir_read(){
  distance1 = Dist.getDistanceCentimeter();
  delay(500);
  distance2 = Dist2.getDistanceCentimeter();
  //Serial.print("Distance in centimeters: ");
  //Serial.println(distance);
  delay(500);
}

char inByte = ' ';   
void loop () 
{
  start_sensor();
  read_sensor();
  Serial.print(d1);
      Serial.print(" ");
      Serial.print(d2);
       Serial.print(" ");
  //ir_read();
  
      Serial.print(distance1);
      Serial.print(" ");
      Serial.print(distance2);
      Serial.print("\n");
  //Serial.print("::");
 
  if(d1<50 && d2>50)
  {
    //Serial.write("Ultra:");
    flag=0;
    //Serial.write('a');//turn left
    if(d1<30)
    {
      ir_read();
      //Serial.print(distance1);
      if(distance1<=30 && distance1>15)
      {
         
  
        //Serial.write("\nIR:");
        //Serial.write('a');//turn left
      }
      else if(distance1<=15)
        {
          //Serial.write("s");
         
  
        }
    }
  }
  else if(d2<50 && d1>50)
  {
    //Serial.write("Ultra:");
    //Serial.write('d');//turn right
    flag=1;
    if(d2<30)
    {
      ir_read();  
      //Serial.print(distance2);
      if(distance2<=30 && distance2>15)
      {
        //Serial.write("\nIR:");
       
  //Serial.print("::");
  
      }
    }
  }
  else if(d1>50 && d2>50)
  {
    //Serial.write("Ultra:");
 
  
    Serial.write('w');//go straight
  }
  else if(d1<=50 && d2<=50)
  {
    //Serial.print("*");
    if(d1>d2)
    {
      //Serial.write("Ultra:");
      Serial.write('d');//turn right
      flag=1;
      if(d2<30)
      {
        ir_read();
        //Serial.print(distance2);
        if(distance2<=30 && distance2>15)
        {
          //Serial.write("\nIR:");
  
  //Serial.print("::");
  
          Serial.write('d');//turn right
        }
        else if(distance2<=15)
        {
          Serial.write("s");
        }
      }
    }
    else if(d1==d2)
    {
      //Serial.write("Ultra:");
      if (flag==1)
        Serial.write('d');//turn right
      else
        Serial.write('a');//left
        
  
    }
    else if(d1<d2)
    {
      //Serial.write("Ultra:");
      //Serial.write('a');//turn left
      flag=0;
      if(d1<30)
      {
        ir_read();
        //Serial.print(distance1);
        if(distance1<=30 && distance1>15)
        {
          //Serial.write("\nIR:");
          Serial.write('a');//turn left
      
  //Serial.print("::");
  
        }
        else if(distance1<=15)
        {
          Serial.write("s");
  
        }
      }
    }
  }
  Serial.write("\n\n");
  delay(210);
}

