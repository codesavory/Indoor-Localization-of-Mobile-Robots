void setup()
{
  Serial.begin(9600);
  pinMode(4,INPUT);
  pinMode(8,INPUT);
}
int IR_1 = 4;
int IR_2 = 8;
void loop()
{
    Serial.println(digitalRead(4));
    Serial.println(digitalRead(8));
    //Serial.write(inByte);
    Serial.print("\n");
    delay(100);//delay for 1/10th of a second
}
