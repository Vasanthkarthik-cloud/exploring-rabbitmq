🐇 RabbitMQ Exploration

This repository contains a simple producer-consumer implementation using RabbitMQ and the pika Python library. The producer sends messages to a queue, and the consumer processes them.
📌 Prerequisites

Before running the scripts, ensure you have the following installed:

    RabbitMQ (Running on localhost)
    Python 3
    pika library (pip install pika)

🚀 Getting Started
1️⃣ Start RabbitMQ

Ensure RabbitMQ is running. If you’re using Docker, you can start RabbitMQ with:

docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

Then, access the RabbitMQ UI at http://localhost:15672/ (Login: guest / guest).
2️⃣ Install Dependencies

pip install pika

3️⃣ Run the Consumer

The consumer listens for messages in the hello queue. Open a terminal and run:

python consumer.py

It will wait for incoming messages.
4️⃣ Send Messages with the Producer

Open another terminal and send messages:

python producer.py "Hello, RabbitMQ!"
python producer.py "Message with dots...."

The consumer will receive and process them. The more dots (.) in the message, the longer the processing time.
📂 File Structure

├── producer.py  # Sends messages to RabbitMQ queue
├── consumer.py  # Receives and processes messages
├── README.md    # Project documentation

🛑 Stopping the Consumer

To stop the consumer, press CTRL+C in the terminal.
🎯 Next Steps

    Experiment with multiple consumers.
    Try different RabbitMQ exchange types.
    Use persistent messaging to ensure messages survive restarts.