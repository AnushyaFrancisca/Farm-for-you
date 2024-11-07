#include <ESP8266WiFi.h>
#include <DHT.h>

#define DHTPIN 2  // GPIO pin where the DHT11 data pin is connected
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "Room no11";  // Wi-Fi SSID
const char* password = "11111111";  // Wi-Fi password
const char* server = "http://your-django-server.com/Farmer/api/save_sensor_data/";

WiFiClient client;

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to Wi-Fi...");
  }
  Serial.println("Connected to Wi-Fi");
}

void loop() {
  // Read temperature and humidity
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Send data to Django server
  if (client.connect(server, 80)) {
    String postData = "temperature=" + String(temperature) + "&humidity=" + String(humidity);

    client.println("POST /api/save_sensor_data/ HTTP/1.1");
    client.println("Host: your-django-server.com");
    client.println("Content-Type: application/x-www-form-urlencoded");
    client.print("Content-Length: ");
    client.println(postData.length());
    client.println();
    client.println(postData);
    client.stop();

    Serial.println("Data sent: " + postData);
  } else {
    Serial.println("Failed to connect to server");
  }

  delay(60000);  // Wait 60 seconds before sending data again
}
