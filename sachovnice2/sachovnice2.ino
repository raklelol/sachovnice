#include <FastLED.h>
#define pocetled 60
#define pin 2
#define minus1 3
#define minus2 4
#define plus1 5
#define plus2 6
#define leddata 12
int ledplocha[2][2];
int plocha[2][2];
int plus[2];
int minus[2];
int minulystav[2][2];
CRGB led[pocetled];
int datacislo;
String data;
String cislo = "";
void setup() {
  Serial.begin(9600);
  pinMode(pin, INPUT);
  pinMode(minus1, OUTPUT);
  pinMode(minus2, OUTPUT);
  pinMode(plus1, OUTPUT);
  pinMode(plus2, OUTPUT);
  ledplocha[0][0] = 0;
  ledplocha[0][1] = 0;
  ledplocha[1][0] = 0;
  ledplocha[1][1] = 0;
  minulystav[0][0] = 1;
  minulystav[0][1] = 1;
  minulystav[1][0] = 1;
  minulystav[1][1] = 1;
  minus[0] = 3;
  minus[1] = 4;
  plus[0] = 5;
  plus[1] = 6;
  plocha[0][0] = 1;
  plocha[0][1] = 1;
  plocha[1][0] = 1;
  plocha[1][1] = 1;
  FastLED.setBrightness(100);
  FastLED.addLeds<WS2812B, leddata, GRB>(led, pocetled);
}

void loop() {
  sachovnice();
  zmena();
  if (Serial.available() > 0) {
    fill_solid(led, pocetled, CRGB(0, 0, 0));
    FastLED.show();
    data = Serial.readStringUntil('\n');
  }
  for (int i = 0; i < data.length(); i++) {
    if (data.charAt(i) != ',' and data.charAt(i) != 'f') {

      cislo = cislo + data.charAt(i);

    }
    if (data.charAt(i) == ',') {
      datacislo = cislo.toInt();
      //Serial.println(datacislo);
      ledky();
      cislo = "";
    }
  }
}


/*
  digitalWrite(11, LOW);
  Serial.println(digitalRead(A0));
*/


void sachovnice() {
  for (int radek = 0; radek < 2; radek++) {
    for (int sloupec = 0; sloupec < 2; sloupec++) {
      digitalWrite(plus[sloupec], HIGH);
      digitalWrite(minus[radek], HIGH);
      delay(10);
      plocha[sloupec][radek] = digitalRead(pin);
      digitalWrite(plus[sloupec], LOW);
      digitalWrite(minus[radek], LOW);
    }
  }
}

void vypis() {
  for (int radek = 0; radek < 2; radek++) {
    for (int sloupec = 0; sloupec < 2; sloupec++) {
      Serial.print(plocha[sloupec][radek]);
    }
    Serial.println(" ");
  }
  Serial.println(" ");
}

void zmena() {
  for (int radek = 0; radek < 2; radek++) {
    for (int sloupec = 0; sloupec < 2; sloupec++) {
      if (plocha[sloupec][radek] != minulystav[sloupec][radek]) {
        Serial.print(sloupec);
        Serial.print(radek);
        Serial.println(plocha[sloupec][radek]);
        minulystav[sloupec][radek] = plocha[sloupec][radek];

      }
    }
  }
}
void ledky() {

  led[datacislo - 1] = CRGB::White;
  FastLED.show();


}
