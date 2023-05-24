from django.shortcuts import render, HttpResponse, redirect
import pandas as pd
from datetime import datetime
import os

def get_current_time_str():
    d = str(datetime.today()).split(" ")[0]
    t = str(datetime.now().time())[:-7].replace(":", "-")
    return d + "_" + t

rename_dct = {
    "transaction_type": "type",
    "name_text": "name",
    "period_slider": "period",
    "crucial_slider": "crucial",
    "remind_slider": "remind_interval",
    "progress_slider": "progress_total",
    "remark_text": "remark"
}

# Create your views here.
def main(request):
    if request.method == "POST":
        if "create_transaction" in request.POST:
            return redirect("../create_transaction")
        elif "finish_transaction" in request.POST:
            return redirect("../finish_transaction")
    return render(request, "main.html")


# 处理.html所访问的函数:
def create_transaction(request):
    if request.method == "POST":
        if "back" in request.POST:
            return redirect("../main")
        elif "submit" in request.POST:
            form_dct = dict(request.POST)
            if form_dct["transaction_type"] and form_dct["name_text"][0]:
                transaction_filepath = 'Records/{}.xlsx'.format(form_dct["transaction_type"][0])
                if not os.path.exists(transaction_filepath):
                    pd.DataFrame().to_excel(transaction_filepath)
                df = pd.read_excel(transaction_filepath)
                # -- 添加必要项，以供显示
                dct_t = {}
                for k, v in form_dct.items():
                    if k in rename_dct.keys():
                        dct_t[rename_dct[k]] = v
                form_dct = dct_t

                form_dct["time"] = get_current_time_str()
                # --
                new_item = pd.DataFrame(form_dct)
                df = pd.concat([df, new_item], axis=0)
                print(df)
                df.to_excel(transaction_filepath)
    return render(request, 'create_transaction.html')

def finish_transaction(request):
    if request.method == "POST":
        if "back" in request.POST:
            return redirect("../main")
    return render(request, "finish_transaction.html")
