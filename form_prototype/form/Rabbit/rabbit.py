import pika

class RabbitMq(object):

    def __init__(self, new_data):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='rabbit')

        self.the_data = new_data

        self.channel.basic_publish(exchange='', routing_key='rabbit', body='%s' % self.the_data)
        self.connection.close()
