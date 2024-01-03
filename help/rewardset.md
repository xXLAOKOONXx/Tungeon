# Rewardset

```json
{
  "name":"simple",
  "display-name":"Simple",
  "description":"simple rewards",
  "rewards":[
    {
      "values":[0],
      "money":1,
      "items":["sword"],
      "rewardset-draws":[
        {
          "rewardset-name":"simple",
          "draw-d10-count":1,
          "draw-base":0
        }
      ]
    }
  ]
}
```

- name: name of the rewardset to use as reference
- display-name: name of the rewardset to display
- description: description of the rewardset, currently not used
- rewards: list of available rewards
  - values: list of values the reward counts for
  - money: money the company receives
  - items: items the company receives
  - rewardset-draws: draws in rewardsets the company receives
    - rewardset-name: rewardset to use for draw
    - draw-d10-count: number of d10 to roll for the rewardset
    - draw-base: base value to use for the reward draw
