module Game.Model exposing (GameState(..), Model)

import Game.Player exposing (..)
import Game.Player exposing (PlayerType(..))
import Game.Player exposing (Team(..))

import Game.Board as Board
import Game.Board exposing (Board)

type GameState
  = Stopped
  | Turn Player
  | Winner Player
  | Draw

type alias Model =
  { gameState : GameState
  , player1 : Player
  , player2 : Player
  , board : Board
  }
