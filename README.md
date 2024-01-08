# Tungeon

Check out the [documentation pages](https://xxlaokoonxx.github.io/Tungeon/)

Find the newest [releases](https://github.com/xXLaokoonXx/Tungeon/releases).

## Configuration

Playing the game requires a world to be played in. You can define the world in a config folder.

For a detailed explaination on how to set up such a configuration see [config](./help/instruction.md)

## Development

### Console App

Build Console App EXE

```bash
poetry run pyinstaller console-app.spec
```

### Documentation

In poetry shell

Build rst files for modules

```bash
sphinx-apidoc -o docs .
```

Build html documentation

```bash
./make.bat html
```

### TODOs

- weapon-type: prop of item and filter in function
- additive drawing

- functions:
  - Meucheln: Töte Gegner vor dem Kampf
  - Diebstahl: stehle ggnstnd in ereignissen; stehlen beim Lagern
  - reroll as round bonus

- ereignisse
  - 1o1 fight ereignisse
  - aussetzen
  - fight + loose => thief behavior
  - enemy using functions e.g. round based bonus
  - poison
  - poisoned-wounds
  - trade
