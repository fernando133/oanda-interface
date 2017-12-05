# oanda-interface
Controll Interface for OANDA Trade API:
<br/>```http://developer.oanda.com/```

The project is for who want to automate the trading process of many instruments in OANDA plataform.

## script_conf.json

Should create the script_conf.json in the ```/conf``` folder with the ```API Key``` and ```ID``` of the account

```json
{
    "script-conf":{
        "oanda":{
            "secret"       : "API_KEY", 
            "account_id"   : "ACCOUNT_ID",
         }
    }
}
```
