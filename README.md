# RabbitMQ Message Queue

This project demonstrates the implementation of a message queue using RabbitMQ with Python. It consists of a sender (`send.py`) that sends messages to a RabbitMQ queue and a receiver (`receive.py`) that consumes those messages.

## Overview

RabbitMQ is a powerful message broker that facilitates communication between different parts of a distributed system. In this implementation, the sender sends a unique message to the queue every second, while the receiver listens for incoming messages and prints them to the console.

## Prerequisites

To run this project, ensure you have the following installed on your machine:

1. **RabbitMQ Server**: Follow the installation instructions [here](https://www.rabbitmq.com/download.html).
2. **Erlang**: RabbitMQ requires Erlang to run. You can download it [here](https://www.erlang.org/downloads).
3. **Pika Library**: This library is used for connecting Python applications to RabbitMQ. You can install it using pip.

##Files
-send.py         # Sender script that sends messages to the RabbitMQ queue
-receive.py      # Receiver script that consumes messages from the RabbitMQ queue
