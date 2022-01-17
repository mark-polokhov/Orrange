import main_db_client

# ID = 0
# Name = "Побег из Шоу Хэнка"
# Type = "Кино"
# Date = "[21,12,2021]"
# Time = "[19,00]"
# Price = "300"
# Address = "Школьный пр., д. 6, Одинцово"
# Coordinates = "[0, 0]"
# IsOpen = "Yes"
# About = "Ждём всех желающих хорошо провести время!"
# Conditions = ""

ID = 0
Name = "Wellcome to the club"
Type = "Учёба"
Date = "[16,12,2021]"
Time = "[9,00]"
Price = "0"
Address = "Покровский бул., 11, стр. 10, Москва"
Coordinates = "[0, 0]"
IsOpen = "Yes"
About = "This english club is the opportunity for you and your friends to improve your English skills. We'll be talking about weather, football, will repeat some grammatical rules"
Conditions = "Intermediate or higher"


# ID = 0
# Name = "Заглушка"
# Type = "Заглушка"
# Date = "Заглушка"
# Time = "Заглушка"
# Price = "Заглушка"
# Address = "Заглушка"
# Coordinates = "Заглушка"
# IsOpen = "Заглушка"
# About = "Заглушка"
# Conditions = "Заглушка"


main_db_client.insert_data(Name, Type, Date, Time, Price, Address, Coordinates, IsOpen, About, Conditions)

print([record for record in main_db_client.view_records()])
