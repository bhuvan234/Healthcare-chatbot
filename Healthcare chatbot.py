from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer #import os


try:

os.remove("db.sqlite3")

print("Old database removed. Training new database")

except:

print('No database found. Creating new database.')



english_bot = ChatBot('Bot') trainer=ListTrainer(english_bot) trainer.train(conv) trainer.train(conv1) trainer.train(conv2) trainer.train(conv3)





from chatterbot import ChatBot from tkinter import *
i=0
 
def ptr():

global i f=e.get()
w=Label(r,text="You: "+e.get(),bg='lightgreen').grid(row=i,column=2) i+=1
t=english_bot.get_response(f) ans=str(t)
w=Label(r,text="Bot: "+ans,bg='white').grid(row=i,column=0) e.delete(0,END)
i+=1

r=Tk() r.title('chatbot')
r.geometry("480x550") e=Entry(r) e.grid(row=20,column=1)
b=Button(r,text="Send",width=10,command=ptr) b.grid(row=20,column=2)
i=i+1 mainloop()
 


