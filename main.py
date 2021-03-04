import requests
import bs4
import random

from tkinter import *
import tkinter as tk
from tkinter import scrolledtext


window = Tk()
window.geometry("400x600")
window.title("vJudge Contest Creator")


global ans

number = StringVar()
srtdif = StringVar()
enddif = StringVar()



def Khela(n, srt, end,):
    setNum = int(n)

    tag = "" + str(srt) + "-" + str(end)

    link = 'https://codeforces.com/problemset/page/1?tags='+str(tag)

    res = requests.get(link)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    numPage = soup.find_all("span", "page-index")

    pages = int(numPage[-1].text.strip())

    List = []

    # Now we iterate over all the pages of the certain difficulty

    for i in range(1, pages + 1):
        link = 'https://codeforces.com/problemset/page/' + str(i) + '?tags='+str(tag)
        res = requests.get(link)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        x = soup.find_all("td", "id")
        for i in x:
            tmp = str(i.text.strip())
            List.append(tmp)

    # Now we have all the problems number in ArrayList


    # Now we scan our old problem set from a txt file so that it won't repeat

    file1 = open("OldProb.txt", "r")

    OldProblems = []

    OldProblems = file1.readlines()

    file1.close()

    # Old problems are stored

    # Now we find random problems which are not set before

    Final = []

    for i in range(setNum):
        rand = random.randint(0, len(List))
        tmp = List[rand]

        if tmp not in OldProblems:
            if tmp not in Final:
                gg = "" + str(List[rand]) + '\n'
                Final.append(gg)
            else:
                setNum + 1
        else:
            setNum + 1

    # Since we got the final set of questions now its time to store them in file

    file2 = open("Final_Problems.txt", "w")

    file2.writelines(Final)

    file2.close()

    # Storing new probs to oldprob file

    file3 = open("OldProb.txt", "a")

    file3.writelines(Final)

    file3.close()

    finalprobs = ""

    for i in Final:
        finalprobs+=i

    return finalprobs



def Start():

    n = number.get()
    srt = srtdif.get()
    end = enddif.get()



    ans = Khela(int(n),str(srt),str(end))

    my_text.delete(1.0,END)

    my_text.insert(tk.INSERT, ans)





label0 = Label(window, text="Problem Picker", fg="blue", font=("arial", 16, "bold")).place(x=120, y=20)


label0 = Label(window, text="Num of Problems: ",  font=("arial", 12, "bold")).place(x=5, y=80)
entry_num = Entry(window, textvar=number, font=("arial", 12))
entry_num.place(x=150, y=80)

label0 = Label(window, text="Start diff: ",  font=("arial", 12, "bold")).place(x=40, y=120)
entry_num = Entry(window, textvar=srtdif, font=("arial", 12))
entry_num.place(x=150, y=120)

label0 = Label(window, text="End diff: ",  font=("arial", 12, "bold")).place(x=45, y=160)
entry_num = Entry(window, textvar=enddif, font=("arial", 12))
entry_num.place(x=150, y=160)



my_text= Text(window, width=47, height=15)
my_text.place(x=10,y=300)

my_text.insert(tk.INSERT, 'www.facebook.com/dhr4fi')

button1 = Button(window,text="Start", font=("arial", 12, "bold"), command= Start).place(x=285,y=200)



label1 = Label(window, text="Created by Rafi", fg="red", font=("arial", 12, "italic")).place(x=140, y=550)

window.mainloop()

#GG