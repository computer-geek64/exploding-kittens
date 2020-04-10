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


@socketio.on('show_players', namespace='/games/exploding-kittens')
def show_players():
    emit('update_players', list(users.keys()))


@socketio.on('disconnect', namespace='/games/exploding-kittens')
def disconnected():
    if request.sid in users.values():
        global game
        print('Client disconnected')
        user = [k for k, v in users.items() if v == request.sid][0]
        users.pop(user)
    if not game == None:
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
        response = {
            'username': k,
            'turn': str(game.players[game.turn % len(game.players)]),
            'hand': [{'action': x.action, 'image': x.image, 'flipped': x.flipped, 'id': x.id} for x in game.get_player_by_name(k).hand.cards]
        }
        for player in game.players:
            if not str(player) == k:
                response['players'] = {}
                response['players'][str(player)] = {'hand': list(map(str, player.show_hand()))}
        emit('update', response, room=users[k])


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)