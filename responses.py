from cgi import print_directory
import dont as q
from datetime import date, datetime
now = datetime.now()
date = now.strftime("date: %Y/%m/%d \n\n time: %H:%M:%S")
date_2 = now.strftime("%H:%M:%S")
def responses(text):
    text = str(text).lower()
    if text in ("تاریخ؟","تاریخ"):
        return date
    elif text in ("سلم","سلام"):
        return f"     سلام خوبی؟\n____________________________\n          {date_2}"
    elif text in ("اره","بله","ممنون","آره","مرسی","خوبم","خوب"):
        return f"     خدارو شکر \n____________________________\n          {date_2}"
    elif text in ("نه"):
        return f"     ای بابا😯😕\n____________________________\n          {date_2}"
    elif text in ("بیا بریم استخر"):
        return f"     کی بریم؟ \n____________________________\n         {date_2}"
    elif text in ("ماشین حساب"):
        return "     به زودی اضافه میشه \n____________________________\n         {date_2}"
    elif text in ("ربات میخوام"):
        return "     از این بگیر \n____________________________\n         @Alireza1385nazari \n____________________________\n         {date_2}"
    elif text in q.fohsh:
        return f"     جواب ابلهان خاموشیست \n____________________________\n          {date_2}"
    else:
        return f"     ___متوجه منظورتون نشدم! ___دستورات من محدوده \n____________________________\n          {date_2}"
# if "گاو" in q.fohsh:
#          print(f"     جواب ابلهان خاموشیست \n____________________________\n          {date_2}")
# input()