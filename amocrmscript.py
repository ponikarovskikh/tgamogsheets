from amocrm.v2 import tokens,Lead,Task,Call,Company,Contact
import time
from datetime import datetime
from datetime import datetime, timedelta
import tokens as tok
def create_task_crm(userdata,user_id):
    tokens.default_token_manager(
    client_id="b7f9d59c-9a90-4eef-a920-fab2ed58679b",
    client_secret="KM0NyV9NYGejXbuv9SRj5AfSkpZellXXvYPdumYhLEvT8p0B0LKvroRtSBQTfBv6",
    subdomain="d4321234",
    redirect_url="https://ya.ru",
    storage=tokens.FileTokensStorage(), 
        )   

    from datetime import datetime, timedelta

    # Получаем текущее время
    current_time = datetime.now()
    print(time.time())
    print(current_time)
    # Добавляем 1 час к текущему времени
    time_plus_one_hour = current_time + timedelta(hours=1)

    # Преобразуем в Unix timestamp
    unix_timestamp = int(time_plus_one_hour.timestamp())
    
    #Task.objects.create(name="Заявка",text=f"<b>Заявка на банкротство</b>\nТелефон:{userdata[user_id]['phone']}\n{userdata[user_id]['surname']} {userdata[user_id]['name']}\nОрганизация: {userdata[user_id]['company']}\nТелеграм: https://t.me/{userdata[user_id]['username']}",complete_till=(unix_timestamp),created_at=int(time.time()))
    Task.objects.create(name="Заявка",text=f"ww",complete_till=(unix_timestamp),created_at=int(datetime.now().timestamp()))


