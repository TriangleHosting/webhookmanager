import webview

def main():
    window = webview.create_window('WebHook Manager', 'index.html', width=1920, height=1080)
    window.title_bar_icon = 'favicon.ico'
    webview.start()

if __name__ == '__main__':
    main()