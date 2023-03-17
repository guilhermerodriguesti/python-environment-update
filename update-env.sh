#!/bin/bash
# sh update-env.sh
# Transforma o .env.example em .env com as variaveis do deployments
    sed -e 's/=.*//' -e 's/^[^=]*=//' -e '/^\s*#.*$/d' -e '/^\s*$/d' .env.example >.env.temp

    while read -r line || [[ -n "$line" ]]; do
      KEY="$(cut -f1 -d= <<<$line)"
      echo "$KEY=\"\$$KEY\"" >>.env.${APP_ENV}
    done <.env.temp
    #envsubst is included in gettext package.Ex: install gettext
    envsubst < .env.${APP_ENV} >> .env
    
    rm -rf .env.temp
    rm -rf .env.${APP_ENV}
    #rm -rf .env.example