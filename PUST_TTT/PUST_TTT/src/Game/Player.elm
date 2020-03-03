module Game.Player exposing (PlayerType(..), Team(..), Player)

type PlayerType
  = AI
  | Human
  | None

type Team
 = Cross
 | Circle

type alias Player =
  { playerType : PlayerType
  , team : Team
  }
