"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

def get_most_active_user(messages):
    user_message_count = {}

    for message in messages:
        user_id = message["sent_by"]
        if user_id in user_message_count:
            user_message_count += 1
        else:
            user_message_count = 1
    most_active_user = max(user_message_count, key=user_message_count.get)
    return most_active_user

def get_most_replied_user(messages):
    reply_count = {}

    for message in messages:
        if message["reply_for"] is not None:
            original_message_id = message["reply_for"]
            for msg in messages:
                if msg["id"] == original_message_id:
                    user_id = msg["sent_by"]
                    if user_id in reply_count:
                        reply_count[user_id] += 1
                    else:
                        reply_count[user_id] = 1

    most_replied_user = max(reply_count, key=reply_count.get)
    return most_replied_user
            
def get_most_seen_user(messages):
    seen_by_count = {}

    for message in messages:
        user_id = message["sent_by"]
        unique_seen_by = len(set(message["seen_by"]))
        if user_id in seen_by_count:
            seen_by_count[user_id] += unique_seen_by
        else:
            seen_by_count[user_id] = unique_seen_by

    most_seen_user = max(seen_by_count, key=seen_by_count.get)
    return most_seen_user


def get_most_active_period(messages):
    morning_count = 0
    afternoon_count = 0
    evening_count = 0

    for message in messages:
        hour = message["sent_at"].hour
        if hour < 12:
            morning_count += 1
        elif 12 <= hour < 18:
            afternoon_count += 1
        else:
            evening_count += 1

    if morning_count > afternoon_count and morning_count > evening_count:
        return "Утро"
    elif afternoon_count > evening_count:
        return "День"
    else:
        return "Вечер"



    print("Пользователь, который написал больше всех сообщений:", get_most_active_user(messages))
    print("Пользователь, на сообщения которого больше всего отвечали:", get_most_replied_user(messages))
    print("Пользователь, сообщения которого видело больше всего уникальных пользователей:", get_most_seen_user(messages))
    print("Больше всего сообщений было:", get_most_active_period(messages))




if __name__ == "__main__":
    print(generate_chat_history())
