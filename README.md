# PhyNav

an 100% python navigator with a tab system


## GUI

I use [tkinter](https://docs.python.org/fr/3/library/tkinter.html) for the gui interface.

```python
root=Tk()

root.geometry("800x500")
root.minsize(600, 300)
root.title(f"  PhySearch 1.0  |  {time.asctime(time.localtime())}")

root.bind('<Return>', search)
canvas.pack(expand=True, fill="both")
root.protocol("WM_DELETE_WINDOW", stop)
root.mainloop()
```

## How it work ?

I can display the html with [tkinterweb](https://github.com/Andereoo/TkinterWeb) and I use [bs4](https://github.com/wention/BeautifulSoup4) for delete script

That is the code that I use for get the html and display it:

```python
def gets(url, name):
    headers = {
    'User-Agent': 'PhySearch 1.0',
    'From': 'idalxprime@gmail.com',
    'Cookie':'CONSENT=YES+cb.20210418-17-p0.it+FX+917; '
}
    canvas.itemconfigure(HPage, window=HTMLLabel(root, html="<div style='background: #23272e; color: white; text-align: center;'><br><h1>Waiting ...</h1></div>", background="#1e2227", highlightthickness=1, highlightbackground='black'))
    try:
        r=requests.get(url, headers=headers)
        if r.status_code==200:
            soup=BeautifulSoup(r.content, "html.parser")
            for data in soup(['script']):
                data.decompose()
            r= ' '.join(soup.stripped_strings)
            print(r)
            canvas.itemconfigure(HPage, window=HTMLLabel(root, html=f"<div style='background: #23272e; color: white;'>{r}</div>", background="#1e2227", highlightthickness=1, highlightbackground='black'))
            pages.append(name)
        else:
            canvas.itemconfigure(HPage, window=HTMLLabel(root, html=f"<div style='background: #23272e; color: white; text-align: center;'><br><h1>Error {r.status_code}</h1></div>", background="#1e2227", highlightthickness=1, highlightbackground='black'))
    except Exception as e:
        canvas.itemconfigure(HPage, window=HTMLLabel(root, html=f"<div style='background: #23272e; color: white; text-align: center;'><br><h1>Error: {e}</h1></div>", background="#1e2227", highlightthickness=1, highlightbackground='black'))

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
```