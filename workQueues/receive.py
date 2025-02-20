import pika
import time

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue='queue1')
def callback(ch, method, properties, body):
    print(f"[x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print("[x] Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='queue1', 
                      on_message_callback=callback, 
                      auto_ack=False)
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()