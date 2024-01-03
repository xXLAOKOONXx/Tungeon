# Tungeon

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
