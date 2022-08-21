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


const char* ssid = "Daksh1"; // Wifi SSID
const char* password = "avl376377"; // Wifi Password
const char* username = ""; // my AskSensors username
const char* pubTopic = "GSM_DATA"; // publish/username/apiKeyIn
const unsigned int writeInterval = 250; // write interval (in ms)


const char* mqtt_server = "203.110.86.71";
unsigned int mqtt_port = 1883;

int rst_cnt = 0 ;
long lastMsg = 0;


// objects
WiFiClient askClient;
PubSubClient client(askClient);




// setup






void callback(char* topic, byte* message, unsigned int length) {
StaticJsonDocument<256> doc;
deserializeJson(doc, message, length);
int a1 = doc["a1"];
Serial.println("kamal singh ne subscribe kiya");
Serial.println(a1);

  
}



void setup() {
Serial.begin(115200);
Serial.println("*****************************************************");
Serial.println("********** Program Start : ESP32 publishes NEO-6M GPS position to AskSensors over MQTT");
Serial.print("********** connecting to WIFI : ");
Serial.println(ssid);


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


}






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



void loop() {
int a;
int b ;
int c;
int d;
int e;

a = random(10,20);
b = random(10,20);
c = random(10,20);
d = random(10,20);
e = random(10,20);

if (!client.connected()) 
reconnect();
client.loop();


long now = millis();
if (now - lastMsg > 450) {
lastMsg = now;
StaticJsonDocument<1200>JSONencoder;
client.subscribe("GSM_sensor2");

 JSONencoder["ID"] = "GSM-DATA";
 JSONencoder["NCH1"] = a;
 JSONencoder["NCH2"] = b;
 JSONencoder["NCH3"] = c;
 JSONencoder["NCH4"] = d;
 JSONencoder["NCH5"] = e;

char JSONmessageBuffer[1200];
 
size_t n = serializeJsonPretty(JSONencoder, JSONmessageBuffer);

client.publish("GSM_sensor1", JSONmessageBuffer);
Serial.println(JSONmessageBuffer);

}
}
// GPS displayInfo



  
   

   
   
    

 
