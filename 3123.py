import datetime
    
def doScrollDown(whileSeconds):
        start = datetime.datetime.now(60)
        end = start + datetime.timedelta(seconds=whileSeconds)
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(1)
            if datetime.datetime.now(60) > end:
                break
