{
  "name": "Dèvílẞø†",
  "description": "The best userbot made by @lucifeermorningstar. Made with Love And Phone And Hardwork and... Nhi aur kahi se to nhi bana....For Support Join @DevilUserBot ",
  "logo": " https://telegra.ph/file/fbe697363d312fec4b671.jpg ",
    "keywords": [
    "telegram",
    "userbot",
    "plugin",
    "modular",
    "productivity"
  ],
  "repository": "https://github.com/theshubhamgundu/chat",
  "website": "https://github.com/lucifeermorningstar/Devil-User-Bot",
  "success_url": "https://t.me/DevilUserBot",
  "env": {
    "ENV": {
      "description": "Setting this to ANYTHING will enable heroku.",
      "value": "ANYTHING"
    },
    "TEMP_DOWNLOAD_DIRECTORY": {
      "description": "Where downloaded files will go.",
      "value": "./userbot/DOWNLOADS/",
      "required": false
    },
    "ALIVE_NAME": {
      "description": "Fill your Full name. By default it is DevilUserBot User",
      "value": "",
      "required": false
    },
    "ALIVE_MSG": {
      "description": "Set Custom Alive Message When entering .hell Command.",
      "value": "",
      "required": false
    },
    "ALIVE_PIC": {
      "description": "Put here any telegraph media link for alive pic in .hell command.",
      "value": "",
      "required": false
    },
    "BIO_MSG": {
      "description": "Put Your Telegram Bio Here Required For Auto Bio.",
      "value": "",
      "required": false
    },
    "PMPERMIT_PIC": {
      "description": "put here any telegraph media link for custom pmpermit pic.",
      "value": "",
      "required": true
    },
    "CUSTOM_PMPERMIT": {
      "description": "Enter Your custom pm permit msg.",
      "value": "",
      "required": false
    },
    "PM_PERMIT_GROUP_ID": {
      "description": "Put an Group Id Same As PRIVATE_GROUP_ID Required For Pmpermit plugin.",
      "value": "",
      "required": true
    },
    "APP_ID": {
      "description": "Get this value from my.telegram.org! Putting Others Value may result In Account Ban.",
      "value": ""
    },
    "REM_BG_API_KEY": {
      "description": "Required for Removing image background. Get your api key from https://www.remove.bg/",
      "value": "",
      "required": false
    },
    "OCR_SPACE_API_KEY": {
      "description": "Register an account on ocr.space to get this value(API key)....",
      "value": "",
      "required": false
    },
    "LYDIA_API_KEY": {
      "description": "Needed for Lydia AI. Follow https://telegra.ph/Lydia-09-05 to get your API.",
      "value": "",
      "required": false
    },
    "API_HASH": {
      "description": "Get this value from my.telegram.org! Putting Others Value May result In Account Ban.",
      "value": ""
    },
    "PLUGIN_CHANNEL": {
      "description": "Create a private group add rose  then type /id. PLUGIN_CHANNEL and PRIVATE_GROUP_ID both values should be same",
      "value": ""
    },
    "PRIVATE_GROUP_BOT_API_ID": {
      "description": "create a private channel and then type .get_id add that value here for save messages",
      "value": ""
    },
    "PRIVATE_GROUP_ID": {
      "description": "Create a private group add rose bot then type /id. PLUGIN_CHANNEL and PRIVATE_GROUP_ID both values should be same",
      "value": ""
    },
    "PM_LOGGR_BOT_API_ID": {
       "description": "for login private messages create a private channel and do .get_id and add that id", 
       "value": ""
    }, 
    "STRING_SESSION": {
      "description": "Get this value by running  https://repl.it/@lucifeermorning/DevilUserBot#main.py ",
      "value": ""
    },
    "HEROKU_API_KEY": {
      "description": "Go to https://dashboard.heroku.com/account, scroll down and press Reveal API.Required for updater to work.",
      "value": "",
      "required": true
    },
    "HEROKU_APP_NAME": {
      "description": "The Value of App Name you filled in right on top.Required for updater to work.",
      "value": "",
      "required": true
    },
    "TG_BOT_TOKEN_BF_HER": {
      "description": "Needed for inline buttons maker. Make a bot at [BotFather](http://telegram.dog/BotFather) and get the token of your bot. And Don't Forget To Turn on inline Mode on bot settings. Get it.",
      "value": ""
    },
    "CHROME_BIN": {
      "description": "For Carbon.py. Leave as it is. ",
      "value": "/app/.apt/usr/bin/google-chrome",
      "required": false
    },
    "CHROME_DRIVER": {
      "description": "For Carbon.py. Leave as it is. ",
      "value": "/app/.chromedriver/bin/chromedriver",
      "required": false
    },
    "TG_BOT_USER_NAME_BF_HER": {
      "description": "Needed for inline buttons maker. Make a bot at @BotFather and get the username of your bot",
      "value": ""
    },
    "OPEN_WEATHER_MAP_APPID": {
      "description": "Get your own APPID from https://api.openweathermap.org/data/2.5/weather",
      "required": false
    },
    "TZ": {
      "description": "Required for Correct Time for autopic get from http://www.timezoneconverter.com/cgi-bin/findzone.tzc",
      "value": "Asia/Kolkata",
      "required": false
    },
    "PM_DATA": {
      "description": "Type DISABLE if you want to disable pm protection... ",
      "value": "ENABLE",
      "required": false 
    }
  },
  "addons": [
    {
      "plan": "heroku-postgresql",
      "options": {
        "version": "12"
      }
    }
  ],
  "buildpacks": [
    {
      "url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest"
  },{
    "url":"https://github.com/amivin/aria2-heroku.git"
  },{
    "url":"https://github.com/heroku/heroku-buildpack-google-chrome"
  },{
     "url": "https://github.com/heroku/heroku-buildpack-apt.git"
  },{
    "url":"https://github.com/heroku/heroku-buildpack-chromedriver"
  },{
    "url": "https://github.com/opendoor-labs/heroku-buildpack-p7zip"
  },{
    "url": "heroku/python"
  }]
}
