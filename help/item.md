# Item

## Example

```json
{
  "name":"silberschwert",
  "display-name":"Silbernes Schwert",
  "is-weapon":true,
  "is-melee":true,
  "damage":1,
  "money-value":60,
  "required-hands":1,
  "resistance":0,
  "functions":[{"function-object"}]
}
```

- name: name of item, used as reference
- display-name: name to show the player
- is-weapon: Flag that the item is a weapon
- is-melee: Flag that the item is for melee usage, used for weapons only, not being melee equals being ranged
- damage: damage of the item
- money-value: value of the item, optional
- required-hands: number of hands required to hold the item, used for weapons and shields
- resistance: resistance value, used primarely for armor and shield
- functions: list of [functions](./function.md) the item has
