from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime, timedelta, date
import os
import pandas as pd

datetime_format = "%Y-%m-%d_%H-%M-%S"

transaction_types = ["routine", "temporary"]

rename_dct = {
    "transaction_type": "类型",
    "name_text": "名称",
    "period_slider": "周期",
    "crucial_slider": "重要程度",
    "remind_slider": "提醒周期",
    "progress_slider": "总进度",
    "remark_text": "备注",
    "limit_day_slider": "时限(天)",
    "limit_hour_slider": "时限(小时)"
}

property_seq = ["名称", "周期", "提醒周期", "重要程度", "进度", "剩余时间", "备注"]
seq_dct = {x: y for x, y in zip(property_seq, range(len(property_seq)))}

def get_current_time_str():
    d = str(datetime.today()).split(" ")[0]
    t = str(datetime.now().time())[:-7].replace(":", "-")
    return d + "_" + t

def arrange_dataframe_dict(dct):
    rnt = {}
    for k, v in dct.items():
        rnt[k] = [v[i] for i in range(len(v))]
    return rnt

def get_transaction_dct():
    for x in transaction_types:
        x = "Records/{}.xlsx".format(x)
        if not os.path.exists(x):
            pd.DataFrame().to_excel(x)
    routine_dct, temporary_dct = [arrange_dataframe_dict(pd.read_excel('Records/{}.xlsx'.format(x)).iloc[:, 1:].to_dict())
                                  for x in transaction_types]
    rnt = []
    for dct in [routine_dct, temporary_dct]:
        if dct:
            if dct == routine_dct:
                # -- 计算剩余时间
                dct["剩余时间"] = []
                for i, record_dt_string in enumerate(dct["记录时间"]):
                    record_dt = datetime.strptime(record_dt_string, datetime_format)
                    lmt_dt = record_dt + timedelta(days=(dct["当前进度"][i] + 1) * dct["周期"][i])
                    left_dt = lmt_dt - datetime.now()
                    left_days, left_hours, left_minutes = left_dt.days, left_dt.seconds // 3600, (left_dt.seconds // 60)%60
                    dct["剩余时间"].append("{}天{}小时{}分".format(left_days, left_hours, left_minutes))
                # --
                dct["进度"] = ["{}/{}".format(x, y) for x, y in zip(dct["当前进度"], dct["总进度"])]
                dct["周期"] = ["{}天".format(x) for x in dct["周期"]]
                del dct["当前进度"], dct["总进度"]
            else:
                # -- 计算剩余时间
                dct["剩余时间"] = []
                for i, record_dt_string in enumerate(dct["记录时间"]):
                    record_dt = datetime.strptime(record_dt_string, datetime_format)
                    lmt_dt = record_dt + timedelta(days=dct["时限(天)"][i], hours=dct["时限(小时)"][i])
                    left_dt = lmt_dt - datetime.now()
                    left_days, left_hours, left_minutes = left_dt.days, left_dt.seconds // 3600, (left_dt.seconds // 60)%60
                    dct["剩余时间"].append("{}天{}小时{}分".format(left_days, left_hours, left_minutes))
                # --
                del dct["时限(小时)"], dct["时限(天)"]
            del dct["类型"], dct["记录时间"]
            dct["提醒周期"] = ["{}天".format(x) for x in dct["提醒周期"]]
            # 整理顺序
            dct_seq = {}
            for k in sorted(dct.keys(), key=lambda x: seq_dct[x]):
                dct_seq[k] = dct[k]
            rnt.append(dct_seq)
    while len(rnt) < 2:
        rnt.append({})
    routine_dct, temporary_dct = rnt
    return routine_dct, temporary_dct

def get_transaction_dataframe(transaction_type):
    df = pd.read_excel('Records/{}.xlsx'.format(transaction_type))
    if len(df):
        df = df.iloc[:, 1:]
    return df

def tran_len(transaction):
    k = list(transaction.keys())[0]
    return len(transaction[k])

def generate_daily_report():
    routine_dct, temporary_dct = get_transaction_dct()

    pdf = canvas.Canvas("Records/Reports/dr_{}.pdf".format(date.today()))

    pdfmetrics.registerFont(TTFont('SimSun', 'simsun.ttc'))

    # 设置字体样式
    pdf.setFont('SimSun', 12)

    text_arr = []

    submit_record_file = "Records/Reports/submit_{}.txt".format(date.today())
    if os.path.exists(submit_record_file):
        f = open(submit_record_file, "r")
        text_arr += f.readlines()

    # 遍历日常事务，哪些事务于今天超时:
    for i in range(tran_len(routine_dct)):
        remain_time_str = routine_dct["剩余时间"][i]
        p1, p2 = remain_time_str.find("天"), remain_time_str.find("小时")
        day, hour = int(remain_time_str[:p1]), int(remain_time_str[p1+1:p2])
        hour += day * 24
        if hour < 5:
            text_arr.append("未完成的日常事务: {}".format(routine_dct["名称"][i]))

    # 遍历临时事务，哪些事务未完成:
    for i in range(tran_len(temporary_dct)):
        remain_time_str = temporary_dct["剩余时间"][i]
        p1, p2 = remain_time_str.find("天"), remain_time_str.find("小时")
        day, hour = int(remain_time_str[:p1]), int(remain_time_str[p1+1:p2])
        hour += day * 24
        if hour < 5:
            text_arr.append("未完成的临时事务: {}".format(temporary_dct["名称"][i]))

    for i, x in enumerate(text_arr):
        pdf.drawString(50, 800 - 20 * (i+1), x)
    pdf.save()


generate_daily_report()