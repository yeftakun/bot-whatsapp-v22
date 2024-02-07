import telebot
import requests
import time

"""
jalan pke mp2 di file ecosystem2.config.js
"""
#import mysql.connector

# konfigurasi ---> ubah token dan pass kalian
bot = telebot.TeleBot('token')
mypass = "pass anda"
# endpoint
api_start = "https://xxxxx.execute-api.ap-southeast-1.amazonaws.com/default/ec2startNew"
api_stop = "https://yyyyyy.execute-api.ap-southeast-1.amazonaws.com/default/ec2stopNew"

#Fungsi Start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    response = "Selamat datang di bot ini..\nℹ️/botinfo\n📜/credit\nSwitch:\t/serveron | /serveroff\n masukan password setelah menjalankan perintah."
    bot.reply_to(message, response)

# Fungsi untuk menampilkan informasi tentang bot
@bot.message_handler(commands=['botinfo'])
def show_botinfo(message):
    bot.reply_to(message, "Ini adalah bot untuk start/stop instance ec2\n")

# Fungsi untuk memberikan kredit kepada pembuat bot
@bot.message_handler(commands=['credit'])
def show_credit(message):
    bot.reply_to(message, "📜Membuat bot : https://youtu.be/sEq6k6UEUGM")
#≠================≠=
# Fungsi untuk start isinstance
@bot.message_handler(commands=['serveron'])
def request_password_forstart(message):
    bot.reply_to(message, "Masukkan password:")
    bot.register_next_step_handler(message, check_password_forstart)
# Fungsi untuk memeriksa password yang dimasukkan
def check_password_forstart(message):
    if message.text == mypass:
        response = requests.get(api_start)
        bot.reply_to(message, response.text)
        bot.reply_to(message, "Bot wa.me/6285775471308 sekarang berjalan")
    else:
        bot.reply_to(message, "Password salah. Masukan kembali command.")
#===============================
# Stop instance
@bot.message_handler(commands=['serveroff'])
def request_password_forstop(message):
    bot.reply_to(message, "Masukkan password:")
    bot.register_next_step_handler(message, check_password_forstop)
# Fungsi untuk memeriksa password yang dimasukkan
def check_password_forstop(message):
    if message.text == mypass:
        response = requests.get(api_stop)
        bot.reply_to(message, response.text)
        bot.reply_to(message, "Bot WA berhenti")
    else:
        bot.reply_to(message, "Password salah. Masukan kembali command.")
#===============================
"""
def stoping_server(message):
    response = requests.get("https://t4cylwsagc.execute-api.ap-southeast-1.amazonaws.com/default/ec2stopNew")
    bot.reply_to(message, response.text)
"""

@bot.message_handler(func=lambda message: True)
def handle_unknown_command(message):
    bot.reply_to(message, "Maaf, perintah salah. Silakan kirim lagi perintah yang valid, atau klik /start untuk lanjut.\n\nhttps://media.giphy.com/media/a6pzK009rlCak/giphy.gif")

bot.polling()