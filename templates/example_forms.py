"""feel free to replace and change these around."""

StartingParams = {
    "AList" : {
    "title":"List of Str",
    "type":"str",
    "enum":["boring default","choose me!", "or  me..", 
            "I will break everything"],
    "value":"boring default"
    },
    "SomeNumbers":{
        "title":"Some Numbers",
    "type":"float",
    "minimum":0,
    "maximum":10,
    "valstep":2,
    "value":6
    },
    "BoolChoice":{
        "title":"Boolean option",
    "type":"bool",
    "value":"False"
    }

}

