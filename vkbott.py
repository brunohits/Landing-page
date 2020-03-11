import vk_api
import random
import time
import json
import requests


token = "92edcf01775d99b9edd7eaf06f270f785465e9b5e83fb2fc144652109dd761ecf8d465db3ccb6ac346722"


vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    
    try:
        print('Бот запущен')

        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})

        if messages["count"] >= 1:

            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]


            if body == "привет" or body == "привет!"or body == "привет." or body == "Привет" or body == "Привет!"or body == "Привет.":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})


            elif body == "кто я?" or body == "Кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "Ты хороший человек", "random_id": random.randint(1, 2147483647)})


            elif body == ":з" or body == ":3":
                vk.method("messages.send", {"peer_id": id, "message": "*Мяв :з", "random_id": random.randint(1, 2147483647)})


            elif body == "hi" or body == "Hi" or body == "hi!" or body == "Hi!" or body == "Hello" or body == "hello" or body == "Hello!" or body == "Hello.":
                vk.method("messages.send", {"peer_id": id, "message": "Оу!!! Вы из Англии, а сразу-то и не скажешь!", "random_id": random.randint(1, 2147483647)})


            elif body == "Прует" or body == "Прует!" or body == "прует" or body == "прует!" or body == "прывет" or body == "Прывет" or body == "Прыувет" or body == "Привэт" or body == "привэт" or body == "прывет" or body == "прыувэт":
                vk.method("messages.send", {"peer_id": id, "message": "Дарова!!!", "random_id": random.randint(1, 2147483647)})


            elif body == "Хэй" or body == "Хай" or body == "хэй" or body == "хай" or body == "Хэй!" or body == "Хай!" or body == "хэй." or body == "хай.":
                vk.method("messages.send", {"peer_id": id, "message": "Хэй!", "random_id": random.randint(1, 2147483647)})


            elif body == "Ку" or body == "ку" or body == "Ку!" or body == "ку!" or body == "ку." or body == "Ку.":
                vk.method("messages.send", {"peer_id": id, "message": "Ку!", "random_id": random.randint(1, 2147483647)})


            elif body == "До свидания" or body == "до свидания" or body == "до свидания!" or body == "До свидания!" or body == "До свидания." or body == "до свидания":
                vk.method("messages.send", {"peer_id": id, "message": "До свидания!!! Ждем с нетерпением.", "random_id": random.randint(1, 2147483647)})


            elif body == "пока" or body == "Пока" or body == "Пока." or body == "Пока!" or body == "пока!" or body == "пока.":
                vk.method("messages.send", {"peer_id": id, "message": "Пока, возвращайся скорее", "random_id": random.randint(1, 2147483647)})


            elif body == "!тест":
                vk.method("messages.send", {"peer_id": id, "message": "Бот работает!", "random_id": random.randint(1, 2147483647)})


            elif body == "Как дела?" or body == "как дела?" or body == "как делишки?" or body == "Как делишки?" or body == "как дела" or body == "Как дела":
                vk.method("messages.send", {"peer_id": id, "message": "Не плохо, у вас?", "random_id": random.randint(1, 2147483647)})

            elif body == "У меня неплохо" or body == "Хорошо" or body == "Нормально":
                vk.method("messages.send", {"peer_id": id, "message": "Это прекрастно и у меня", "random_id": random.randint(1, 2147483647)})


            elif body == "У меня плохо" or body == "Не очень" or body == "Ужастно":
                vk.method("messages.send", {"peer_id": id, "message": "Оу, зайчик, почему? Не грусти :з Мы любим тебя ", "random_id": random.randint(1, 2147483647)})

            elif body == "Даже не знаю почему" or body == "Просто так" or body == "Не знаю":
                vk.method("messages.send", {"peer_id": id, "message": "Все будет хорошо, солнышко, улыбнись! ", "random_id": random.randint(1, 2147483647)})
                

            elif body == "!команды":
                vk.method("messages.send", {"peer_id": id, "message": "Список команд:\nАниме-тян\nГифка\nКотики", "random_id": random.randint(1, 2147483647)})

            elif body == "тян" or body == "Тян" or body == "Фото" or body == "Аниме-тян" or body == "Тяночку":
                vk.method("messages.send", {"peer_id": id, "message": "Тян", "attachment": "photo-192537437_457239018", "random_id": 0})


            else:
                vk.method("messages.send", {"peer_id": id, "message": "Я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)


