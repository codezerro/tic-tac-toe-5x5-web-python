// define human and computer

var HUMAN = -1;
var COMP = +1;
// predefine board game
var board = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
];

// check empty cell or not
function emptyCells(state) {
	var cells = [];
	for (var x = 0; x < 5; x++) {
		for (var y = 0; y < 5; y++) {
			if (state[x][y] == 0) cells.push([x, y]);
		}
	}

	return cells;
}

// valid move function
/* A move is valid if the chosen cell is empty */
function validMove(x, y) {
	var empties = emptyCells(board);
	try {
		if (board[x][y] == 0) {
			return true;
		} else {
			return false;
		}
	} catch (e) {
		return false;
	}
}

/* Set the move on board, if the coordinates are valid */
function setMove(x, y, player) {
	if (validMove(x, y)) {
		board[x][y] = player;
		return true;
	} else {
		return false;
	}
}

/* This function tests if a specific player wins */
function gameOver(state, player) {
	var win_state = [
		[state[0][0], state[1][1], state[2][2], state[3][3], state[4][4]],
		[state[0][0], state[0][1], state[0][2], state[0][3], state[0][4]],
		[state[0][0], state[1][0], state[2][0], state[3][0], state[4][0]],
		[state[0][1], state[1][1], state[2][1], state[3][1], state[4][1]],
		[state[0][2], state[1][2], state[2][2], state[3][2], state[4][2]],
		[state[0][3], state[1][3], state[2][3], state[3][3], state[4][3]],
		[state[0][4], state[1][4], state[2][4], state[3][4], state[4][4]],
		[state[1][0], state[1][1], state[1][2], state[1][3], state[1][4]],
		[state[2][0], state[2][1], state[2][2], state[2][3], state[2][4]],
		[state[3][0], state[3][1], state[3][2], state[3][3], state[3][4]],
		[state[4][0], state[4][1], state[4][2], state[4][3], state[4][4]],
		[state[0][4], state[1][3], state[2][2], state[3][1], state[4][0]],
	];

	for (var i = 0; i < 12; i++) {
		var line = win_state[i];
		var filled = 0;
		for (var j = 0; j < 5; j++) {
			if (line[j] == player) filled++;
		}
		if (filled == 5) return true;
	}
	return false;
}

function gameOverAll(state) {
	return gameOver(state, HUMAN) || gameOver(state, COMP);
}

// todo code for ai
/* Function to heuristic evaluation of state. */
function evalute(state) {
	// console.log('hello');
	var score = 0;

	if (gameOver(state, COMP)) {
		score = +1;
	} else if (gameOver(state, HUMAN)) {
		score = -1;
	} else {
		score = 0;
	}

	return score;
}

/* *** AI function that choice the best move *** */
function minimax(state, depth, player) {
	var best;

	if (player == COMP) {
		best = [-1, -1, -10000];
	} else {
		best = [-1, -1, +10000];
	}

	if (depth == 0 || gameOverAll(state)) {
		var score = evalute(state);
		return [-1, -1, score];
	}

	emptyCells(state).forEach(function(cell) {
		var x = cell[0];
		var y = cell[1];
		state[x][y] = player;
		var score = minimax(state, depth - 1, -player);
		state[x][y] = 0;
		score[0] = x;
		score[1] = y;

		if (player == COMP) {
			if (score[2] > best[2]) best = score;
		} else {
			if (score[2] < best[2]) best = score;
		}
	});

	return best;
}
/* It calls the minimax function */
function aiTurn() {
	var x, y;
	var move;
	var cell;

	if (emptyCells(board).length == 25) {
		x = parseInt(Math.random() * 4);
		y = parseInt(Math.random() * 4);
	} else {
		move = minimax(board, 5, COMP); //emptyCells(board).length
		x = move[0];
		y = move[1];
	}

	if (setMove(x, y, COMP)) {
		cell = document.getElementById(String(x) + String(y));
		cell.innerHTML = 'O';
	}
}
// todo code end for ai

/* main  */
function clickedCell(cell) {
	var button = document.getElementById('bnt-restart');
	button.disabled = true;
	var conditionToContinue = gameOverAll(board) == false && emptyCells(board).length > 0;
	// conditionToContinue = true;
	if (conditionToContinue == true) {
		var x = cell.id.split('')[0];
		var y = cell.id.split('')[1];
		// console.log(x);
		var move = setMove(x, y, HUMAN);
		if (move == true) {
			cell.innerHTML = 'X';
			if (conditionToContinue) {
				setTimeout(() => {
					aiTurn();
				}, 1);
			}
		}
	}
	if (gameOver(board, COMP)) {
		var lines;
		var cell;
		var msg;

		if (board[0][0] == 1 && board[1][1] == 1 && board[2][2] == 1 && board[3][3] == 1 && board[4][4] == 1) {
			lines = [
				[0, 0],
				[1, 1],
				[2, 2],
				[3, 3],
				[4, 4],
			];
		} else if (board[0][0] == 1 && board[0][1] == 1 && board[0][2] == 1 && board[0][3] == 1 && board[0][4] == 1) {
			lines = [
				[0, 0],
				[0, 1],
				[0, 2],
				[0, 3],
				[0, 4],
			];
		} else if (board[0][0] == 1 && board[1][0] == 1 && board[2][0] == 1 && board[3][0] == 1 && board[4][0] == 1) {
			lines = [
				[0, 0],
				[1, 0],
				[2, 0],
				[3, 0],
				[4, 0],
			];
		} else if (board[0][1] == 1 && board[1][1] == 1 && board[2][1] == 1 && board[3][1] == 1 && board[4][1] == 1) {
			lines = [
				[0, 1],
				[1, 1],
				[2, 1],
				[3, 1],
				[4, 1],
			];
		} else if (board[0][2] == 1 && board[1][2] == 1 && board[2][2] == 1 && board[3][2] == 1 && board[4][2] == 1) {
			lines = [
				[0, 2],
				[1, 2],
				[2, 2],
				[3, 2],
				[4, 2],
			];
		} else if (board[0][3] == 1 && board[1][3] == 1 && board[2][3] == 1 && board[3][3] == 1 && board[4][3] == 1) {
			lines = [
				[0, 3],
				[1, 3],
				[2, 3],
				[3, 3],
				[4, 3],
			];
		} else if (board[0][4] == 1 && board[1][4] == 1 && board[2][4] == 1 && board[3][4] == 1 && board[4][4] == 1) {
			lines = [
				[0, 4],
				[1, 4],
				[2, 4],
				[3, 4],
				[4, 4],
			];
		} else if (board[1][0] == 1 && board[1][1] == 1 && board[1][2] == 1 && board[1][3] == 1 && board[1][4] == 1) {
			lines = [
				[1, 0],
				[1, 1],
				[1, 2],
				[1, 3],
				[1, 4],
			];
		} else if (board[2][0] == 1 && board[2][1] == 1 && board[2][2] == 1 && board[2][3] == 1 && board[2][4] == 1) {
			lines = [
				[2, 0],
				[2, 1],
				[2, 2],
				[2, 3],
				[2, 4],
			];
		} else if (board[3][0] == 1 && board[3][1] == 1 && board[3][2] == 1 && board[3][3] == 1 && board[3][4] == 1) {
			lines = [
				[2, 0],
				[2, 1],
				[2, 2],
				[2, 3],
				[2, 4],
			];
		} else if (board[4][0] == 1 && board[4][1] == 1 && board[4][2] == 1 && board[4][3] == 1 && board[4][4] == 1) {
			lines = [
				[4, 0],
				[4, 1],
				[4, 2],
				[4, 3],
				[4, 4],
			];
		} else if (board[4][0] == 1 && board[4][1] == 1 && board[4][2] == 1 && board[4][3] == 1 && board[4][4] == 1) {
			lines = [
				[4, 0],
				[4, 1],
				[4, 2],
				[4, 3],
				[4, 4],
			];
		} else if (board[0][4] == 1 && board[1][3] == 1 && board[2][2] == 1 && board[3][1] == 1 && board[4][0] == 1) {
			lines = [
				[0, 4],
				[1, 3],
				[3, 2],
				[3, 1],
				[4, 0],
			];
		}

		for (var i = 0; i < lines.length; i++) {
			cell = document.getElementById(String(lines[i][0]) + String(lines[i][1]));
			cell.style.color = 'red';
		}

		msg = document.getElementById('message');
		msg.innerHTML = 'You lose!';
	}
	if (emptyCells(board).length == 0 && !gameOverAll(board)) {
		var msg = document.getElementById('message');
		msg.innerHTML = 'Draw!';
	}
	if (gameOverAll(board) == true || emptyCells(board).length == 0) {
		button.value = 'Restart';
		button.disabled = false;
	}
}

/* Restart the game*/
function restartBnt(button) {
	if (button.value == 'Start AI') {
		aiTurn();
		button.disabled = true;
	} else if (button.value == 'Restart') {
		var htmlBoard;
		var msg;

		for (var x = 0; x < 5; x++) {
			for (var y = 0; y < 5; y++) {
				board[x][y] = 0;
				htmlBoard = document.getElementById(String(x) + String(y));
				htmlBoard.style.color = '#444';
				htmlBoard.innerHTML = '';
			}
		}
		button.value = 'Start AI';
		msg = document.getElementById('message');
		msg.innerHTML = '';
	}
}
