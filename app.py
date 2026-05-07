from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Game state
game_state = {
    'board': ['', '', '', '', '', '', '', '', ''],
    'current_player': 'X',
    'game_over': False,
    'winner': None
}

def check_winner(board):
    """Check if there's a winner"""
    # Winning combinations
    winning_combos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    
    return None

def is_board_full(board):
    """Check if board is full"""
    return all(cell != '' for cell in board)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/game-state', methods=['GET'])
def get_game_state():
    """Get current game state"""
    return jsonify(game_state)

@app.route('/api/move', methods=['POST'])
def make_move():
    """Make a move in the game"""
    global game_state
    
    data = request.json
    position = data.get('position')
    
    # Validate move
    if not (0 <= position < 9) or game_state['board'][position] != '':
        return jsonify({'error': 'Invalid move'}), 400
    
    if game_state['game_over']:
        return jsonify({'error': 'Game is over'}), 400
    
    # Make the move
    game_state['board'][position] = game_state['current_player']
    
    # Check for winner
    winner = check_winner(game_state['board'])
    if winner:
        game_state['winner'] = winner
        game_state['game_over'] = True
    # Check for draw
    elif is_board_full(game_state['board']):
        game_state['game_over'] = True
    else:
        # Switch player
        game_state['current_player'] = 'O' if game_state['current_player'] == 'X' else 'X'
    
    return jsonify(game_state)

@app.route('/api/reset', methods=['POST'])
def reset_game():
    """Reset the game"""
    global game_state
    game_state = {
        'board': ['', '', '', '', '', '', '', '', ''],
        'current_player': 'X',
        'game_over': False,
        'winner': None
    }
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
