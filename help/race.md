# Race

```json
{
  "name":"human",
  "display-name":"Human",
  "speed-base":2,
  "speed-upgrades":{
    "3":1,
    "4":3,
    "5":5
  },
  "strength-base":2,
  "strength-upgrades":{
    "3":1,
    "4":3,
    "5":5
  },
  "agility-base":2,
  "agility-upgrades":{
    "3":1,
    "4":3,
    "5":5
  },
  "intelligence-base":2,
  "intelligence-upgrades":{
    "3":1,
    "4":3,
    "5":5
  },
  "origin-regions":[
    "town"
  ],
  "additional-regionslots":2
}
```

- name: name of the race, used for reference
- display-name: name of the race to display to the user
- speed-base: starting value for speed
- speed-upgrades: dictionary of target value and cost in improvement-points
- strength-base: starting value for strength
- strength-upgrades: dictionary of target value and cost in improvement-points
- agility-base: starting value for agility
- agility-upgrades: dictionary of target value and cost in improvement-points
- intelligence-base: starting value for intelligence
- intelligence-upgrades: dictionary of target value and cost in improvement-points
- origin-regions: list of regions the race comes from
- additional-regionslots: amount of addtional regions the race might learn
