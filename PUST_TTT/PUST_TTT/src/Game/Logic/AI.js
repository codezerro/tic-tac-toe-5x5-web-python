module Game.Logic.AI exposing (..)

import Game.Model exposing (GameState(..), Model)

import Game.Player as Player
import Game.Player exposing (..)
import Game.Player exposing (PlayerType(..))
import Game.Player exposing (Team(..))

import Game.Board as Board
import Game.Board exposing (Field(..), Board)

import Maybe exposing (Maybe(..))
import Array

import Game.Logic.Human as HumanLogic

import Debug

makeMove : Model -> Player -> Model
makeMove currentGame currentPlayer =
  let
    (bestMove, moveScore) = minimax currentGame currentPlayer True 3 currentGame.board

    newBoard = case bestMove of
      Nothing -> currentGame.board
      Just (rowIndex, colIndex) ->
        HumanLogic.markBoardPosition currentGame.board currentPlayer rowIndex colIndex
    newGameState = case bestMove of
      Nothing -> currentGame.gameState
      Just (rowIndex, colIndex) ->
        HumanLogic.checkGameState currentGame newBoard currentPlayer rowIndex colIndex
  in
    { currentGame | board = newBoard, gameState = newGameState }

-- https://www.thanassis.space/score4.html
minimax : Model -> Player -> Bool -> Int -> Board -> (Maybe (Int, Int), Int)
minimax currentGame player maximize depth board =
  case depth of
    0 -> (Nothing, scoreBoard currentGame player maximize board)
    _ ->
      let validMoves = findValidMoves board in
      case validMoves of
        [] -> (Nothing, scoreBoard currentGame player maximize board)
        _ ->
          let
            validMovesAndBoards = performMoves board validMoves player
            targetScore = if maximize then 10000 else -10000
            killerMoves = validMovesAndBoards
              |> List.map (\(move, board) -> (move, scoreBoard currentGame player maximize board))
              |> List.filter (\(_, score) -> score == targetScore)
          in
            case killerMoves of
              (killerMove, killerScore)::rest -> (Just killerMove, killerScore)
              [] ->
                let
                  validBoards = validMovesAndBoards |> List.map Tuple.second
                  bestScores = validBoards
                    |> List.map
                      (minimax currentGame (otherPlayer player currentGame) (not maximize) (depth - 1))
                    |> List.map Tuple.second
                  allData = List.map2 (,) validMoves bestScores
                  best = \((_, s1) as l) ((_, s2) as r) -> if s1 > s2 then l else r
                  worst = \((_, s1) as l) ((_, s2) as r) -> if s1 < s2 then l else r
                  (bestMove, bestScore) =
                    List.foldl
                      (if maximize then best else worst)
                      (case List.head allData of
                        Nothing -> ((0, 0), 0)
                        Just head -> head)
                      (case List.tail allData of
                        Nothing -> []
                        Just tail -> tail)
                in
                  (Just bestMove, bestScore)

scoreBoard : Model -> Player -> Bool -> Board -> Int
scoreBoard game player maximize board =
  let
    boardSize = Board.size board
    accumulator =
      { vertical = Array.initialize boardSize (\_ -> ((0, 0), (0, 0)))
      , horizontal = Array.initialize boardSize (\_ -> ((0, 0), (0, 0)))
      , diagonalRight = Array.initialize (boardSize * 2 - 1) (\_ -> ((0, 0), (0, 0)))
      , diagonalLeft = Array.initialize (boardSize * 2 - 1) (\_ -> ((0, 0), (0, 0)))
      }
    (mainPlayer, opponent) =
      if maximize then (player, (otherPlayer player game)) else ((otherPlayer player game), player)

    rejectUnlessWon = \sum potential ->
      ((if potential >= 4 then sum else 0), (if potential >= 4 then potential else 0))

    boardAnalysis = Board.reduce (\rowIndex colIndex field acc ->
      let
        updateAnalysis = \analysis at ->
          let
            ((mainSum, mainPotential), (otherSum, otherPotential)) =
              case Array.get at analysis of
                Just result -> result
                Nothing -> ((0, 0), (0, 0))

            newAnalysis =
              if HumanLogic.fieldMatchesPlayer field mainPlayer then
                ((mainSum + 1, mainPotential + 1), rejectUnlessWon otherSum otherPotential)
              else if HumanLogic.fieldMatchesPlayer field opponent then
                (rejectUnlessWon mainSum mainPotential, (otherSum + 1, otherPotential + 1))
              else
                ((mainSum, mainPotential + 1), (otherSum, otherPotential + 1))
          in
            Array.set at newAnalysis analysis

        { vertical, horizontal, diagonalRight, diagonalLeft } = acc

        newVertical = updateAnalysis vertical colIndex
        newHorizontal = updateAnalysis horizontal rowIndex
        newDiagonalRight = updateAnalysis diagonalRight (rowIndex - colIndex + boardSize - 1)
        newDiagonalLeft = updateAnalysis diagonalLeft (rowIndex + colIndex)

      in
        { acc | vertical = newVertical, horizontal = newHorizontal, diagonalRight = newDiagonalRight, diagonalLeft = newDiagonalLeft }) accumulator board
  in
    let
      sumAnalysis = \analysis ->
        Array.foldl (\analysis acc ->
          let
            ((mainSum, mainPotential), (otherSum, otherPotential)) = analysis
          in
            if mainSum >= 4 then 10000
            else if otherSum >= 4 then -10000
            else if (not (acc == 10000)) && (not (acc == -10000)) then
              acc +
                (if mainPotential >= 4 then mainSum else 0) -
                  (if otherPotential >= 4 then otherSum else 0)
            else acc) 0 analysis

      verticalScore = sumAnalysis boardAnalysis.vertical
      horizontalScore = sumAnalysis boardAnalysis.horizontal
      diagonalRightScore = sumAnalysis boardAnalysis.diagonalRight
      diagonalLeftScore = sumAnalysis boardAnalysis.diagonalLeft

      sum = verticalScore + horizontalScore + diagonalRightScore + diagonalLeftScore
    in
      if sum > 10000 then 10000 else if sum < -10000 then -10000 else sum

findValidMoves : Board -> List (Int, Int)
findValidMoves board =
  board |>
    Board.reduce (\rowIndex colIndex field acc ->
      case field of
        Empty -> (rowIndex, colIndex) :: acc
        _ -> acc) []

otherPlayer : Player -> Model -> Player
otherPlayer player game =
  if player == game.player1 then
    game.player2
  else
    game.player1

performMoves : Board -> List (Int, Int) -> Player -> List ((Int, Int), Board)
performMoves board moves player =
  moves
    |> List.map (\((rowIndex, colIndex) as move) ->
      (move, HumanLogic.markBoardPosition board player rowIndex colIndex))
