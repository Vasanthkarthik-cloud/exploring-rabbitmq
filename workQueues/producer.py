import sys
import pika
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue='queue1')
message=' '.join(sys.argv[1:]) or "This is rabbitmq"
channel.basic_publish(exchange='', 
                      routing_key='queue1', 
                      body=message)
print(f"[x] Sent {message}")
connection.close()
