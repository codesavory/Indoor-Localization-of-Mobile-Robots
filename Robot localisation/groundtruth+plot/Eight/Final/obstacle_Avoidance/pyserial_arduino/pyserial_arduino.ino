void setup()
{
    Serial.begin(9600);
    Serial.println("Ready");
}
char inByte = ' ';
void loop()
{
    if (Serial.available())//only send data back when data is sent
    {
      inByte = Serial.read();//read the incoming data
      Serial.write(inByte);//send the data back in a new line
      //so that it is not all along one line
    }
    delay(100);//delay for 1/10th of a second
}
