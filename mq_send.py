import pika

#要发送的消息
message = input("请输入你想说的话：")

#连接主机
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#连接进队列
channel.queue_declare(queue="pmf")
#向该队列发送消息
channel.basic_publish(exchange = "",routing_key='pmf',body=message)

print("send over")