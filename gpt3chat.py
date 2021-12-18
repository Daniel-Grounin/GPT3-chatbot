import openai
from tkinter import *

def gpt3(stext):
    openai.api_key = 'YOUR-API-KEY'
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=stext,
        temperature=0.1,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].text

def send():
    msg = Box.get("1.0",'end-1c').strip()
    Box.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n')

        res = gpt3(msg)
        ChatLog.insert(END, "AI: " + res + '\n')

        ChatLog.yview(END)

base = Tk()
base.geometry("900x550")
base.config(bg = "grey")
base.title("AI Chatbot")

startchatimage = PhotoImage(file='start.png')
buttons = Button(base, image=startchatimage, command=gpt3, borderwidth=0)
buttons.place(x=150, y=0)

#Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="150")
ChatLog.config(state=DISABLED)

#scrollbar
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

#Button to send message
Button = Button(base, font=("fantasy",20), text="SEND", width="7", height=5,  bd=0, bg="black", activebackground="grey",fg='#ffffff', command= send )

#Box to enter message
Box = Text(base, bd=0, bg="white",width="40", height="5")

#Components on the screen
scrollbar.place(x=790,y=50, height=386)
ChatLog.place(x=7,y=50, height=385, width=800)
Box.place(x=130, y=436, height=100, width=670)
Button.place(x=6, y=435, height=100)

base.mainloop()