const int IN1 = 5;           // L298N IN1 to Arduino D5~  (black)
const int IN2 = 6;           // L298N IN2 to Arduino D6~  (white)
const int IN3 = 9;           // L298N IN3 to Arduino D9~  (purple)
const int IN4 = 10;          // L298N IN4 to Arduino D10~ (brown)
float baseline = 0; // golbal

void setup() {
  Serial.begin(9600);
  pinMode(5,OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(20, OUTPUT); // LED
  delay(500);

  // envLight_sampling
  long sumA0 = 0;
  long sumA1 = 0;
  digitalWrite(20, HIGH);
  for (int i=0; i<10; i++) {
    int senVal_back = analogRead(A0);  // 電池那端（後）
    int senVal_front = analogRead(A1); // 萬向輪那端（前）
    sumA0 += senVal_back;
    sumA1 += senVal_front;
    delay(1000);
  }
  baseline = (sumA0+sumA1) / 20; //實驗室平均光
  digitalWrite(20, LOW);
  Serial.print("AVG =  ");
  Serial.print(baseline);
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

/*
// 小實驗的場合
void loop() {
  
  int senVal_back = analogRead(A0);  // 電池那端
  int senVal_front = analogRead(A1); // 萬向輪那端
  Serial.println("batt:");
  Serial.println(senVal_back);
  Serial.println("whell:");
  Serial.println(senVal_front);
  delay(1000);
}
*/

// para
int spd = 0;               // 先設零
int basespd = 50;          // 不確定，先設這個
const int timee = 100;     
const int verybright = 50; // 35+1
const int delta = 30;      // 有效差值
 
// 車車
void loop() {
  int senVal_back = analogRead(A0);  // 電池那端（後）
  int senVal_front = analogRead(A1); // 萬向輪那端（前）
                                                                        // 非常亮區間
  if (senVal_back < senVal_front && senVal_back < verybright) {         // 向後，非常亮
    backk(basespd);
    delay(timee);
  } else if (senVal_front < senVal_back && senVal_front < verybright) { // 向前，非常亮
    frontt(basespd);
    delay(timee);
  } else {                                                                      // 進入普通區間
    if ((senVal_front-senVal_back) > delta  && senVal_back < baseline) {        // 向後，普通區間
      spd = map(senVal_back, verybright+10, baseline+15, basespd, 255);
      backk(spd);
      delay(timee);
    } else if ((senVal_back-senVal_front) > delta  && senVal_front < baseline) {  // 向前，普通區間
      spd = map(senVal_front, verybright+10, baseline+15, basespd, 255);
      frontt(spd);
      delay(timee);
    } else {                                                                      // 剩餘情況全部先停
      stoppp();
    }
  }
}
