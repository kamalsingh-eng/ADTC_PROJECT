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
WiFiClient espClient132523;
PubSubClient client(espClient132523);
long lastMsg = 0;
char msg101[2000];
//int value = 0;
int rst_cnt = 0;
int mqtt_conn_cnt = 0;
int buttonState = 0;
int ScriptNum = 0;
uint8_t wifi_pin = 32;
uint8_t mqtt_pin = 33;
uint8_t ser_dis = 34;
uint8_t ser_dis1 = 25;
uint8_t buttonPin = 2;
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
digitalWrite(ser_dis, HIGH);


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

    if (client.connect("ESP8266Client132523", mqttUser, mqttPassword )) {
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
  





  Serial.println("Hello!");
  
  Serial.println("Getting single-ended readings from AIN0..3");
  Serial.println("ADC Range: +/- 6.144V (1 bit = 3mV/ADS1015, 0.1875mV/ADS1115)");
  
  // The ADC input range (or gain) can be changed via the following
  // functions, but be careful never to exceed VDD +0.3V max, or to
  // exceed the upper and lower limits if you adjust the input range!
  // Setting these values incorrectly may destroy your ADC!
  //                                                                ADS1015  ADS1115
  //                                                                -------  -------
  // ads.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
   ads.setGain(GAIN_ONE);        // 1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
  // ads.setGain(GAIN_TWO);        // 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  // ads.setGain(GAIN_FOUR);       // 4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
  // ads.setGain(GAIN_EIGHT);      // 8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
  // ads.setGain(GAIN_SIXTEEN);    // 16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV
  
  ads.begin();
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



void loop(void) 
{

 int mqtt_result = 0;
 int16_t x;
 int16_t x1;
 int16_t x2;
 int16_t x3;
 
 int16_t adc0, adc1, adc2, adc3;
 float volts0,volts1,volts2,volts3;

 
  //Serial.print("AIN1: "); Serial.println(adc1);
  //Serial.print("AIN2: "); Serial.println(adc2);
  //Serial.print("AIN3: "); Serial.println(adc3);
  //Serial.println(" ");
  

   while (!client.connected())   {
 
      
    Serial.println("Connecting to MQTT...or wifi not connecting");
    client.connect("ESP8266Client132523",mqttUser, mqttPassword);
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

   long now = millis();
if (now - lastMsg > 400) {
lastMsg = now;
 adc0 = ads.readADC_SingleEnded(0);
 adc1 = ads.readADC_SingleEnded(1);
 adc2 = ads.readADC_SingleEnded(2);
 adc3 = ads.readADC_SingleEnded(3);
 volts0 = adc0*0.000125;
 volts1 = adc1*0.000125;
 volts2 = adc2*0.000125;
 volts3 = adc3*0.000125;
 Serial.print("AIN0: "); Serial.print(adc0);
 Serial.print("volts: "); Serial.println(volts0);
 Serial.print("AIN1: "); Serial.print(adc1);
 Serial.print("volts: "); Serial.println(volts1);
 Serial.print("AIN2: "); Serial.print(adc2);
 Serial.print("volts: "); Serial.println(volts2);
 Serial.print("AIN3: "); Serial.print(adc3);
 Serial.print("volts: "); Serial.println(volts3);
  
  x = adc0;
  x1 = adc1;
  x2 = adc2;
  x3 = adc3;
   
 StaticJsonDocument<200>JSONencoder;

  JSONencoder["ID"] = "VANAZ_PT";
  JSONencoder["NCH1"] = x;
  
 
  size_t n = serializeJsonPretty(JSONencoder, msg101);
  

  Serial.println("Sending message to MQTT topic..");
  Serial.println(msg101);
  client.publish("VANAZ_PT",msg101);


//    node.clearResponseBuffer();
    delay(100);
  }
  //  client.loop();  
    
  }
 
