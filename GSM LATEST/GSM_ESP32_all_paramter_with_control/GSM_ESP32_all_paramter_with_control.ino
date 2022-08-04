/*
* MQTT and AskSensors IoT Platform
* Description: ESP32 publishes NEO-6M GPS position to AskSensors using MQTT
* Author: https://asksensors.com, 2020
* github: https://github.com/asksensors
*/

#include <WiFi.h>
#include <PubSubClient.h>
#include <SoftwareSerial.h>
#include <TinyGPS++.h>
#include <ArduinoJson.h>

//TODO: ESP32 MQTT user config
const char* ssid = "PTL-1"; // Wifi SSID
const char* password = "12345678"; // Wifi Password
const char* username = ""; // my AskSensors username
const char* pubTopic = "GSM_DATA"; // publish/username/apiKeyIn
const unsigned int writeInterval = 250; // write interval (in ms)

static const int RXPin = 16, TXPin = 17;
static const uint32_t GPSBaud = 9600;
//AskSensors MQTT config
const char* mqtt_server = "203.110.86.71";
unsigned int mqtt_port = 1883;




// objects
WiFiClient askClient;
PubSubClient client(askClient);
TinyGPSPlus gps; // The TinyGPS++ object
SoftwareSerial ss(RXPin, TXPin); // The serial connection to the GPS device


int f_flag = 1;
int r_flag = 1;
int f_count = 0;
int r_count = 0;
float current_lat = 0.000000;
float previous_lat = 0.0000000;
float difference = 0.0;
float lattitude1 = 0.0;
float Totalspeed = 0.0 ;
float Avgspeed = 0.0;
int speedcount = 0 ;
int counts;
int pub = 0;
int anArray[10];  //an array capable of holding 20 entries numbered 0 to 19
byte arrayIndex = 0;
const int ledpin =2 ;
//BlynkTimer timer;

float spd;       //Variable  to store the speed
float sats;      //Variable to store no. of satellites response
String bearing;  //Variable to store orientation or direction of GPS

//unsigned int move_index;         // moving index, to be used later
unsigned int move_index = 1;       // fixed location for now
int rst_cnt = 0;
int mqtt_conn_cnt = 0;

// setup
void setup() {
Serial.begin(115200);
Serial.println("*****************************************************");
Serial.println("********** Program Start : ESP32 publishes NEO-6M GPS position to AskSensors over MQTT");
Serial.print("********** connecting to WIFI : ");
Serial.println(ssid);
pinMode(ledpin, OUTPUT);

WiFi.begin(ssid, password);

while (WiFi.status() != WL_CONNECTED) {
delay(1000);
    rst_cnt = rst_cnt+1; 
        
        Serial.print("connecting..time(Sec)");
        Serial.println(rst_cnt);
         if (rst_cnt>15)
        {
          ESP.restart();
        }



}
Serial.println("");
Serial.println("->WiFi connected");
Serial.println("->IP address: ");
Serial.println(WiFi.localIP());

client.setServer(mqtt_server, mqtt_port);
client.setCallback(callback);
// GPS baud rate
ss.begin(GPSBaud);

}
// loop
void loop() {

if (!client.connected()) 
reconnect();
client.loop();
// This sketch displays information every time a new sentence is correctly encoded.
while (ss.available() > 0)
if (gps.encode(ss.read()))
displayInfo();

if (millis() > 5000 && gps.charsProcessed() < 10)
{
Serial.println(F("No GPS detected: check wiring."));
while(true);
}
}

// GPS displayInfo
void displayInfo() {

if (gps.location.isValid()) {
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
    //Blynk.virtualWrite(V1, String(latitude, 6));   
    //Blynk.virtualWrite(V2, String(longitude, 6)); 
    //Blynk.virtualWrite(V2,(difference)); 
    //Blynk.virtualWrite(V6, String(longitude, 6));  
      
    //myMap.location(move_index, latitude, longitude, "GPS_Location");
    spd = gps.speed.kmph();               //get speed
    Totalspeed  = Totalspeed + spd ;
    speedcount++;
    Avgspeed = Totalspeed/speedcount;
       //Blynk.virtualWrite(V3, spd);
       //Blynk.virtualWrite(V3, f_count);
       
       sats = gps.satellites.value();    //get number of satellites
       //Blynk.virtualWrite(V4, sats);
       //Blynk.virtualWrite(V4, r_count);
       bearing = TinyGPSPlus::cardinal(gps.course.value()); // get the direction
       //Blynk.virtualWrite(V5, Avgspeed);                   

    //delay(500);

   StaticJsonDocument<1200>JSONencoder;
   StaticJsonDocument<1200>JSONencoder1;

   
   //if (x2 > 0){

      //lastMsg = now;
    //Serial.println("Sending message to MQTT topic..");
    //Serial.println(JSONmessageBuffer);
    //client.publish("esp/test3", JSONmessaeBuffer,n);
    client.subscribe("esp32/output");

if (pub == 1 ){

    JSONencoder["ID"] = "GSM-DATA";
    JSONencoder["NCH1"] = String(latitude,6);
    JSONencoder["NCH2"] = String(longitude,6);
    JSONencoder["NCH3"] = f_count;
    JSONencoder["NCH4"] = r_count;
    JSONencoder["NCH5"] = Avgspeed;
    JSONencoder["NCH6"] = spd;
    JSONencoder["NCH7"] = difference;

    JSONencoder1["name"] = "GSM-DATA";
    JSONencoder1["icon"] = "fa-car";
    JSONencoder1["lat"] = String(latitude,6);
    JSONencoder1["lon"] = String(longitude,6);
   
    
 
    
    char JSONmessageBuffer[1200];
    char JSONmessageBuffer1[1200];
    

    size_t n = serializeJsonPretty(JSONencoder, JSONmessageBuffer);
    size_t n1 = serializeJsonPretty(JSONencoder1, JSONmessageBuffer1);
    client.publish("GSM_sensor", JSONmessageBuffer);
    Serial.println(JSONmessageBuffer);
    delay(100);
    client.publish("MAP_DATA", JSONmessageBuffer1);
    Serial.println(JSONmessageBuffer1);
}
 if (pub == 0 ){

    JSONencoder["ID"] = "GSM-DATA";
    JSONencoder["NCH1"] = 0;
    JSONencoder["NCH2"] = 0;
    JSONencoder["NCH3"] = 0;
    JSONencoder["NCH4"] = 0;
    JSONencoder["NCH5"] = 0;
    JSONencoder["NCH6"] = 0;
    JSONencoder["NCH7"] = 0;

   
   
    
 
    
    char JSONmessageBuffer[1200];

    

    size_t n = serializeJsonPretty(JSONencoder, JSONmessageBuffer);
   
    client.publish("GSM_sensor", JSONmessageBuffer);
    Serial.println(JSONmessageBuffer);
   

    }

delay(writeInterval);// delay 
//   
}
else {
Serial.println(F("INVALID"));
}


}
//MQTT callback
void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();

  // Feel free to add more if statements to control more GPIOs with MQTT

  // If a message is received on the topic esp32/output, you check if the message is either "on" or "off". 
  // Changes the output state according to the message
  if (String(topic) == "esp32/output") {
    Serial.print("Changing output to ");
    if(messageTemp == "on"){
      Serial.println("on");
     digitalWrite(ledpin, HIGH);
      pub =1 ;
    }
    else if(messageTemp == "off"){
      Serial.println("off");
     digitalWrite(ledpin, LOW);
      pub = 0 ;
    }
  }
}
//MQTT reconnect
void reconnect() {
// Loop until we're reconnected
while (!client.connected()) {
Serial.print("********** Attempting MQTT connection...");
// Attempt to connect
if (client.connect("ESP32Client", username, "")) { 
Serial.println("-> MQTT client connected");
} else {
Serial.print("failed, rc=");
Serial.print(client.state());
Serial.println("-> try again in 5 seconds");
// Wait 5 seconds before retrying
delay(5000);
}
}
}
