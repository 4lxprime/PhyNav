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

I can display the html with [tkinterweb](https://github.com/Andereoo/TkinterWeb)

That is the code that I use for get the html and display it:

```python
def gets(url, name):
    headers = {
    'User-Agent': 'PhySearch 1.0',
    'From': 'idalxprime@gmail.com',
    'Cookie':'CONSENT=YES+cb.20210418-17-p0.it+FX+917; '
}
    htmlFR.load_html(f"<div style='background: white; color: #23272e; text-align: center;'><br><h1>Waiting</h1><br><p>for <a href='{url}'>{url}</a></p></div>")
    pages.append(name)
    try:
        r=requests.get(url, headers=headers)
        if r.status_code==200:
            htmlFR.load_website(url, force=True)
            while actual_page!=[]:
                for i in actual_page:
                    actual_page.remove(i)
            actual_page.append(name)
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
```
