#include <WiFi.h>
#include <PubSubClient.h>
#include <ModbusMaster.h>
#include <SoftwareSerial.h>
#include <ArduinoJson.h>
#include <ESPmDNS.h>

//------------------------BLYNK-------------------------------

// Fill-in information from your Blynk Template here
                                   //                   #define BLYNK_TEMPLATE_ID "TMPLFCQplxL-"
                                                 //    #define BLYNK_DEVICE_NAME "ADTC"
//
                                   //               #define BLYNK_FIRMWARE_VERSION        "0.1.0"

                                      //        #define BLYNK_PRINT Serial
//#define BLYNK_DEBUG

//int randomNumber;
                                      //     #define APP_DEBUG

// Uncomment your board, or configure a custom board in Settings.h
//#define USE_WROVER_BOARD
//#define USE_TTGO_T7
//#define USE_ESP32C3_DEV_MODULE
//#define USE_ESP32S2_DEV_KIT

                                   //      #include "BlynkEdgent.h"


//------------------------BLYNK END _1-------------------------------



const char* ssid = "PTL-1";                 // wifi ssid
const char* password =  "12345678";         // wifi password

//const char* serverHostname = "raspberrypi";    // IP adress Raspberry Pi
const char* serverHostname = "203.110.86.71";    // IP adress Raspberry Pi
//const char* serverHostname = "192.168.0.108";    // IP adress Raspberry Pi
const int mqttPort = 1883;
const char* mqttUser = "";      // if you don't have MQTT Username, no need input
const char* mqttPassword = "";  // if you don't have MQTT Password, no need input

WiFiClient espClient21022;
PubSubClient client(espClient21022);
long lastMsg = 0;
int first_scan=0;

const int potPin1 = 34;
const int potPin2 = 35;
const int potPin3 = 32;


// variable for storing the potentiometer value


float pot1Value = 0;
float pot2Value = 0;
float pot3Value = 0;
float pot1Value1 = 0;
float pot2Value1 = 0;
float pot3Value1 = 0;
float a = 0;
float b = 0;
float c = 0;
float distance1 = 0;
float distance2 = 0;
float distance3 = 0;

int value = 0;
int rst_cnt = 0;
int mqtt_conn_cnt = 0;
uint8_t wifi_pin = 4;
uint8_t mqtt_pin = 2;







void setup() 
{


  Serial.begin(115200);
    //------------------------BLYNK_2-------------------------------
//void setup()
//{
// // Serial.begin(115200);
 // delay(100);
  
 // BlynkEdgent.begin();
//}
//------------------------BLYNK_2 END----------------------


  pinMode(wifi_pin, OUTPUT);
  pinMode(mqtt_pin, OUTPUT);

  digitalWrite(wifi_pin, LOW);
  digitalWrite(mqtt_pin, LOW);


  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) 
     {
         delay(1000);
          rst_cnt = rst_cnt+1; 
        digitalWrite(wifi_pin, LOW);
        Serial.print("connecting..time(Sec)");
        Serial.println(rst_cnt);
        if (rst_cnt>15)
        {
          ESP.restart();
        }
    
      }
  Serial.println("Connected to the WiFi network having IP");
  Serial.println(WiFi.localIP());
  Serial.print("WITH DEVICE WIFI MAC Address:  ");
  Serial.println(WiFi.macAddress());
  digitalWrite(wifi_pin, HIGH);
  if (!MDNS.begin("esp32")) {
      Serial.println("Error setting up MDNS responder!");
      while(1)

      {
          delay(1000);
      }

  }

  /* get the IP address of server by MDNS name */
  Serial.println("mDNS responder started");
 // IPAddress serverIp = MDNS.queryHost(serverHostname);
  Serial.print("IP address of server: ");
 // Serial.println(serverIp.toString()); 
client.setServer(serverHostname,mqttPort);
 
     
 // client.setServer(serverIp, mqttPort);
  client.setCallback(callback);
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");

    if (client.connect("ESP8266Client202210", mqttUser, mqttPassword )) {

      Serial.println("connected");


    } else {

      mqtt_conn_cnt = mqtt_conn_cnt + 1;
      Serial.print("failed with state ");
      Serial.println(client.state());
      Serial.print("failed_count..");
      Serial.println(mqtt_conn_cnt);
      delay(50);
       digitalWrite(mqtt_pin, LOW);
      if (mqtt_conn_cnt > 2)
      {
        ESP.restart();
      }

    }
  }
}
void callback(char* topic, byte* payload, unsigned int length) {

  Serial.print("Message arrived in topic: ");
  Serial.println(topic);

  Serial.println("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }

  Serial.println();
  Serial.println("-----------------------");
  // wait for a second
}

void loop() {
  int mqtt_result = 0;
  //int potValue = 0; 
  int Value_PUMA_Monitor_Bit = 0;
  int Value_PUMA_Manual_Bit = 0;
  int Value_PUMA_Idle_Bit = 0;
  client.subscribe("ATDC_CONTROL");
  
  while (!client.connected())   {


    Serial.println("Connecting to MQTT...or wifi not connecting");
     digitalWrite(mqtt_pin, LOW);
    client.connect("ESP8266Client202210", mqttUser, mqttPassword);
    mqtt_result = mqtt_result + 1;

    delay(1000);
    Serial.println(mqtt_result);
    if (mqtt_result > 16)
    {
      ESP.restart();

    }
  }

   if (client.connected()) {
   digitalWrite(mqtt_pin, HIGH);
   }
   long now = millis();
   if(first_scan=0)
   {
     long now = millis();
     lastMsg = now;
     first_scan=1;
     Serial.print("first scan done  ");
     Serial.print(first_scan);
   }
  //if (now - lastMsg > 1000) {
  //  lastMsg = now;
{   delay(500);


    //----------------------Analog Channel-------------------------

 


  pot1Value = analogRead(potPin1);
  pot2Value = analogRead(potPin2);
  pot3Value = analogRead(potPin3);
  pot1Value1 = pot1Value-666;
  distance1 = pot1Value1/675;
  pot2Value1 = pot2Value-666;
  distance2 = pot2Value1/675;
  pot3Value1 = pot3Value-666;
  distance3 = pot3Value1/675;
 
  //distance3 = movingAverage(analogRead(potPin));
//------------------------BLYNK_3-------------------------------

  //Blynk.virtualWrite(V0, distance1); //sending to Blynk
 // Blynk.virtualWrite(V1, distance2); //sending to Blynk
  //Blynk.virtualWrite(V2, distance3); //sending to Blynk
  //BlynkEdgent.run();

//------------------------BLYNK_3 END-------------------------------

  
  //Serial.println(pot1Value);
  ////Serial.println(pot1Value1);
  //Serial.println(pot2Value);
  //Serial.println(pot2Value1);
  //Serial.println(distance1);
  //Serial.println(distance2);
  //Serial.println(pot3Value);
  //Serial.println(pot3Value1);
  //Serial.println(distance3);


//------------------------BLYNK_4 -------------------------------/*

  //BlynkEdgent.run();
//------------------------BLYNK_4 END-------------------------------/*



  delay(500);

    StaticJsonDocument<1200>JSONencoder;

    JSONencoder["ID"] = "distance-senseor";
    JSONencoder["PCH1"] = pot1Value;
    JSONencoder["PCH2"] = pot2Value;
    JSONencoder["PCH3"] = distance1;
    JSONencoder["PCH4"] = distance2;
    JSONencoder["PCH5"] = pot3Value;
    JSONencoder["PCH6"] = distance3;
 
    
    char JSONmessageBuffer[1200];
    

    size_t n = serializeJsonPretty(JSONencoder, JSONmessageBuffer);

   //if (x2 > 0){
   if (now - lastMsg > 20000) {
      //lastMsg = now;
    //Serial.println("Sending message to MQTT topic..");
    //Serial.println(JSONmessageBuffer);
    //client.publish("esp/test3", JSONmessageBuffer,n);
    
   client.publish("distance_sick_seensor", JSONmessageBuffer);
   }
    client.loop();

}
  }
