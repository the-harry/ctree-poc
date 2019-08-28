#define SIGPIN A0

int analogVal;

void setup()
{
  Serial.begin(9600);
  pinMode(SIGPIN, INPUT);
}

void loop()
{
  analogVal = analogRead(SIGPIN);
  Serial.println(String(analogVal));
  delayMicroseconds(1000);
}
