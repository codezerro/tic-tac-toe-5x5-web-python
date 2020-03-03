module Site.Base exposing (init, update, view, subscriptions)

import Html exposing (Html, button, select, option, text, div, span)
import Html.Events exposing (onClick, onInput, on)
import Html.Attributes exposing (..)
import Svg exposing (svg)
import Svg.Attributes exposing (..)
import Json.Decode as Json

import Game.Base as Game
import Game.Model as GameModel
import Game.Player exposing (..)

import Debug

type alias Model =
  { game : GameModel.Model
  , firstPlayerDropdownValue : String
  , secondPlayerDropdownValue : String
  }

type Msg
  = GameMsg Game.Msg
  | SelectFirstPlayerType String
  | SelectSecondPlayerType String

init : (Model, Cmd Msg)
init =
  (initialState, Cmd.none)

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    GameMsg gameMsg ->
      let
        (newGame, newMsg) = Game.update gameMsg model.game
      in
        ({ model | game = newGame }, Cmd.map GameMsg newMsg)
    SelectFirstPlayerType playerType ->
      ({ model | firstPlayerDropdownValue = playerType }, Cmd.none)
    SelectSecondPlayerType playerType ->
      ({ model | secondPlayerDropdownValue = playerType }, Cmd.none)

view : Model -> Html Msg
view model =
  pageContainer
    [ gameSettingsContainer
        [ span [] [ text "Cross: " ]
        , selectPlayerType SelectFirstPlayerType
        , span [ Html.Attributes.style [ ("margin-left", "10px") ] ] [ text "Circle: " ]
        , selectPlayerType SelectSecondPlayerType
        , startGameButton model
        , gameStateDescription model.game
        ]
    , svgContainer
        [ Html.map GameMsg (Game.view model.game) ]
    ]

subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none

-- private

initialState : Model
initialState =
  { game = Game.initialState
  , firstPlayerDropdownValue = "Human"
  , secondPlayerDropdownValue = "Human"
  }

pageContainer : List (Html Msg) -> Html Msg
pageContainer children =
  div
    [ Html.Attributes.style [ ("height", "100%"), ("width", "100%"), ("text-align", "center") ] ]
    children

gameSettingsContainer : List (Html Msg) -> Html Msg
gameSettingsContainer children =
  div [ Html.Attributes.style [ ("margin-bottom", "20px") ] ] children

svgContainer : List (Html Msg) -> Html Msg
svgContainer children =
  svg
    [ viewBox "0 0 1000 1000", Svg.Attributes.style "width: 90%; height: 90%;" ]
    children

selectPlayerType : (String -> Msg) -> Html Msg
selectPlayerType onSelection =
  select [ onInput onSelection ]
    [ option [ value "Human" ] [ text "Human" ]
    , option [ value "AI" ] [ text "AI" ]
    ]

startGameButton : Model -> Html Msg
startGameButton model =
  let
    startGameMsg = Game.startGame model.firstPlayerDropdownValue model.secondPlayerDropdownValue
  in
    Html.map GameMsg
      (button
        [ onClick startGameMsg
        , Html.Attributes.style [ ("margin-left", "10px") ]
        ] [ text "Start game" ])

gameStateDescription : GameModel.Model -> Html Msg
gameStateDescription game =
  let
    label = case game.gameState of
      GameModel.Stopped -> "Start the game"
      GameModel.Draw -> "Draw!"
      GameModel.Turn player -> (playerTeamToLabel player) ++ "'s turn" ++
        (if player.playerType == AI then " - click anywhere to trigger an AI move" else "")
      GameModel.Winner player -> (playerTeamToLabel player) ++ " has won!"
  in
    div [ Html.Attributes.style [ ("margin-left", "10px") ] ] [ text label ]

playerTeamToLabel : Player -> String
playerTeamToLabel player =
  if player.team == Cross then
    "Cross"
  else
    "Circle"
