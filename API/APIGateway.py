#!/usr/bin/env python
#coding: utf8 

from flask import jsonify,request, Flask
import os
import datetime
import json

def Auth(deviceId):
    return True

def ProfileListFollowers(userId):
    return jsonify({"success":1,"response":"running api"}) 

def ProfileListFollows(userId):
    return jsonify({"success":1,"response":"running api"}) 


