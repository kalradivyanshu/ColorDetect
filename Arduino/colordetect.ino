int ledgreen=9;
int ledblue=10;
int ledred=11;
int tx=1;
int rx=0;
String myString="";


void setup(){
  Serial.begin(9600);
  pinMode(ledred, OUTPUT);
  pinMode(ledgreen, OUTPUT);
  pinMode(ledblue, OUTPUT);
  pinMode(tx, OUTPUT);
  pinMode(rx, INPUT);
}

void loop(){
    int i=0;
    int m=0;
    delay(500);                                         
    if (Serial.available() > 0) {      
       while (Serial.available() > 0) {
         myString += (char)Serial.read();
       }
        Serial.print("Input:");
        Serial.println(myString);
       int commaIndex = myString.indexOf(',');
      //  Search for the next comma just after the first
      int secondCommaIndex = myString.indexOf(',', commaIndex+1);
      String firstValue = myString.substring(0, commaIndex);
String secondValue = myString.substring(commaIndex+1, secondCommaIndex);
String thirdValue = myString.substring(secondCommaIndex+1,myString.length()); // To the end of the string
Serial.println(thirdValue);
myString="";
int b = firstValue.toInt();
int g = secondValue.toInt();
int r = thirdValue.toInt();
Serial.print("RED:");
Serial.print(r);
Serial.print("Blue:");
Serial.print(b);
Serial.print("Green:");
Serial.println(g);
      analogWrite(ledred,255-r);
      analogWrite(ledblue,255-b);
      analogWrite(ledgreen,255-g);
}}
     
    
  
