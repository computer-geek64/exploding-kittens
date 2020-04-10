from flask import Flask, jsonify, redirect, request, render_template
from flask_socketio import SocketIO, emit, send, join_room, disconnect
import os
from Game import Game


app = Flask(__name__, template_folder=os.path.abspath(os.path.dirname(__file__)))
socketio = SocketIO(app)

users = {}
game = None


@app.route('/', methods=['GET'])
def index():
    return render_template('template.html')


@socketio.on('join', namespace='/games/exploding-kittens')
def join(username):
    users[username] = request.sid
    send('You have joined the game, ' + username + '!')


@socketio.on('disconnect', namespace='/games/exploding-kittens')
def disconnected():
    if request.sid in users.values():
        global game
        print('Client disconnected')
        user = [k for k, v in users.items() if v == request.sid][0]
        users.pop(user)
        game.remove_player(user)
        send_update()


@socketio.on('start', namespace='/games/exploding-kittens')
def start_game():
    global game
    game = Game(users.keys())
    send_update()


def send_update():
    global game
    for k in users.keys():
        emit('update', {'turn': game.turn % len(game.players), 'players': list(map(str, game.players)), 'hand': list(map(str, game.get_player_by_name(k).hand.cards))}, room=users[k])


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)