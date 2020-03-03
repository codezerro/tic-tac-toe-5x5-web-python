module Game.Base exposing (initialState, update, view, Msg, startGame)

import Html exposing (Html)

import Game.Model exposing (GameState(..), Model)

import Game.Player exposing (..)
import Game.Player exposing (PlayerType(..))
import Game.Player exposing (Team(..))
import Game.BoardRenderer as BoardRenderer
import Game.Board as Board
import Game.Board exposing (Board)
import Game.Logic.Human as HumanLogic
import Game.Logic.AI as AILogic

import Debug

type Msg
  = StartGame Player Player
  | OnFieldClick Int Int

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    StartGame player1 player2 ->
      let
        newModel =
          { model |
            gameState = Turn player1
          , board = Board.initFiveByFive
          , player1 = player1
          , player2 = player2
          }
      in
        (newModel, Cmd.none)

    OnFieldClick rowIndex colIndex ->
      case model.gameState of
        Turn player ->
          case player.playerType of
            AI ->
              let
                newGame = AILogic.makeMove model player
              in
                (newGame, Cmd.none)

            Human ->
              let
                newGame = HumanLogic.makeMove model player rowIndex colIndex
              in
                (newGame, Cmd.none)

            None -> (model, Cmd.none)

        _ -> (model, Cmd.none)

view : Model -> Html Msg
view model =
  BoardRenderer.render OnFieldClick model.board

initialState : Model
initialState =
  { gameState = Stopped
  , player1 = Player None Cross
  , player2 = Player None Circle
  , board = Board.initFiveByFive
  }

startGame : String -> String -> Msg
startGame player1type player2type =
  let
    player1 = Player (playerType player1type) Cross
    player2 = Player (playerType player2type) Circle
  in
    StartGame player1 player2

-- private

playerType : String -> PlayerType
playerType stringPlayerType =
  case stringPlayerType of
    "Human" -> Human
    "AI" -> AI
    _ -> Debug.crash "not supported you dingus"
