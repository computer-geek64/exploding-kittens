from flask import Flask, jsonify, redirect, request, render_template
from flask_socketio import SocketIO, emit, send, join_room, disconnect
import os
from Game import Game


app = Flask(__name__, template_folder=os.path.abspath(os.path.dirname(__file__)))
socketio = SocketIO(app)

users = {}


@app.route('/', methods=['GET'])
def index():
    return render_template('template.html')


@socketio.on('join', namespace='/games/exploding-kittens')
def join(data):
    users[data['username']] = data['id']
    send('You have joined the game, ' + data['username'] + '!')


@socketio.on('disconnect', namespace='/games/exploding-kittens')
def disconnected():
    print('Client disconnected')


@socketio.on('start', namespace='/games/exploding-kittens')
def start_game():
    game = Game(users.keys())
    for k in users.keys():
        emit('update', {'hand': list(map(lambda x: x.action, game.get_player_by_name(k).hand.cards))}, room=users[k])

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)