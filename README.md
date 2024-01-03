# Tungeon

## Configuration

see [config](./help/instruction.md)

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
