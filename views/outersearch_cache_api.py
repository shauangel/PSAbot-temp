#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:06:08 2021

@author: shauangel
"""
# --- flask --- #
from flask import Blueprint, request, jsonify

# --- our models ---- #
from models import outer_data_cache

outersearch_cache_api = Blueprint('outersearch_cache_api', __name__)

#獲取摘要資訊
@outersearch_cache_api.route('/query_cache_by_id', methods=['POST'])
def query_cache_by_id():
    idx = request.get_json()
    try:
        result = outer_data_cache.query_by_id(idx)
        # 慈測試 START
        print("HTTP POST - query_cache_by_id的輸入: ")
        print(idx)
        print("query_cache_by_id的輸出: ")
        print(jsonify(result))
        # 慈測試 END
        return jsonify(result)
        
    except Exception as e :
        setting_dict = {"error" : e.__class__.__name__ + ":" + str(e.args[0])}
        print("錯誤訊息: ", e)
    return jsonify(setting_dict)

#新增快取資料
@outersearch_cache_api.route('/insert_cache', methods=['POST'])
def insert_cache():
    data = request.get_json()
    try:
        result = outer_data_cache.insert_cache(data['data'], data['type'])
        # 慈測試 START
        print("HTTP POST - insert_cache的輸入: ")
        print(data)
        print("insert_cache的輸出: ")
        print(jsonify(result))
        # 慈測試 END
        return jsonify(result)
    except Exception as e :
        setting_dict = {"error" : e.__class__.__name__ + ":" + str(e.args[0])}
        print("錯誤訊息: ", e)
    return jsonify(setting_dict)

#更新點讚情況
@outersearch_cache_api.route('/update_cache_score', methods=['POST'])
def update_cache_score():
    data = request.get_json()
    try:
        outer_data_cache.update_cache_score(data)
        # 慈測試 START
        print("HTTP POST - update_cache_score的輸入: ")
        print(data)
        print("update_cache_score的輸出: ")
        print(jsonify("success"))
        # 慈測試 END
        return jsonify("success")
    except Exception as e :
        setting_dict = {"error" : e.__class__.__name__ + ":" + str(e.args[0])}
        print("錯誤訊息: ", e)
    return jsonify(setting_dict)
