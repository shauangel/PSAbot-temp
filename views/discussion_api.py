#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:00:01 2021

@author: linxiangling
"""
from datetime import datetime
import requests 
import json
import flask
from flask import request, Blueprint, jsonify
from models import user,chat_data

discussion_api=Blueprint('discussion_api', __name__)

#head_url='http://localhost:55001/api/'
head_url='https://soselab.asuscomm.com:55002/api/'

#共同討論推薦user
@discussion_api.route('discussion_recommand_user', methods=['POST'])
def discussion_recommand_user():
    first_level = requests.get(head_url + 'query_all_languages')
    
    data = request.get_json()
    tags = data['tags']
    #初步篩選
    users = user.query_skill_discussion_initial_filter(tags)
    #加權
    for i in users:
        sort_scores = 0
        for j in i['skill']:
            if j in first_level:
                sort_scores += (j['interested_score']+j['score']) * 1
            else:
                sort_scores += (j['interested_score']+j['score']) * 3
        i.update({'sort_scores':sort_scores})
    #排序
    sorted_users = sorted(users, key=lambda k: k['sort_scores'], reverse=True)
    stage1_id_array = [i['_id'] for i in sorted_users]
    #print("stage1_id_array ", stage1_id_array)
    #print('sorted_users ', sorted_users)
    #不足十人，找更多人推薦
    if len(users) < 10:
        lacking_num = 10 - len(users)
        stage2_id_array = user.query_skill_discussion_scores_only(stage1_id_array, tags, lacking_num)
        #print("stage2_id_array ", stage2_id_array)
        stage1_id_array.extend(stage2_id_array)
    else:
        stage1_id_array = stage1_id_array[0:10]
    return jsonify({"recommand_user_id":stage1_id_array})
    

# 詢問機器人建立聊天室
@discussion_api.route('create_psabot_chat', methods=['POST'])
def create_psabot_chat():
    data = request.get_json()
    chat_dict = {
        '_id':'',
        'tags': [],
        'keywords': data['keywords'],
        'question': data['question'],
        'time':datetime.now().replace(microsecond=0),
        'members': 
        [
            {
            'user_id':data['asker']['user_id'],
            'user_name':data['asker']['user_name'],
            'incognito':data['asker']['incognito']
            }
        ],
        'chat_logs':[],
        'end_flag':False
    }
    room_id = chat_data.insert_chat(chat_dict)
    return jsonify({"_id":room_id})
# 詢問機器人儲存聊天訊息
@discussion_api.route('insert_psabot_chat_log', methods=['POST'])
def insert_psabot_chat_log():
    data = request.get_json()
    chat_dict = {
        '_id':data['_id'],
        'user_id':data['user_id'],
        'time':datetime.now().replace(microsecond=0),
        'type':data['type'],
        'content':data['type']
    }
    chat_data.insert_message(data)
    return jsonify(chat_dict)