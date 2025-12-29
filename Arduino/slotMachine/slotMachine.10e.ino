#include <LCDI2C_Multilingual.h>

LCDI2C_Symbols lcd(0x27,16,2);

bool lcd_prepared=false;
const int Rpin=7,Gpin=12,LEDpin=10,SWITCHpin=3;//
int Rstate=0,Gstate=0,cheating=0;
int have5=0,have4=0,have3=0,have2=0;
int lottNum[5];
int prii[10]={0}; //index[0,9],prizing

void setup() {
  Serial.begin(9600);
  pinMode(Rpin,INPUT_PULLUP);
  pinMode(Gpin,INPUT_PULLUP);
  pinMode(LEDpin,OUTPUT);
  pinMode(SWITCHpin,INPUT);
  lcd.init();
  lcd.backlight();
  lcd.println("Power connected");
  lcd.println("successfully :)");
  randomSeed(analogRead(A0));
  delay(800);
}

void loop() {
  delay(200);
  Rstate=digitalRead(Rpin);
  Gstate=digitalRead(Gpin);

  if (Gstate==LOW) {
    lcd.clear();
    lcd.println("READY!");
    delay(1500);
    lcd.clear();
    lcd.println("press RED button");
    lcd.println("to START!");
    cheating=digitalRead(SWITCHpin);

    //reset
    lcd_prepared=true;
    have5=0,have4=0,have3=0,have2=0;
    delay(200);
  }

  if (Rstate==LOW and lcd_prepared==true) {
    lcd.clear();
    lcd.print("rollinggg...");
    delay(2300);
    lcd.clear();
    lcd.println("your num are >>");

    if (cheating==1) { //cheeeeeat
      for (int i=0;i<5;i++) {
        lottNum[i]=5;
        lcd.print(lottNum[i]);
        lcd.print(".");
        delay(1000);
        }
    } else { //常態生成
      for (int i=0;i<5;i++) {
        lottNum[i]=random(0,10);
        lcd.print(lottNum[i]);
        lcd.print(".");
        delay(1000);
        }
      }
      
      //note the Num in prii
    memset(prii,0,sizeof(prii)); //clear prii first
    for (int i=0;i<5;i++) {
      prii[lottNum[i]]++;
    }

      //計算他媽幾同幾異
    for (int i=0;i<10;i++) {
      int k=prii[i];
      if (k==5) {
        have5++;
        break;
      } else if (k==4) {
        have4++;
        break;
      } else if (k==3) {
        have3++;
      } else if (k==2) {
        have2++;
      }
    }

    //show lottNum again
    lcd.clear();
    lcd.print("<");
    for (int i=0;i<5;i++) {
      lcd.print(lottNum[i]);
      lcd.print(".");
    }
    lcd.println(">");
    delay(800);

    //print the out come
    if (have5==1) {
      lcd.print("SUPER WINNER!");
    } else if (have4==1) {
      lcd.print("four of a kind!");
    } else if (have3==1 and have2==1) {
      lcd.print("full house");
    } else if (have3==1 and have2==0) {
      lcd.print("three of a kind");
    } else if (have2==2) {
      lcd.print("two pairs");
    } else if (have2==1) {
      lcd.print("one pair");
    } else {
      lcd.print("no pair");
    }

    //some reactions
    if (have5==1 or have4==1) {
      digitalWrite(LEDpin,HIGH);
      delay(7000);
      digitalWrite(LEDpin,LOW);
    }

    //cycle reset
    lcd_prepared=false;
    have5=0,have4=0,have3=0,have2=0;
  }
}