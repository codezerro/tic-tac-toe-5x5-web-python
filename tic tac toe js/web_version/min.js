
def minmax2(self, depth, isMax, alpha, beta, startTime, timeLimit):

    moves = self.genrate()
    # print(moves)
    score = self.evaluate()
    position = None

    if datetime.datetime.now() - startTime >= timeLimit:
        self.mTimePassed = True

    if not moves or depth == 0 or self.mTimePassed:
        gameResult = self.checkGameState()
        if gameResult.value == 'X':
            return -10**(self.mBoard.mSize+1), position
        elif gameResult.value == 'O':
            return 10**(self.mBoard.mSize+1), position
        elif gameResult.value == 'Tie':
            return 0, position
        return score, position

    if isMax:
        for i in moves:
            self.mBoard.drawO(i)
            score, dummy = self.minmax2(
                depth-1, not isMax, alpha, beta, startTime, timeLimit)
            if score > alpha:
                alpha = score
                position = i
                self.mBestMove = i

            self.mBoard.drawEmpty(i)
            if beta <= alpha:
                break

        return alpha, position
    else:
        for i in moves:
            self.mBoard.drawX(i)
            score, dummy = self.minmax2(
                depth-1, not isMax, alpha, beta, startTime, timeLimit)
            if score < beta:
                beta = score
                position = i
                self.mBestMove = i
            self.mBoard.drawEmpty(i)
            if alpha >= beta:
                break

        return beta, position

// # """this function search the best move it find in 5 seconds.
// #    The function goes as deep as possible in 5 second in the game tree
// #    and return the best move"""

function iterativeDeepSearch(){
    // const d = new Date();
    // const endTime = 5.000; //datetime.timedelta(0, SEARCH_TIME)
    const depth = 1
    const position = null;
    const mTimePassed = false
    while (true){
        const d = new Date();
        // currentTime=d/1000;
        // if (currentTime >= endTime){
        //     break
        // }
        setTimeout()
        best, position = self.minmax2(
            depth, true, -10000000, 10000000)
        depth += 1
    }
    // if position is None:
    //     position = self.mBestMove

    return position
}