import pika

class Rabbit(object):

    def __init__(self, new_data):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.56.101'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='sender')

        self.the_data = new_data

        self.channel.basic_publish(exchange='api', type='topic', routing_key='sender', body='%s' % self.the_data)
        self.connection.close()
