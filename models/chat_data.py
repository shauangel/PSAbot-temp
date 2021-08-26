''' ======== CHAT_DATA_COLLECTION ======== *
- 新增資料 : insert_資料名稱
- 取得資料 : query_資料名稱
- 編輯資料 : update_資料名稱
- 刪除資料 : remove_資料名稱
- 資料名稱統一，以底線分隔，function前加上註解
- 使用collection : _db.CHAT_DATA_COLLECTION
* ========================================'''
# ====== our models ===== #
from . import _db
from . import user
import re
# ======================= #

def insert_chat(chat_dict):
    all_chat = _db.CHAT_DATA_COLLECTION.find()
    if all_chat.count() == 0 : 
        # 處理第一篇貼文編號
        chat_dict['_id'] = '000001'
    else:
        # sort post_id,將最大的+1當作新的post_id
        biggest_chat_id = int(all_chat.limit(1).sort('_id',-1)[0]['_id'])
        chat_dict['_id'] = str(biggest_chat_id + 1).zfill(6)
        
    _db.CHAT_DATA_COLLECTION.insert_one(chat_dict)
    return chat_dict['_id']
    