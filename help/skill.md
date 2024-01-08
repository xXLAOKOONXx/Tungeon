# Skill

```json
{
  "name":"precision",
  "display-name":"Precision",
  "description":"Aim precisely to deal more damage.",
  "functions":[
    {"functions-object"}
  ],
  "learning-cost-money":30,
  "learning-cost-improvement-points":1,
  "learning-required-skills":["prec"],
  "learning-removes-skills":["prec"],
  "other-skill-prevention":["prec"]
}
```

- name: name of the skill, used for reference
- display-name: name of the skill to show to the player
- description: description to show the player, not used yet
- functions: list of [functions](./function.md)
- learning-cost-money: money to spend for learning the skill
- learning-cost-improvement-points: improvement-points to spend for learning the skill
- learning-required-skills: skills the hero has to learn before learning this skill
- learning-removes-skills: skills a hero looses in case he learns this skill
- other-skill-prevention: skills a hero can no longer learn once the hero has this skill
