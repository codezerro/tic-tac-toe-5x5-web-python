import Html

import Site.Base as Site

main =
  Html.program
    { init = Site.init
    , update = Site.update
    , view = Site.view
    , subscriptions = Site.subscriptions
    }
