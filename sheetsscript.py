import gspread




def create_info_google_sheets(user_data:dict,user_id:int):
    
    

    gc = gspread.service_account(filename='creds.json')

    # Open a sheet from a spreadsheet in one go
    wks = gc.open("taskssheet1").sheet1
    row =[
    f"t.me/{user_data[user_id]['username']}",                        # Страница в Телеграм (ID пользователя)
        user_data[user_id]['name'],      # Имя
        user_data[user_id]['surname'],   # Фамилия
        user_data[user_id]['company'],   # Компания
        user_data[user_id]['phone'], 
        user_data[user_id]['time']
        ]
    
    # Добавление строки в конец таблицы
    wks.append_row(row, value_input_option="USER_ENTERED")
    print("Данные успешно добавлены!")
    

# create_info_google_sheets(user_data=user_data,user_id=list(user_data.keys())[0])