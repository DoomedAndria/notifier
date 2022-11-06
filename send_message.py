from twilio.rest import Client


def send_message(message):
    account_sid = 'AC8310fb9cff2576cc49c5555f14ba362f'
    auth_token = '81542c8a1fddb58a022309707db02cc4'
    client = Client(account_sid, auth_token)

    client.messages.create(
        from_='whatsapp:+14155238886',
        body=message,
        to='whatsapp:+995591750895'
    )


def send_kutaisi(dates):
    message_kutaisi = 'ქუთაისი:\n\n'
    if len(dates) == 0:
        message_kutaisi += "საგამოცდო თარიღი ვერ მოიძებნა"
    else:
        for i in dates:
            message_kutaisi += i + "\n"
    send_message(message_kutaisi)


def send_sachkhere(dates):
    message_sachkhere = 'საჩხერე:\n\n'
    if len(dates) == 0:
        message_sachkhere += "საგამოცდო თარიღი ვერ მოიძებნა"
    else:
        for i in dates:
            message_sachkhere += i + "\n"
    send_message(message_sachkhere)
