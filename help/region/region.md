# Region

```json
{
  "name":"town",
  "display-name":"Town",
  "available-regions":["fields"],
  "free-camping":true,
  "shop-items":[
    "sword",
    "shield"
  ],
  "trainable-skills":[
    "precision"
  ],
  "events":[
    {"step-object"}
  ]
}
```

- name: name of the region, used as reference
- display-name: name to show the player
- available-regions: list of adjacent regions in which the company can go to from the current region
- free-camping: flag whether camping is free in this region, free camping does not require a hero setting up a camp
- shop-items: list of items available for purchase within this region
- trainable-skills: list of skills that can be trained within this region while camping
- events: list of events that might happen in this region
