import pika
import time

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue named 'test_queue'
channel.queue_declare(queue='test_queue')

# Counter for the messages
counter = 1

try:
    while True:
        message = f"My name is John Doe and I love Python! #{counter}"
        # Send message to the 'test_queue'
        channel.basic_publish(exchange='', routing_key='test_queue', body=message)
        print(f" [x] Sent: {message}")
        counter += 1
        # Sleep for 1 second before sending the next message
        time.sleep(1)

except KeyboardInterrupt:
    # Close connection when interrupted
    connection.close()
    print(" [x] Connection closed.")
