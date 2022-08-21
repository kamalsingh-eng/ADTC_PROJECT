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
const char* ssid = "Daksh"; // Wifi SSID
const char* password = "avl376377"; // Wifi Password
const char* username = ""; // my AskSensors username


static const int RXPin = 16, TXPin = 17;
static const uint32_t GPSBaud = 9600;
//AskSensors MQTT config


const char* mqtt_server = "192.168.0.147"; //192.168.0.241
const char* mqtt_server1 = "203.110.86.71";



unsigned int mqtt_port = 1883;

unsigned int mqtt_port1 = 1883;


float spd=0;
float spd1=0; 
float longitude=0;
float latitude=0;


float VALUE=0;
float FR=0;
float FL=0;
float BR1=0;
float BL=0;



int f_count1 = 0;
int r_count1 = 0;

int FD=0;

float Avgspeed1 = 0.0;

int stop_count1 = 0;












// objects
WiFiClient askClient;
WiFiClient askClient1; 

PubSubClient client(askClient);
PubSubClient client1(askClient1);



int f_flag = 1;
int r_flag = 1;
int f_count = 0;
int r_count = 0;
float current_lat = 0.000000;
float previous_lat = 0.0000000;
float current_lon = 0.000000;
float previous_lon = 0.0000000;
float difference = 0.0;
float difference1 = 0.0;
float lattitude1 = 0.0;
float longitude1 = 0.0;
float Totalspeed = 0.0 ;
float Avgspeed = 0.0;
int speedcount = 0 ;
int counts;
int pub = 0;
int pub1 = 0;

int anArray[10];  //an array capable of holding 20 entries numbered 0 to 19
int anArray1[10]; 
byte arrayIndex = 0;
const int ledpin =2 ;
int stop_count_flag = 0;
int stop_flag = 0;
int stop_count = 0;
//BlynkTimer timer;



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

client1.setServer(mqtt_server1, mqtt_port1);

client.setCallback(callback);

client1.setCallback(callback1);


// GPS baud rate




}




// loop
void loop() {

if (!client.connected()) 
{
 reconnect();
}
if (!client1.connected()) {

reconnect1();
}





spd=random(0,20);
Serial.println(spd);

  
displayInfo();
/*
if (millis() > 5000 && gps.charsProcessed() < 10)
{
Serial.println(F("No GPS detected: check wiring."));
while(true);
}

*/
}


// GPS displayInfo
void displayInfo() {
int i=10;
if (i>5)
{

   StaticJsonDocument<1200>JSONencoder;
   //StaticJsonDocument<1200>JSONencoder1;

   


  latitude= (random(28,30));
  longitude= (random(77,80));

  

  spd=random(0,20);
  Avgspeed1 = random(1,20);
  

  f_count1= random(1,10);
  delay(1000);
  r_count1= random(1,10);
  delay(500);
  stop_count1= random(1,10);

  
  if (spd>Avgspeed1)
  {
    Avgspeed=Avgspeed1;
  }

   if (f_count1>r_count1)
  {
    r_count = r_count1;
  }

     if (stop_count1<f_count1)
  {
    stop_count = stop_count1;
  }




  VALUE=random(0,20);
  FR = random(1,20);
  FL = random(1,20);
  BR1 = random(1,20);
  BL = random(1,20);
  spd=random(0,20);






    
    client1.subscribe("ADTC/GSM11");  //esp32/output

if ((pub == 0) || (pub1==0)){

    JSONencoder["ID"] = "ADTC/GSM2";
    JSONencoder["N1"] = latitude;
    JSONencoder["N2"] = longitude;
    JSONencoder["N3"] = f_count1;
    JSONencoder["N4"] = r_count;
    JSONencoder["N5"] = Avgspeed1;
    JSONencoder["N6"] = spd;
    JSONencoder["N7"] = difference;
    JSONencoder["N8"] = stop_count;
    JSONencoder["N9"] = stop_count_flag;
    JSONencoder["N10"] = stop_flag;
    JSONencoder["N11"]= difference1;

   // JSONencoder1["ID"] = "ADTC/GSM12";
  //  JSONencoder1["N1"] = 1;
 
    
 
    
    char JSONmessageBuffer[1200];
   // char JSONmessageBuffer1[1200];
    

    size_t n = serializeJsonPretty(JSONencoder, JSONmessageBuffer);
    
  //  size_t n1 = serializeJsonPretty(JSONencoder1, JSONmessageBuffer1);
    client.publish("ADTC/GSM2", JSONmessageBuffer);
    Serial.println(JSONmessageBuffer);
    delay(100);
   // client1.publish("ADTC/GSM12", JSONmessageBuffer1);
    //Serial.println(JSONmessageBuffer1);
   
}
 if (pub == 1 ){

    f_count = 0;
    r_count = 0;
    Avgspeed = 0;
   // spd = 0 ;
    difference = 0;
    stop_count = 0;
    stop_count_flag = 0;
    stop_flag = 0;



    JSONencoder["ID"] = "ADTC/GSM2";
    JSONencoder["N1"] = 0;
    JSONencoder["N2"] = 0;
    JSONencoder["N3"] = 0;
    JSONencoder["N4"] = 0;
    JSONencoder["N5"] = 0;
    JSONencoder["N6"] = 0;
    JSONencoder["N7"] = 0;
    JSONencoder["N8"] = 0;
    JSONencoder["N9"] = 0;
    JSONencoder["N10"]= 0;
   
   
    
 
    
    char JSONmessageBuffer[1200];

    

    size_t n = serializeJsonPretty(JSONencoder, JSONmessageBuffer);
   
    client.publish("ADTC/GSM2", JSONmessageBuffer);
    Serial.println(JSONmessageBuffer);
  

    }





  



    StaticJsonDocument<1200>JSONencoder2;
if (pub == 0 ){

    JSONencoder2["ID"] = "ADTC/LS2";
    JSONencoder2["N1"] = VALUE;
    JSONencoder2["N2"] = FR;
    JSONencoder2["N3"] = FL;
    JSONencoder2["N4"] = BR1;
    JSONencoder2["N5"] = BL;
    JSONencoder2["N6"] = spd;
    JSONencoder2["N7"] = 0;
    JSONencoder2["N8"] = 0;
    JSONencoder2["N9"] = 0;
    JSONencoder2["N10"] = 0;
    JSONencoder2["N11"]= 0;


   
    
 
    
    char JSONmessageBuffer2[1200];
    

    size_t n2 = serializeJsonPretty(JSONencoder2, JSONmessageBuffer2);
    client.publish("ADTC/LS2", JSONmessageBuffer2);
    //client.publish("RCV",JSONmessageBuffer1);

    
    Serial.println(JSONmessageBuffer2);
    delay(100);



}


if (pub == 1 )

{

 


    JSONencoder2["ID"] = "ADTC/LS2";
    JSONencoder2["N1"] = 0;
    JSONencoder2["N2"] = 0;
    JSONencoder2["N3"] = 0;
    JSONencoder2["N4"] = 0;
    JSONencoder2["N5"] = 0;
    JSONencoder2["N6"] = 0;
    JSONencoder2["N7"] = 0;
    JSONencoder2["N8"] = 0;
    JSONencoder2["N9"] = 0;
    JSONencoder2["N10"]= 0;
   
   
    
 
    
    char JSONmessageBuffer2[1200];

    

    size_t n2 = serializeJsonPretty(JSONencoder2, JSONmessageBuffer2);
   
    client.publish("ADTC/LS2", JSONmessageBuffer2);
    Serial.println(JSONmessageBuffer2);

    
  

    }

int BACK=0;
  BACK = random(0,2);

int parking =0;

parking=random(0,12);

int ZB=0;
ZB = random(0,2);


  



    StaticJsonDocument<1200>JSONencoder3;
if (pub == 0 ){

    JSONencoder3["ID"] = "ADTC/GS2";
    JSONencoder3["N1"] = ZB;
    JSONencoder3["N2"] = parking;
    JSONencoder3["N3"] = BACK;


    char JSONmessageBuffer3[1200];
    

    size_t n3 = serializeJsonPretty(JSONencoder3, JSONmessageBuffer3);
    client.publish("ADTC/GS2", JSONmessageBuffer3);
    //client.publish("RCV",JSONmessageBuffer3);

    
    Serial.println(JSONmessageBuffer3);
    delay(100);

}


if (pub == 1 )
{



    JSONencoder3["ID"] = "ADTC/GS2";
    JSONencoder3["N1"] = 0;
    JSONencoder3["N2"] = 0;
    JSONencoder3["N3"] = 0;


   
    
    char JSONmessageBuffer3[1200];

    

    size_t n3 = serializeJsonPretty(JSONencoder3, JSONmessageBuffer3);
   
    client.publish("ADTC/GS2", JSONmessageBuffer3);
    Serial.println(JSONmessageBuffer3);

   

    
   

    }





  




    


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
      pub =0 ;
    }
    else if(messageTemp == "off"){
      Serial.println("off");
     digitalWrite(ledpin, LOW);
      pub = 1 ;
    }
  }
}

//MQTT callback1
void callback1(char* topic1, byte* message1, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic1);
  Serial.print(". Message: ");
  String messageTemp1;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message1[i]);
    messageTemp1 += (char)message1[i];
  }
  Serial.println();

  // Feel free to add more if statements to control more GPIOs with MQTT

  // If a message is received on the topic esp32/output, you check if the message is either "on" or "off". 
  // Changes the output state according to the message
  if (String(topic1) == "ADTC/GSM11") {
    Serial.print("Changing output to ");
    if(messageTemp1 == "on"){
      Serial.println("on from the remote server request");
     digitalWrite(ledpin, HIGH);
      pub1 =0 ;

   StaticJsonDocument<1200>JSONencoder1;
   char JSONmessageBuffer1[1200];
   size_t n1 = serializeJsonPretty(JSONencoder1, JSONmessageBuffer1);
   JSONencoder1["ID"] = "ADTC/GSM12";
   JSONencoder1["N"] = 1;
   
 client1.publish("ADTC/GSM12", JSONmessageBuffer1);
 Serial.println(JSONmessageBuffer1);



      
    }
    else if(messageTemp1 == "off"){
      Serial.println("off");
     digitalWrite(ledpin, LOW);
      pub1 = 1 ;
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




//MQTT reconnect
void reconnect1() {
// Loop until we're reconnected
while (!client1.connected()) {
Serial.print("********** Attempting MQTT connection...");
// Attempt to connect
if (client1.connect("ESP32Client", username, "")) { 
Serial.println("-> MQTT client connected");
} else {
Serial.print("failed, rc=");
Serial.print(client1.state());
Serial.println("-> try again in 5 seconds");


// Wait 5 seconds before retrying
delay(5000);
}
}
}
