# cloud-project
Image Recognition for IoT in the Cloud. Built a simple PoC to simulate a "smart" camera IOT device which streams images to the cloud where they are analysed.


Today cloud services have gone far beyond providing compute and storage facilities, and have
expanded into a wide variety of services from machine learning, automated load balancing,
decentralized peer to peer architectures and internet of things. At the same time, the number of
companies providing cloud services has exploded in the last few years. This document presents
an application built using cloud only components from multiple providers to build a real world
application.

The application developed was a prototype of a automatic vehicle image recognition system
capable of recognizing images of vehicles from a stream of photos sent to it by an intelligent
network connected set of cameras.

Project was implemented using google cloud simulators for IoT devices which stream images(simulated here) to the server using MQTT
and a pub sub engine. IoT server then sends the images to a amazon rekognition(amazons image recognition engine) which then 
analyses these images and sends back the results back to the google IoT server, which can take actions accordingly.

Project report:
https://drive.google.com/file/d/17pW4H6rLS9QpNxlWRpXziLvkCDlVtlit/view?usp=sharing
