# Function

## General

```json
{
  "condition-type":"round-preperation",
  "function-groups":["music"]
}
```

- condition-type: type of function
- function-groups: groups the function is part of, used for limiting the amount of functions of a group used

## Base Skill Check

```json
{
  "..."
  "base-skill-check":{
    "is-intelligence":true,
    "is-agility":false,
    "is-strength":false,
    "is-speed":false,
    "check-modifier":0,
    "check-types":["intelligence", "fight-related"]
  }
}
```

- base-skill-check: base skill check that needs to be successful to apply effects
  - is-intelligence: flag whether check is performed against intelligence
  - is-agility: flag whether check is performed against agility
  - is-strength: flag whether check is performed against strength
  - is-speed: flag whether check is performed against speed
  - check-modifier: modifier applied to the skill check
  - check-types: types the check might fit under

## Dice Reroll

```json
{
  "condition-type":"dice-reroll",
  "reroll-types":["fight"]
}
```

## Fight

```json
{
  "condition-type":"fight",
  "fight-enemy-types":["undead"],
  "fight-type":"melee",
  "fight-enemy-min":4,
  "fight-voluntary-required":true,
  "fight-rounds":[1],
  
  "fight-flat-bonus":1,

  "resistance-passing":2,
  "resistance-surpassing":false,

  "resistance-bonus":1
}
```

Function only works if all requirements are met.

- condition-type: "fight" for fight functionality
- fight-enemy-types: list of enemy types the functionality works against
- fight-type: type of the fight, "melee" or "ranged"
- fight-enemy-min: minimum amount of enemies required
- fight-voluntary-required: Flag if the fight needs to be voluntary
- fight-rounds: rounds the function might be available

- fight-flat-bonus: additional damage

- resistance-passing: value of resistance the hero can pass
- resistance-surpassing: flag whether the resistance passing can surpass 0 and can turn into negative armor values

- resistance-bonus: resistance the hero might receive

## Round Preperation

```json
{
  "condition-type":"round-preperation",
  "wound-reduce":1,
  "strength-bonus":1,
  "speed-bonus":1,
  "agility-bonus":1,
  "intelligence-bonus":1,
  "additional-rounds":0,
  "other-hero-allowed":true,
}
```

- condition-type: "round-preperation" for round preperation
- wound-reduce: number of wounds reduced
- strength-bonus: strength the hero receives temporarily
- speed-bonus: speed the hero receives temporarily
- agility-bonus: agility the hero receives temporarily
- intelligence-bonus: intelligence the hero receives temporarily
- additional-rounds: number of additional rounds the effect stays
- other-hero-allowed: flag whether the described effects can be applied to a different hero
