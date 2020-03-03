module Game.Board exposing (..)

import Game.Player exposing (Team(..))

import List

type Field
  = Empty
  | Cross
  | Circle

type alias Board =
  List (List Field)

initFiveByFive : Board
initFiveByFive =
    [ [ Empty, Empty, Empty, Empty, Empty ]
    , [ Empty, Empty, Empty, Empty, Empty ]
    , [ Empty, Empty, Empty, Empty, Empty ]
    , [ Empty, Empty, Empty, Empty, Empty ]
    , [ Empty, Empty, Empty, Empty, Empty ]
    ]

map : (Int -> Int -> Field -> Field) -> Board -> Board
map fn board =
  board |>
    List.indexedMap (\rowIndex row ->
      row |>
        List.indexedMap (\colIndex field -> fn rowIndex colIndex field))

reduce : (Int -> Int -> Field -> a -> a) -> a -> Board -> a
reduce fn initAcc board =
  List.foldl
    (\(row, rowIndex) accRow ->
      List.foldl (\(field, colIndex) acc -> fn rowIndex colIndex field acc)
        accRow
        (listWithIndices row))
    initAcc
    (listWithIndices board)

listWithIndices : List a -> List (a, Int)
listWithIndices list =
  List.map2 (,) list (List.range 0 ((List.length list) - 1))

size : Board -> Int
size board =
  List.length board

