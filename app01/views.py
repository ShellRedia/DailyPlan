from django.shortcuts import render, HttpResponse, redirect
from func import *

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
    routine_dct, temporary_dct = get_transaction_dct()

    if request.method == "POST":
        if "back" in request.POST:
            return redirect("../main")
        elif "submit" in request.POST:
            form_dct = dict(request.POST)
            transaction_type = form_dct["transaction_type"][0]
            transaction_name = form_dct["name_text"][0]
            if transaction_type and transaction_name:
                df = get_transaction_dataframe(transaction_type)
                # 改项名:
                dct_t = {}
                for k, v in form_dct.items():
                    if k in rename_dct.keys():
                        dct_t[rename_dct[k]] = v
                form_dct = dct_t
                # -- 添加必要项，以供显示:
                if transaction_type == "routine":
                    form_dct["当前进度"] = 0
                form_dct["记录时间"] = get_current_time_str()

                new_record = pd.DataFrame(form_dct)
                df = pd.concat([df, new_record])

                transaction_filepath = 'Records/{}.xlsx'.format(transaction_type)
                df.to_excel(transaction_filepath)

                return redirect("../main")
    return render(request, 'create_transaction.html', dict(zip(transaction_types, [routine_dct, temporary_dct])))

def finish_transaction(request):
    routine_dct, temporary_dct = get_transaction_dct()

    if request.method == "POST":
        if "back" in request.POST:
            return redirect("../main")
        elif "submit" in request.POST:
            request_dct = dict(request.POST)
            transaction_type = request_dct["transaction_type"][0]
            selected_index = request_dct["selected_index"][0]
            finish_type = request_dct["finish_type"][0] 
            if selected_index.isdigit():
                si = int(selected_index)
                cond1 = transaction_type == "routine" and 0 <= si < tran_len(routine_dct)
                cond2 = transaction_type == "temporary" and 0 <= si < tran_len(temporary_dct)

                if cond1 or cond2:
                    df = get_transaction_dataframe(transaction_type)
                    submit_record_file = "Records/Reports/submit_{}.txt".format(date.today())
                    f = open(submit_record_file, "a")
                    select_trans_dct = {"routine":routine_dct, "temporary":temporary_dct}[transaction_type]
                    if finish_type == "current":
                        df["当前进度"][si] += 1
                        f.writelines(["打卡日常: {}, 进度: {}\n".format(select_trans_dct["名称"][si], select_trans_dct["进度"][si])])
                    else:
                        if finish_type == "finish":
                            f.writelines(["完成事务: {}\n".format(select_trans_dct["名称"][si])])
                        elif finish_type == "give_up":
                            f.writelines(["放弃事务: {}\n".format(select_trans_dct["名称"][si])])
                        df = df.drop(df.index[si])

                    transaction_filepath = 'Records/{}.xlsx'.format(transaction_type)
                    df.to_excel(transaction_filepath)

                return redirect("../main")
    return render(request, "finish_transaction.html", dict(zip(transaction_types, [routine_dct, temporary_dct])))
