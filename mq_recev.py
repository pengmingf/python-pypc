import pika

def deal_msg(ch,method,type,body):
    # print("ch:")
    # print(ch)
    # print("method:")
    # print(method)
    # print("type:")
    # print(type)
    print("body:")
    print(body)


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.basic_consume(queue="pmf" , auto_ack = True , on_message_callback = deal_msg)
channel.start_consuming()

