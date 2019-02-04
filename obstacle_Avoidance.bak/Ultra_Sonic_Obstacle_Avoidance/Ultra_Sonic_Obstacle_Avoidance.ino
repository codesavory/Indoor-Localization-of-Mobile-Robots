const int triggerPin=2;
const int anPin1 = 0;
const int anPin2 = 1;
long anVolt1,anVolt2;
void setup()
{
  Serial.begin(9600);
  pinMode(triggerPin,OUTPUT);
  delay(200);
}
void start_sensor()
{
  digitalWrite(triggerPin,HIGH);
  delay(1);
  digitalWrite(triggerPin,LOW);
}
void read_sensor()
{
  anVolt1 = analogRead(anPin1);
  anVolt2 = analogRead(anPin2);
}
char inByte = ' ';
void loop()
{
  start_sensor();
  read_sensor();
  /*if(anVolt1 <=50 && anVolt2<=50)
  {
    Serial.write('d');//turn right
  }
  else if(anVolt1 <=50 && anVolt2>=50)
  {
    Serial.write('a');//turn left
  }
  else if(anVolt1 >=50 && anVolt2<=50)
  {
    Serial.write('d');//turn right
  }
  else if(anVolt1 >=50 && anVolt2>=50)
  {
    Serial.write('w');//go straight
  }*/
  Serial.print("S1=");
  Serial.print(anVolt1);
  Serial.print("cm");
  
  Serial.print(" S2=");
  Serial.print(anVolt2);
  Serial.print("cm");
  
  Serial.print("\n");
  delay(200);
}
