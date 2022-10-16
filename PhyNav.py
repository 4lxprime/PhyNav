from tkinter import *
from tkinterweb import *
import requests
import time
import threading

pages=[]
n=[]
ong_del=[]

def stop():
    root.destroy()
    exit(0)

def gets(url, name):
    headers = {
    'User-Agent': 'PhySearch 1.0',
    'From': 'idalxprime@gmail.com',
    'Cookie':'CONSENT=YES+cb.20210418-17-p0.it+FX+917; '
}
    htmlFR.load_html(f"<div style='background: white; color: #23272e; text-align: center;'><br><h1>Waiting</h1><br><p>for <a href='{url}'>{url}</a></p></div>")
    try:
        r=requests.get(url, headers=headers)
        if r.status_code==200:
            htmlFR.load_website(url)
        else:
            htmlFR.load_html(f"<div style='background: white; color: #23272e; text-align: center;'><br><h1>Error {r.status_code}</h1></div>")
    except Exception as e:
        htmlFR.load_html(f"<div style='background: white; color: #23272e; text-align: center;'><br><h1>Error: {e}</h1></div>")

def search(x):
    url=urle.get()
    if url!="" and "http" in url:
        print(url)
        threading.Thread(target=gets, args=(url, url.replace("https://", ""))).start()
    elif not "http" in url:
        if "." in url:
            url=f"https://{url}"
            threading.Thread(target=gets, args=(url, url.replace("https://", ""))).start()
        else:
            if " " in url:
                url.replace(" ", "%20")
            url=f"https://www.google.com/search?q={url}"
            threading.Thread(target=gets, args=(url, url.replace("https://www.google.com/search?q=", "").replace("%20", " "))).start()
    else:
        root.update()
        print(canvas.winfo_width()-1)

root=Tk()

root.geometry("800x500")
root.minsize(600, 300)
root.title(f"  PhySearch 1.0  |  {time.asctime(time.localtime())}")

def act_title():
    while 1:
        root.title(f"  PhySearch 1.0  |  {time.asctime(time.localtime())}")
        time.sleep(1)

ttl=threading.Thread(target=act_title)
ttl.setDaemon(True)
ttl.start()

canvas=Canvas(root, bg="#23272e", width=800, height=500)

canvas.create_rectangle(0, 0, root.maxsize()[0], 80, outline="black", fill="#1c1c1c")

root.update()

urle=Entry(root, font=("Arial", 20), relief="flat", borderwidth=0, bg="#1e2227", width=38, highlightthickness=1, highlightbackground='black', fg="white")
UrlInput=canvas.create_window(root.winfo_width()/2 , 40, window=urle)

htmlFR=HtmlFrame(root)
htmlFR.load_website("https://google.com")
HPage=canvas.create_window(2, 80, anchor="nw", window=htmlFR, width=root.winfo_width()-5, height=root.winfo_height()-82)

def butt_press(x):
    print(x)
    for i in pages:
        if i==f"|ok|{x}":
            url=x
            print(url)
            if url!="" and "http" in url:
                print(url)
                threading.Thread(target=gets, args=(url, url.replace("https://", ""))).start()
            elif not "http" in url:
                if "." in url:
                    url=f"https://{url}"
                    threading.Thread(target=gets, args=(url, url.replace("https://", ""))).start()
                else:
                    if " " in url:
                        url.replace(" ", "%20")
                    url=f"https://www.google.com/search?q={url}"
                    threading.Thread(target=gets, args=(url, url.replace("https://www.google.com/search?q=", "").replace("%20", " "))).start()
            else:
                root.update()
                print(canvas.winfo_width()-1)

def ong_save():
    while 1:
        if len(ong_del)!=0:
            for i in pages:
                if i.startswith("|ok|"):
                    i=i.replace("|ok|", "")
                    if canvas.coords(globals()[f'ongl'+i])[0]==2:
                        canvas.coords(globals()[f'ongl'+i], canvas.coords(globals()[f'ongl'+i])[0], root.winfo_height()-41)
                        canvas.coords(globals()[f'onglcrx'+i], canvas.coords(globals()[f'onglcrx'+i])[0], root.winfo_height()-41)
                    else:
                        canvas.coords(globals()[f'ongl'+i], canvas.coords(globals()[f'ongl'+i])[0]-172, root.winfo_height()-41)
                        canvas.coords(globals()[f'onglcrx'+i], canvas.coords(globals()[f'onglcrx'+i])[0]-172, root.winfo_height()-41)
            ong_del.remove("x")
        else:
            for i in pages:
                if i.startswith("|ok|"):
                    i=i.replace("|ok|", "")
                    canvas.coords(globals()[f'ongl'+i], canvas.coords(globals()[f'ongl'+i])[0], root.winfo_height()-41)
                    canvas.coords(globals()[f'onglcrx'+i], canvas.coords(globals()[f'onglcrx'+i])[0], root.winfo_height()-41)
        time.sleep(0.1)

t=threading.Thread(target=ong_save)
t.setDaemon(True)
t.start()

def ong_kill(ong):
    for i in pages:
        if i==f"|ok|{ong}":
            pages.remove(i)
            canvas.delete(globals()[f'ongl'+ong])
            canvas.delete(globals()[f'onglcrx'+ong])
            n.remove("x")
            ong_del.append("x")

def ong():
    while 1:
        for i in pages:
            if i.startswith("|ok|"):
                pass
            else:
                brk=[]
                for t in pages:
                    if f"|ok|{i}"==t:
                        pages.remove(i)
                        brk.append(True)
                        print("bad")
                    else:
                        print("ok")
                        pass
                if brk:
                    break
                else:
                    pass
                x=172*len(n)
                print(i)
                globals()[f'ong'+i]=Button(root, text=i, font=("Arial", 15), bg="#1c1c1c", fg="white", command=lambda m=f"{i}": butt_press(m), width=15, height=1, relief="flat", borderwidth=0)
                globals()[f'ongl'+i]=canvas.create_window(2+x, root.winfo_height()-42, anchor="nw", window=globals()[f'ong'+i])

                globals()[f'ongcrx'+i]=Button(root, text="X", font=("Arial", 15), bg="#1c1c1c", command=lambda m=f"{i}": ong_kill(m), width=3, height=1, relief="flat", borderwidth=0, fg="white")
                globals()[f'onglcrx'+i]=canvas.create_window(134+x, root.winfo_height()-42, anchor="nw", window=globals()[f'ongcrx'+i])
                # globals()[f'ongl'+i]=canvas.create_rectangle(2+x, root.winfo_height()-43, 172+x, root.winfo_height(), outline="black", fill="#1c1c1c")
                # globals()[f'onglT'+i]=canvas.create_text(80+x, root.winfo_height()-22, text=i, font=("Arial", 15), width=210, fill="white")
                pages.remove(i)
                pages.append(f"|ok|{i}")
                n.append("x")
        time.sleep(0.5)

t=threading.Thread(target=ong)
t.setDaemon(True)
t.start()

def act():
    while 1:
        root.update()
        canvas.itemconfigure(HPage, width=root.winfo_width()-5, height=root.winfo_height()-122)
        canvas.coords(UrlInput, root.winfo_width()/2, 40)
        
    
t=threading.Thread(target=act)
t.setDaemon(True)
t.start()

root.bind('<Return>', search)
canvas.pack(expand=True, fill="both")
root.protocol("WM_DELETE_WINDOW", stop)
root.mainloop()