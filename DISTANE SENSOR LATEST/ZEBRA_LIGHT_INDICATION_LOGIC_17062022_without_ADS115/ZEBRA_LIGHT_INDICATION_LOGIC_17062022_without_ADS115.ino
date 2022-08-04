#include <Wire.h>
#include <FS.h>
#include <WiFi.h>
#include <PubSubClient.h>

#include <ESPmDNS.h>
#include <ArduinoJson.h>
#include <Adafruit_ADS1015.h>

 Adafruit_ADS1115 ads;  /* Use this for the 16-bit version */
//Adafruit_ADS1015 ads;     /* Use thi for the 12-bit version */


const char* ssid = "Daksh";                 // wifi ssid
const char* password =  "avl376377";         // wifi password
const char* serverHostname = "203.110.86.71";    // IP adress Raspberry Pi
const int mqttPort = 1883;
const char* mqttUser = "";      // if you don't have MQTT Username, no need input
const char* mqttPassword = "";  // if you don't have MQTT Password, no need input
WiFiClient espClient11132523;
PubSubClient client(espClient11132523);
long lastMsg = 0;
char msg101[2000];
//int value = 0;
int rst_cnt = 0;
int mqtt_conn_cnt = 0;
int buttonState = 0;
int ScriptNum = 0;

const int potPin1 = 34;
const int potPin2 = 35;
const int potPin3 = 32;
const int Seatbelt = 22 ;


// variable for storing the potentiometer value


float pot1Value = 0;
float pot2Value = 0;
float pot3Value = 0;
float pot1Value1 = 0;
float pot2Value1 = 0;
float pot3Value1 = 0;
int Seatbelt_status = 0 ;
float a = 0;
float b = 0;
float c = 0;
float distance1 = 0;
float distance2 = 0;
float distance3 = 0;
uint8_t wifi_pin = 23;
uint8_t mqtt_pin = 24;
uint8_t ser_dis = 2;
uint8_t ser_dis1 = 25;
uint8_t buttonPin = 14;
uint32_t big_number;
uint16_t low_order_byte = 15;
uint16_t high_order_byte =1;

//IPAddress local_IP(192, 168, 0, 101);
//IPAddress gateway(192, 168, 0, 1);
//IPAddress subnet(255, 255, 0, 0);
//IPAddress primaryDNS(8, 8, 8, 8); // optional
//IPAddress secondaryDNS(8, 8, 4, 4); // optional



//uint8_t LED1pin = D3;
//uint8_t LED1status;
//uint8_t LED2status;
//uint8_t LED3status;
//uint8_t LEDon;
//uint8_t LED1on;
//uint8_t LED2on;

//uint8_t LED2pin = D4;
//byte value;
//byte value1;
//byte value2;

//bool LED2status = LOW;
 //void preTransmission()
//{
  //digitalWrite(MAX485_RE_NEG, 1);
  //digitalWrite(MAX485_DE, 1);
//}

//void postTransmission()
//{
//  digitalWrite(MAX485_RE_NEG, 0);
  //digitalWrite(MAX485_DE, 0);
//}

void setup() {

//pinMode(LED_BUILTIN, OUTPUT);   
//pinMode(MAX485_RE_NEG, OUTPUT);
//pinMode(MAX485_DE, OUTPUT);
pinMode(wifi_pin, OUTPUT);
pinMode(mqtt_pin, OUTPUT);
pinMode(ser_dis, OUTPUT);
pinMode(ser_dis1, OUTPUT);
pinMode(buttonPin, INPUT);
  // Init in receive mode
//digitalWrite(MAX485_RE_NEG, 1);
  //digitalWrite(MAX485_DE, 1);
digitalWrite(wifi_pin, LOW);
digitalWrite(mqtt_pin, LOW);
digitalWrite(ser_dis, LOW);


  //My slave uses 19200 baud
Serial.begin(115200);



//   if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS)) {
//  Serial.println("STA Failed to configure");
// }

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
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
// if (!MDNS.begin("esp32")) {
//      Serial.println("Error setting up MDNS responder!");
//      while(1) {
//          delay(1000);
 //     }
//  }
  /* get the IP address of server by MDNS name */
 // Serial.println("mDNS responder started");
 // IPAddress serverIp = MDNS.queryHost(serverHostname);
 // Serial.print("IP address of server: ");
 // Serial.println(serverIp.toString()); 
   

  
  client.setServer(serverHostname, mqttPort);
  client.setCallback(callback);
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");

    if (client.connect("ESP8266Client11132523", mqttUser, mqttPassword )) {
     digitalWrite(mqtt_pin, HIGH);
      Serial.println("connected");
    //    RS485.begin(9600);
  

      


      
       
    } else {

          mqtt_conn_cnt = mqtt_conn_cnt+1;
      Serial.print("failed with state ");
      Serial.println(client.state());
      Serial.print("failed_count..");
      Serial.println(mqtt_conn_cnt);
      delay(50);
      digitalWrite(mqtt_pin, LOW);
      if (mqtt_conn_cnt>2)
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
 // digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(500);                       // wait for a second
  //digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(500);                       // wait for a second
  }

void red_light_on(void){

digitalWrite(ser_dis,HIGH);   // turn the LED on (HIGH is the voltage level)
  pot1Value = analogRead(potPin1);
  pot2Value = analogRead(potPin2);
  pot3Value = analogRead(potPin3);
  Seatbelt_status = digitalRead(Seatbelt);
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
  Serial.println(pot3Value1);
  Serial.println(distance3);


//------------------------BLYNK_4 -------------------------------/*

  //BlynkEdgent.run();
//------------------------BLYNK_4 END-------------------------------/*

 StaticJsonDocument<200>JSONencoder;

  JSONencoder["ID"] = "INDICATION_DATA";
  JSONencoder["NCH1"] = "ZEBRA_CROSS_LINE_DETECTED";
  
 
  size_t n = serializeJsonPretty(JSONencoder, msg101);
  

  Serial.println("Sending message to MQTT topic..");
  //Serial.println(msg101);
 

 if (distance3 < 2.0 ){
   client.publish("INDICATION_DATA",msg101);
   Serial.println("msg sent");
  }
delay(500);
}

void red_light_off(void){

digitalWrite(ser_dis, LOW);   // turn the LED on (HIGH is the voltage level)

}

void loop(void) 
{
  
 long now = millis();
 int mqtt_result = 0;
  

   while (!client.connected())   {
 
      
    Serial.println("Connecting to MQTT...or wifi not connecting");
    client.connect("ESP8266Client11132523",mqttUser, mqttPassword);
    mqtt_result=mqtt_result+1;
    digitalWrite(mqtt_pin, LOW);
    delay(1000);
    Serial.println(mqtt_result);
    if (mqtt_result>3)
    {
    ESP.restart();
   
      } 
   }
   if (client.connected()) {
    digitalWrite(mqtt_pin, HIGH);
   }

 
  
if (now - lastMsg <30000) {
  red_light_on();
}

if ((now - lastMsg >30000) &&(now - lastMsg <40000)) {
  red_light_off();
}

if (now - lastMsg >40000) {
  lastMsg = now;
}



//    node.clearResponseBuffer();
  
  //  client.loop();  
    
  }
 
