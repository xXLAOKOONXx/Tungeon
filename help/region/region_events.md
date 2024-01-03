# Region Event

Each region event consists of steps which link to one another.  
I recommend to use one step only for a specific function and not to mix different effects into the same step.  
The step with id 0 is the entry point of the event.

```json
{
  "name":"temple",
  "display-name":"Temple",
  "values":[1,2],
  "steps":[
    {"step-object"}
  ]
}
```

- name: name for the event, could be used for reference, not used yet
- display-name: name to display to player, not used yet
- values: list of int values that lead to this event
- steps: list of step objects

## Step Examples

### Base

"next-step" is the default step id to go to if "yes", "no", "fight-win" or similar are not set.

### Decision

```json
{
  "id":0,
  "text":"Do you want to enter the cave?",
  "decision":true,
  "yes":1,
  "no":2
}
```

- id: id of the step
- text: description text for player
- decision: flag that this step is a decision
- yes: step id if player answers with yes
- no: step id if player answers with no

### Fight

```json
{
  "id":0,
  "is-fight":true,
  "fight-enemy-count":3,
  "fight-enemy-types":["undead"],
  "fight-enemy-dice":3,
  "fight-enemy-base-damage":6,
  "fight-enemy-resistance":0,
  "fight-thief-count":1,
  "fight-win":1,
  "fight-tie":2,
  "fight-loose":3
}
```

- id: id of the step
- text: description text for player
- is-fight: Flag that this is a fight
- fight-enemy-count: count of enemies
- fight-enemy-types: list of types the enemy is
- fight-enemy-dice: number of (6-sided) dice to roll for the enemy
- fight-enemy-base-damage: base damage value for the enemy
- fight-enemy-resistance: resistance of the enemy group
- fight-thief-count: number of thiefs in the enemy team, not implemented yet
- fight-win: step id to go to if the player wins
- fight-tie: step id to go to if the fight ends in a tie
- fight-loose: step-id to go to if the player lost

### Learn Skills

```json
{
  "id":0,
  "required-professions":["fighter"],
  "learn-skills":[
    {
      "skill-name":"precision",
      "money":30,
      "points":1
    }
  ],
  "yes":1,
  "no":2
}
```

- id: id of the step
- required-professions: professions that might learn skills, optional
- learn-skills:  list of skills that might be learned
  - skill-name: name of the skill that might be learned
  - money: money cost of learning
  - points: amounts of improvement points required for learning
- yes: step id to go to if at least one skill was learned
- no: step id to go to if no skill was learned

### Money Loss

```json
{
  "id":0,
  "text":"You loose 10 money.",
  "money-loss":5,
  "unable-to-pay":1
}
```

- id: id of the step
- text: description text for player
- money-loss: money the company looses in this step
- unable-to-pay: next step id if the company is unable to pay

### Profession Check

```json
{
  "id":0,
  "profession-check":true,
  "required-professions":["fighter"],
  "yes":1,
  "no":2
}
```

- id: id of the step
- profession-check: required flag for profession check
- required-professions: list of professions to check for
- yes: step id to go to if at least one hero has one of the professions
- no: step id to go to instead of yes

### Rewards

```json
{
  "id":0,
  "text":"You find several items",
  "is-reward":true,
  "reward-improvement-points":1,
  "reward-gold":1,
  "reward-items":["sword"],
  "reward-draws":[
    {
      "rewardset-name":"simple",
      "draw-d6-count":2,
      "draw-base":-2
    }
  ]
}
```

- id: id of the step
- text: description text for player
- is-reward: required flag for reward distribution
- reward-improvement-points: amount of improvement points received
- reward-gold: money the player receives
- reward-items: list of item names the player receives
- reward-draws: list of draws the player receives
  - rewardset-name: name of the rewardset the draw is using
  - draw-d6-count: number of dices rolled, also supported are d10 and d100
  - draw-base: value that is added to the dice roll number, can be negative

### Steals

```json
{
  "id":0,
  "text":"You get robbed.",
  "is-steal":true,
  "steal-types":["money","active","melee","ranged","armor","shield","backpack"],
  "can-miss":false,
  "backpack-parts":true
}
```

- id: id of the step
- text: description text for player
- is-steal: required flag for stealing
- steal-types: list of slots the thief might steal from
- can-miss: flag whether or not it can happen that the thief does not steal anything (as he looks in the wrong place)
- backpack-parts: flag whether the thief steals parts from within backpack or the whole backpack
