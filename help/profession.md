# Profession

```json
{
  "name":"fighter",
  "display-name":"Fighter",
  "available-skills":[
    "penetration"
  ],
  "double-price-skills":[
    "precision"
  ],
  "starter-items":["sword"],
  "starter-money":10,
  "starter-skills":[
    {
      "is-roll":true,
      "roll-results":[
        ["penetration"]
      ]
    }
  ]
}
```

- name: name of the profession
- display-name: name of the profession to display to player
- available-skills: list of skills that are learnable by normal rates
- double-price-skills: list of skills that are learnable by doubled rates
- starter-items: list of item names the hero starts with
- starter-money: amount of money the hero starts with
- starter-skills: list of rolls the hero starts with
  - is-roll: should be true
  - roll-results: list of lists with skill names
