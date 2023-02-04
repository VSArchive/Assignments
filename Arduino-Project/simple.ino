int SERVO=3;
int MOTOR2=2;
int MOTOR2DIR=4;
int BEEPER=5;
int LED=6;
int pushButtonSiren=7;
int pushButtonMotor=8;
int pushButtonDirection=9;
int pushButtonLED=10;

void setup()
{
	pinMode(SERVO, OUTPUT);
	pinMode(MOTOR2, OUTPUT);
	pinMode(MOTOR2DIR, OUTPUT);
	pinMode(BEEPER, OUTPUT);
	pinMode(pushButtonSiren, INPUT);
	pinMode(pushButtonMotor, INPUT);
	pinMode(pushButtonDirection, INPUT);
	pinMode(pushButtonLED, INPUT);
}

void loop()
{
	digitalWrite(SERVO, HIGH);
	int siren = digitalRead(pushButtonSiren);
	if (siren == HIGH)
	{
		digitalWrite(BEEPER, HIGH);
	}
	else if (siren == LOW)
	{
		digitalWrite(BEEPER, LOW);
	}
	
	int motorStart = digitalRead(pushButtonMotor);
	if (motorStart == HIGH)
	{
		digitalWrite(SERVO, HIGH);
	}
	else if (motorStart == LOW)
	{
		digitalWrite(SERVO, LOW);
	}
	
	int motorDirection = digitalRead(pushButtonDirection);
	if (motorStart == HIGH)
	{
		digitalWrite(MOTOR2DIR, HIGH);
	}
	else if (motorStart == LOW)
	{
		digitalWrite(MOTOR2DIR, LOW);
	}
	
	int ledONOFF = digitalRead(pushButtonLED);
	if (ledONOFF == HIGH)
	{
		digitalWrite(LED, HIGH);
	}
	else if (ledONOFF == LOW)
	{
		digitalWrite(LED, LOW);
	}
}
