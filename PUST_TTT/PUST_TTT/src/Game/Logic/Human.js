module Game.Logic.Human exposing (..)

import Game.Model exposing (GameState(..), Model)

import Game.Player as Player
import Game.Player exposing (..)
import Game.Player exposing (PlayerType(..))
import Game.Player exposing (Team(..))

import Game.Board as Board
import Game.Board exposing (Field(..), Board)

makeMove : Model -> Player -> Int -> Int -> Model
makeMove currentGame currentPlayer changedRowIndex changedColIndex =
  let
    fieldIsTaken = currentGame.board |>
      Board.reduce (\rowIndex colIndex field acc ->
        if rowIndex == changedRowIndex && colIndex == changedColIndex then
          not (field == Board.Empty)
        else
          acc) False

    newBoard = if fieldIsTaken then currentGame.board else
      markBoardPosition currentGame.board currentPlayer changedRowIndex changedColIndex

    newGameState = if fieldIsTaken then currentGame.gameState else
      checkGameState currentGame newBoard currentPlayer changedRowIndex changedColIndex
  in
    { currentGame | board = newBoard, gameState = newGameState }

markBoardPosition : Board -> Player -> Int -> Int -> Board
markBoardPosition board player markedRowIndex markedColIndex =
  board |>
    Board.map (\rowIndex colIndex field ->
      if markedRowIndex == rowIndex && markedColIndex == colIndex then
        if player.team == Player.Cross then Board.Cross else Board.Circle
      else
        field)

checkGameState : Model -> Board -> Player -> Int -> Int -> GameState
checkGameState currentGame newBoard currentPlayer changedRowIndex changedColIndex =
  let
    (hasWon, isDraw) = checkWinCondition currentPlayer newBoard changedRowIndex changedColIndex
  in
    if hasWon then
      Winner currentPlayer
    else if isDraw then
      Draw
    else
      Turn (getOtherPlayer currentGame currentPlayer)

checkWinCondition : Player -> Board -> Int -> Int -> (Bool, Bool)
checkWinCondition currentPlayer newBoard changedRowIndex changedColIndex =
  let
    (noFieldsEmpty, vertical, horizontal, diagonalRight, diagonalLeft) =
      analyzeBoard newBoard currentPlayer changedRowIndex changedColIndex

    hasWon = (vertical >= 4) || (horizontal >= 4) || (diagonalRight >= 4) || (diagonalLeft >= 4)
    isDraw = (not hasWon) && noFieldsEmpty
  in
    (hasWon, isDraw)

getOtherPlayer : Model -> Player -> Player
getOtherPlayer game player =
  if player == game.player1 then
    game.player2
  else
    game.player1

fieldMatchesPlayer : Field -> Player -> Bool
fieldMatchesPlayer field player =
  field == Board.Circle && player.team == Player.Circle ||
    field == Board.Cross && player.team == Player.Cross

analyzeBoard : Board -> Player -> Int -> Int -> (Bool, Int, Int, Int, Int)
analyzeBoard board currentPlayer changedRowIndex changedColIndex =
  board |>
    Board.reduce
      (\rowIndex colIndex field (noFieldsEmpty, vertical, horizontal, diagonalRight, diagonalLeft) ->
        let
          newNoFieldsEmpty = noFieldsEmpty && (not (field == Board.Empty))

          newVertical =
            if colIndex == changedColIndex then
              if fieldMatchesPlayer field currentPlayer then
                vertical + 1
              else if vertical >= 4 then
                vertical
              else
                0
            else
              vertical

          newHorizontal =
            if rowIndex == changedRowIndex then
              if fieldMatchesPlayer field currentPlayer then
                horizontal + 1
              else if horizontal >= 4 then
                horizontal
              else
                0
            else
              horizontal

          newDiagonalRight =
            if rowIndex + colIndex == changedRowIndex + changedColIndex then
              if fieldMatchesPlayer field currentPlayer then
                diagonalRight + 1
              else if diagonalRight >= 4 then
                diagonalRight
              else
                0
            else
              diagonalRight

          newDiagonalLeft =
            if rowIndex - colIndex == changedRowIndex - changedColIndex then
              if fieldMatchesPlayer field currentPlayer then
                diagonalLeft + 1
              else if diagonalLeft >= 4 then
                diagonalLeft
              else
                0
            else
              diagonalLeft
        in
          (newNoFieldsEmpty, newVertical, newHorizontal, newDiagonalRight, newDiagonalLeft)) (True, 0, 0, 0, 0)
