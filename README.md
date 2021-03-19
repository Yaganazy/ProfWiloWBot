# ProfWilowBot

Bot para ajudar um grupo de Pokémon GO no Telegram

### Funções
- [x] Calculadora de IV
- [ ] Criar lista de raids
- [ ] Criar lista com codigo de treinador dos membros do grupo

## Como usar

Baixe os arquivos, extraia, entre na pasta criada.
Crie um ambiente virtual: `python3 -m venv .env`
Ative o ambiente virtual: usando o **CMD**: `.env/bin/activate.bat` ou usando o **PowerShell**: `.env/bin/activate.ps1`
download the requirements for the bot to work: `pip install -r requeriments`

#### Pastas e arquivos

se você não tiver um arquivo chamado **config.toml** crie ele dentro da pasta **config** e se ela não existir crie-a.

```
ProfWilowBot
├── bot.py
├── Comandos.py
├── config
│   └── config.toml
├── README.md
└── requeriments
```

conteúdo do arquivo **config.toml**
`TOKEN='your TOKEN here'`

Dentro do arquivo **config.toml** coloque seu **TOKEN**, caso nao tenha um **TOKEN** fale com o [BotFather](https://t.me/BotFather) para criar um.