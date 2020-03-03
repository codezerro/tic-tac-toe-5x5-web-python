module Game.BoardRenderer exposing (..)

import Html exposing (Html)
import Svg exposing (..)
import Svg.Attributes exposing (..)
import Svg.Events exposing (..)

import Game.Board as Board
import Game.Board exposing (Board)
import Game.Board exposing (Field(..))

render : (Int -> Int -> msg) -> Board -> Html msg
render onFieldClickMsg board =
  Svg.g [] (drawFields onFieldClickMsg board)

-- private

drawFields : (Int -> Int -> msg) -> Board -> List (Html msg)
drawFields onFieldClickMsg board =
  (Board.reduce (appendRect onFieldClickMsg) [] board)

appendRect : (Int -> Int -> msg) -> Int -> Int -> Field -> List (Html msg) -> List (Html msg)
appendRect onFieldClickMsg rowIndex colIndex field acc =
  List.append acc [ drawField onFieldClickMsg rowIndex colIndex field ]

drawField : (Int -> Int -> msg) -> Int -> Int -> Field -> Html msg
drawField onFieldClickMsg rowIndex colIndex field =
  Svg.svg
    [ x (toString (colIndex * 200))
    , y (toString (rowIndex * 200))
    ]
    [ fieldBorder onFieldClickMsg
    , fieldInsides onFieldClickMsg field
    , eventCapture onFieldClickMsg rowIndex colIndex
    ]

fieldBorder : (Int -> Int -> msg) -> Html msg
fieldBorder onFieldClickMsg =
  Svg.rect
    [ width "200"
    , height "200"
    , fill "white"
    , stroke "black"
    ] []

fieldInsides : (Int -> Int -> msg) -> Field -> Html msg
fieldInsides onFieldClickMsg field =
  case field of
    Empty -> Svg.g [] []
    Cross -> cross onFieldClickMsg
    Circle -> circle onFieldClickMsg

circle : (Int -> Int -> msg) -> Html msg
circle onFieldClickMsg =
  Svg.circle [ cx "100", cy "100", r "90", fill "white", stroke "black" ] []

cross : (Int -> Int -> msg) -> Html msg
cross onFieldClickMsg =
  Svg.g []
  [ Svg.line [ x1 "10", y1 "10", x2 "190", y2 "190", stroke "black" ] []
  , Svg.line [ x1 "10", y1 "190", x2 "190", y2 "10", stroke "black" ] []
  ]

eventCapture : (Int -> Int -> msg) -> Int -> Int -> Html msg
eventCapture onFieldClickMsg rowIndex colIndex =
  Svg.rect
    [ opacity "0", height "200", width "200", onClick (onFieldClickMsg rowIndex colIndex) ] []
