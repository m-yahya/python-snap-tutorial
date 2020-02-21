
import click
import paho.mqtt.client as mqtt


@click.command()
@click.option('--name', prompt='enter your name', help='enter user name')
@click.option('--age', prompt='enter your age', help='enter user age')
def init(name, age):

    client = mqtt.Client()

    print(client)
    print(name)
    print(age)
