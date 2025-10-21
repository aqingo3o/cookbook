const int IN1 = 5;           // L298N IN1 to Arduino D5~  (black)
const int IN2 = 6;           // L298N IN2 to Arduino D6~  (white)
const int IN3 = 9;           // L298N IN3 to Arduino D9~  (purple)
const int IN4 = 10;          // L298N IN4 to Arduino D10~ (brown)

void setup() {
  Serial.begin(9600);
  pinMode(5,OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  delay(500);
}

void stoppp() {
  analogWrite(IN1, 0);
  analogWrite(IN2, 0);
  analogWrite(IN3, 0);
  analogWrite(IN4, 0);
}

// IN3, IN1
// IN2, IN4
void frontt(int spdd) {
  analogWrite(IN2, spdd);
  analogWrite(IN4, spdd);
  analogWrite(IN1, 0);
  analogWrite(IN3, 0);
}
void backk(int spdd) {
  analogWrite(IN1, spdd);
  analogWrite(IN3, spdd);
  analogWrite(IN2, 0);
  analogWrite(IN4, 0);
}

const int timee = 100;
const int spd = 200;  // 就是動
void loop() {
  
  int senVal_back = analogRead(A0);  // 電池那端
  int senVal_front = analogRead(A1); // 萬向輪那端

  if (senVal_back < senVal_front && senVal_back < 300) {
    backk(spd);
    delay(timee);
  } else if (senVal_front < senVal_back && senVal_front < 300) {
    frontt(spd);
    delay(timee);
  } else {
    stoppp();
  }
}
