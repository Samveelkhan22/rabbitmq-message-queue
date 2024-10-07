import pika

# Define a callback function to process the received message
def callback(ch, method, properties, body):
    print(f" [x] Received: {body.decode()}")

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same queue 'test_queue'
channel.queue_declare(queue='test_queue')

# Tell RabbitMQ to send messages to callback function
channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
