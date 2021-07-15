import telegram

def bot(type='p', message = 'None'):

    botter = telegram.Bot('1334671210:AAG9Cfvt8PYb0meZxgH7KKWzNHcVtqTKzts')
    botter.send_message('@news1_private_test',message)
