//Viral Science www.viralsciencecreativity.com www.youtube.com/c/viralscience
//Realtime GPS Tracker with Nodemcu ESP8266
#include <PubSubClient.h>
#include <ModbusMaster.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include <ArduinoJson.h>

const char* ssid = "PTL-1";                 // wifi ssid
const char* password =  "12345678";         // wifi password

//const char* serverHostname = "raspberrypi";    // IP adress Raspberry Pi
const char* serverHostname = "203.110.86.71";    // IP adress Raspberry Pi
//const char* serverHostname = "192.168.0.108";    // IP adress Raspberry Pi
const int mqttPort = 1883;
const char* mqttUser = "";      // if you don't have MQTT Username, no need input
const char* mqttPassword = "";  // if you don't have MQTT Password, no need input

WiFiClient espClient2102223;
PubSubClient client(espClient2102223);
long lastMsg = 0;
int first_scan=0;

static const int RXPin = 4, TXPin = 5;   // GPIO 4=D2(conneect Tx of GPS) and GPIO 5=D1(Connect Rx of GPS
static const uint32_t GPSBaud = 9600; //if Baud rate 9600 didn't work in your case then use 4800

TinyGPSPlus gps; // The TinyGPS++ object

SoftwareSerial ss(RXPin, TXPin);  // The serial connection to the GPS device

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
//BlynkTimer timer;

float spd;       //Variable  to store the speed
float sats;      //Variable to store no. of satellites response
String bearing;  //Variable to store orientation or direction of GPS

//char auth[] = "V3qQJ3A4kR83kpYCBHjgjMsH-zL9J-Bb";              //Your Project authentication key
//char ssid[] = "AVL_Engg";                                       // Name of your network (HotSpot or Router name)
//char pass[] = "avl376377";                                      // Corresponding Password

//unsigned int move_index;         // moving index, to be used later
unsigned int move_index = 1;       // fixed location for now
int rst_cnt = 0;
int mqtt_conn_cnt = 0;
  

void setup()
{
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) 
     {
         delay(1000);
          rst_cnt = rst_cnt+1; 
        
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
  Serial.println();

  client.setServer(serverHostname,mqttPort);
 
     
 // client.setServer(serverIp, mqttPort);
  client.setCallback(callback);
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");

    if (client.connect("ESP8266Client202223", mqttUser, mqttPassword )) {

      Serial.println("connected");


    } else {

      mqtt_conn_cnt = mqtt_conn_cnt + 1;
      Serial.print("failed with state ");
      Serial.println(client.state());
      Serial.print("failed_count..");
      Serial.println(mqtt_conn_cnt);
      delay(50);
      
      if (mqtt_conn_cnt > 2)
      {
        ESP.restart();
      }

    }
  }
  ss.begin(GPSBaud);
  //Blynk.begin(auth, ssid, pass);
  //timer.setInterval(5000L, checkGPS); // every 5s check if GPS is connected, only really needs to be done once
}

void checkGPS(){
  if (gps.charsProcessed() < 10)
  {
    Serial.println(F("No GPS detected: check wiring."));
      Blynk.virtualWrite(V4, "GPS ERROR");  // Value Display widget  on V4 if GPS not detected
  }
}


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
     digitalWrite(LED_BUILTIN, HIGH);
      pub =1 ;
    }
    else if(messageTemp == "off"){
      Serial.println("off");
     digitalWrite(LED_BUILTIN, LOW);
      pub = 0 ;
    }
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
        
  //Blynk.run();
  //timer.run();
}


void displayInfo()
{
  int mqtt_result = 0;
  while (!client.connected())   {


    Serial.println("Connecting to MQTT...or wifi not connecting");
     //digitalWrite(mqtt_pin, LOW);
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
   //digitalWrite(mqtt_pin, HIGH);
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

    delay(500);

   StaticJsonDocument<1200>JSONencoder;
   StaticJsonDocument<1200>JSONencoder1;

   
   //if (x2 > 0){
   if (now - lastMsg >1000) {
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
    delay(100);
    client.publish("MAP_DATA", JSONmessageBuffer1);

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
   

    }
  
  }
 Serial.println();
}
}
