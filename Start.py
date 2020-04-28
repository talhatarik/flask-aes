#!/usr/bin/env python
#coding: utf8 

from flask import jsonify,request, Flask
import os
import datetime
import json

from API.APIGateway import ProfileListFollowers,ProfileListFollows,Auth
from AES.AES import getKeyGenerator,getDecode


app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route('/',methods=['POST'])
def Api():
    apiEncodeRequest =request.values.get("api")

    parseApiRequest = getDecode(apiEncodeRequest).split("&")

    #Auth Success
    if Auth(parseApiRequest[1]) == True:

        #API Router
        if parseApiRequest[0].lstrip(" ") == "ProfileListFollowers":
            return ProfileListFollowers(parseApiRequest[2])

        elif parseApiRequest[0] == "ProfileListFollows":
            return ProfileListFollows(parseApiRequest[2])

    
    #Auth Not Success
    else:
        return jsonify({"success":0,"response":"Auth Error"})



if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=port)


