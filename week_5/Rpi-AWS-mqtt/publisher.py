import paho.mqtt.publish as publish

publish.single("ifn649", "Hello World", hostname="13.236.187.192")
print("Done")