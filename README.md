# update-environment

Scripts que gera arquivo temporario baseado no `.env.example` 
1. Transforma o arquivo removendo espaços, linhas vazias e comentários;
2. Ler as variaveis:
     Ex: `APP_NAME=Laravel` será transformado em `APP_NAME=$APP_NAME` 
     onde o valor da variável `$APP_NAME` 
3. Ler as variaveis armazenadas nos deployments do Repositorio.
4. Cria um arquivo `.env` com os valores exportados

## Usage 

1. Export some vars:
```
export APP_NAME=Laravel
export APP_ENV=local
export APP_KEY=
export APP_DEBUG=true
export APP_URL=http://localhost
```
2. Execute Shell:

```
chmod +x update-env.sh && sh update-env.sh
```
or 

2. Execute Python:

```
python3 update-env.py && envsubst < .env.tpl >> .env
```

