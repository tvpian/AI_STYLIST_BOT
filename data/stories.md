## dress path 1
* greet
  - utter_greet
* dress_search{"occasion": "party", "bodyshape": "hourglass"}
  - slot{"bodyshape":"hourglass"}
  - slot{"occasion":"party"}
  - action_dress_search
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## dress path 2
* greet
  - utter_greet
* dress_search{"occasion": "wedding", "bodyshape": "petite"}
  - slot{"occasion":"wedding"}
  - slot{"bodyshape":"petite"}
  - action_dress_search
  - utter_did_that_help
* deny
  - utter_ask_again
* dress_search{"occasion": "wedding", "bodyshape": "petite"}
  - slot{"occasion":"wedding"}
  - slot{"bodyshape":"petite"}
  - action_dress_search
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude

## dress path 3
* dress_search{"occasion": "formal affair", "bodyshape": "pear"}
  - slot{"occasion":"formal affair"}
  - slot{"bodyshape":"athletic"}
  - action_dress_search
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude

## greet path
* greet
  - utter_greet

## goodbye path
* goodbye
  - utter_goodbye

## dress path restart
* dress_search{"occasion": "date", "bodyshape": "hourglass"}
    - slot{"occasion":"date"}
    - slot{"bodyshape":"hourglass"}
    - action_dress_search
    - utter_did_that_help
* deny
    - utter_ask_again
* dress_search{"occasion": "everyday", "bodyshape": "straight & narrow"}
    - slot{"occasion":"everyday"}
    - slot{"bodyshape":"straight & narrow"}
    - action_dress_search
    - utter_did_that_help
* thanks
    - utter_gratitude
* goodbye
    - utter_goodbye