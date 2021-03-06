import PySimpleGUI as sg
import twitterBot as bot
import database as db

sg.theme('Dark Blue 3')

tweet_list = db.getTweets()

layout = [[sg.Text('Enter a tweet to send'), sg.Text(size=(12,1))],
          [sg.Input(key='-IN-')],
          [sg.Button('Tweet'), sg.Button('Delete'), sg.Button('Refresh'), sg.Button('Exit')],
          [sg.Text(key='-OUTPUT-')],
          [sg.Text(text=tweet_list, key='-TWEET-')]]

window = sg.Window('Tweet Bot', layout)

while True:  # Event Loop
    event, values = window.read()
    
    
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Tweet':
        tweet = values['-IN-']
        tweet_id, message = bot.create_tweet(tweet)
        window['-OUTPUT-'].update(message)
        tweet_list = db.getTweets()
        window['-TWEET-'].update(tweet_list)
    if event == 'Delete':
        tweet = values['-IN-']
        message = bot.delete_tweet(tweet)
        window['-OUTPUT-'].update(message)
        tweet_list = db.getTweets()
        window['-TWEET-'].update(tweet_list)
    if event == 'Refresh':
        tweet_list = db.getTweets()
        window['-TWEET-'].update(tweet_list)

window.close()
