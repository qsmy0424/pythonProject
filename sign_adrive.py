import requests
import calendar
from datetime import date
import schedule
import time

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_message_to_email(msg):
    """使用第三方 SMTP 服务发送邮件"""
    # 第三方 SMTP 服务
    # 用哪个第三方的 SMTP 更换为 哪个第三方的SMTP 的host、user、pass
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "qsmy0424@163.com"  # 用户名
    mail_pass = "ISVEQTTBYISFICBV"  # 口令

    sender = 'qsmy0424@163.com'
    receivers = ['qsmy0424@outlook.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header("qsmy0424@outlook.com", 'utf-8')

    subject = '阿里云盘签到'
    message['Subject'] = Header(subject, 'utf-8')
    # 使用 465 接口必须使用 SMTP_SSL
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    try:
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())

    except smtplib.SMTPException as e:
        print(e)
    finally:
        smtpObj.quit()


def aliyun_dirve_get_access_token(refresh_token):
    # 刷新token获取access_token
    res = requests.post("https://auth.aliyundrive.com/v2/account/token",
                        json={
                            "grant_type": "refresh_token",
                            "refresh_token": refresh_token
                        })
    res = res.json()

    return res.get('access_token')


def aliyun_drive_sign_in():
    """签到"""
    for refresh_token in refresh_tokens:
        if refresh_token != "":
            # 刷新token获取access_token
            access_token = aliyun_dirve_get_access_token(refresh_token)

            if access_token is None:
                send_message_to_email("refresh_token错误，请重新填写refresh_token")
            else:
                try:
                    # 进行签到
                    res2 = requests.post("https://member.aliyundrive.com/v1/activity/sign_in_list",
                                         json={"_rx-s": "mobile"},
                                         headers={"Authorization": 'Bearer ' + access_token})
                    res2 = res2.json()
                    signInCount = res2.get('result', {}).get('signInCount', 0)
                    send_message_to_email(f"{date.today()} 今日签到成功!")
                except:
                    send_message_to_email(f"{date.today()} 今日签到失败!")


def aliyun_drive_get_sign_award(sign_day):
    """领取签到奖励"""
    # global MG
    for refresh_token in refresh_tokens:
        if refresh_token != "":
            # 获取 access_token
            access_token = aliyun_dirve_get_access_token(refresh_token)

            if access_token is None:
                send_message_to_email()
            else:
                global mg
                try:
                    # 进行领取奖励
                    res3 = requests.post("https://member.aliyundrive.com/v1/activity/sign_in_reward?_rx-s=mobile",
                                         json={
                                             # "signInDay": signInCount
                                             "signInDay": sign_day
                                         },
                                         headers={"Authorization": 'Bearer ' + access_token})

                    res3 = res3.json()
                    reward_name = res3.get("result", {}).get("name")
                    reward_description = res3.get("result", {}).get("description")
                    mg += "本月第{}天的奖励已领取成功！\n".format(sign_day)
                except:
                    mg += ("领取{}日奖励失败！\n".format(sign_day))


def is_last_day_of_month():
    """判断今天是否为月底"""
    today = date.today()

    _, last_day = calendar.monthrange(today.year, today.month)

    # 返回月底的日期 和 是否为月底
    return last_day, today.day == last_day


def job():
    """执行签到或者领取奖励"""
    end_day, is_last_day = is_last_day_of_month()

    # 签到
    aliyun_drive_sign_in()

    # 如果是月底，则领取月初到月底的奖励
    if is_last_day:
        # 遍历日期
        for i in range(1, end_day + 1):
            # 领取奖励
            aliyun_drive_get_sign_award(i)
        # 发送领取奖励邮件
        global mg
        send_message_to_email(mg)
        mg = "阿里云盘奖励领取：\n"


def start():
    # schedule.every().day.at("09:00").do(job)  # 每天的09:00执行任务
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    job()


if __name__ == '__main__':
    # 多token
    # refresh_tokens = ["token1", "token2", "token3"]
    mg = "阿里云盘奖励领取：\n"

    refresh_tokens = ["a6d1bf09600c4b128d7e82f64b017390"]
    start()
