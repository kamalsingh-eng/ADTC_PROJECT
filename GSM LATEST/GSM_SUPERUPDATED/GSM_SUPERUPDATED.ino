//Viral Science www.viralsciencecreativity.com www.youtube.com/c/viralscience
//Realtime GPS Tracker with Nodemcu ESP8266
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

static const int RXPin = 4, TXPin = 5;   // GPIO 4=D2(conneect Tx of GPS) and GPIO 5=D1(Connect Rx of GPS
static const uint32_t GPSBaud = 9600; //if Baud rate 9600 didn't work in your case then use 4800

TinyGPSPlus gps; // The TinyGPS++ object
WidgetMap myMap(V0);  // V0 for virtual pin of Map Widget

SoftwareSerial ss(RXPin, TXPin);  // The serial connection to the GPS device

int f_flag = 1;
int r_flag = 1;
int f_count = 0;
int r_count = 0;
float current_lat = 0.000000;
float previous_lat = 0.0000000;
float difference = 0.0;
float lattitude1 = 0.0;
int counts;
int anArray[10];  //an array capable of holding 20 entries numbered 0 to 19
byte arrayIndex = 0;
BlynkTimer timer;

float spd;       //Variable  to store the speed
float sats;      //Variable to store no. of satellites response
String bearing;  //Variable to store orientation or direction of GPS

char auth[] = "V3qQJ3A4kR83kpYCBHjgjMsH-zL9J-Bb";              //Your Project authentication key
char ssid[] = "AVL_Engg";                                       // Name of your network (HotSpot or Router name)
char pass[] = "avl376377";                                      // Corresponding Password

//unsigned int move_index;         // moving index, to be used later
unsigned int move_index = 1;       // fixed location for now
  

void setup()
{
  Serial.begin(115200);
  Serial.println();
  ss.begin(GPSBaud);
  Blynk.begin(auth, ssid, pass);
  timer.setInterval(5000L, checkGPS); // every 5s check if GPS is connected, only really needs to be done once
}

void checkGPS(){
  if (gps.charsProcessed() < 10)
  {
    Serial.println(F("No GPS detected: check wiring."));
      Blynk.virtualWrite(V4, "GPS ERROR");  // Value Display widget  on V4 if GPS not detected
  }
}

void loop()
{
    while ((ss.available() > 0) && counts == 0) 
    {
      // sketch displays information every time a new sentence is correctly encoded.
    
      if (gps.encode(ss.read())){
        displayInfo();
       
      }
      
   
    }
     
        
        
        //displayInfo();
        
  Blynk.run();
  timer.run();
}


void displayInfo()
{ 
   if (gps.location.isValid() ) 
  {   
    float latitude = (gps.location.lat());     //Storing the Lat. and Lon. 
    
   
    
    anArray[arrayIndex] = latitude*1000000;
    float longitude = (gps.location.lng()); 
    

    if ((difference > 25) && f_flag == 1) {

      f_flag = 0 ;
      r_flag = 1;
      f_count = f_count +1 ;
    }
    if ((difference < -25) && r_flag == 1) {

      f_flag = 1 ;
      r_flag = 0;
      r_count = r_count +1 ;
    }
   
    if (arrayIndex == 6){
      difference = anArray[6] - anArray[1];
      arrayIndex = 0;
      memset(anArray, 0, sizeof(anArray));
     
    }
     arrayIndex++;
    Serial.print("Previous LAT:  ");
    Serial.println(anArray[1] ); // float to x decimal places
    Serial.print("current LAT:  ");
    Serial.println(anArray[5]); // float to x decimal places
    Serial.print("LONG: ");
    Serial.println(longitude, 6);
    Serial.print("DIfference in lattitude:");
     Serial.println(difference);
    Serial.print("forward_count:");
     Serial.println(f_count);
    Serial.print("reverse_count:");
     Serial.println(r_count);
    
    //Serial.println(gps.satellites.value());
    Blynk.virtualWrite(V1, String(latitude, 6));   
    //Blynk.virtualWrite(V2, String(longitude, 6)); 
    Blynk.virtualWrite(V2,(difference)); 
      
    myMap.location(move_index, latitude, longitude, "GPS_Location");
    spd = gps.speed.kmph();               //get speed
       //Blynk.virtualWrite(V3, spd);
       Blynk.virtualWrite(V3, f_count);
       
       sats = gps.satellites.value();    //get number of satellites
       //Blynk.virtualWrite(V4, sats);
       Blynk.virtualWrite(V4, r_count);
       bearing = TinyGPSPlus::cardinal(gps.course.value()); // get the direction
       Blynk.virtualWrite(V5, bearing);                   
  
  } 
 Serial.println();
}
