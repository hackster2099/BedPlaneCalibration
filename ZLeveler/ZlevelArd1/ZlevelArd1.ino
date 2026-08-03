#include <LiquidCrystal.h>
#include <SoftwareSerial.h>

// setting up the LED screen
const int regSel = 11, enable = 12, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(regSel, enable, d4,d5,d6,d7);
SoftwareSerial mySerial(8, 9); // 8 is RX and 9 is TX

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  lcd.begin(16,2);  

}

String dataRoll = "";
String dataGeneral = "";

void loop() {

  while(mySerial.available()){
  
    char c = mySerial.read();

    if(c == ',') {
      
      String *dataPitch = &dataGeneral;

      while(c != '\n'){

        c = mySerial.read();
        
  
        if(c == '\n'){

          break;

        }

        dataRoll+=c;

      }
    
      lcd.setCursor(0,0);
      lcd.print("Pitch: " + *dataPitch);
        
      lcd.setCursor(0,1);
      lcd.print("Roll: " + dataRoll);

      delay(500);

      lcd.clear();
        
      dataGeneral = "";
      dataRoll = "";
        
    }

    else if(c == '\n'){

      lcd.setCursor(0,0);
      lcd.print(dataGeneral);
      delay(500);

      dataGeneral = "";
      lcd.clear();

    }

    else {

      dataGeneral+=c;

    }

  }
}
