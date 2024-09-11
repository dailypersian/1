import smtplib
from email.mime.text import MIMEText
import random
import schedule
import time

# تنظیمات ایمیل
smtp_server = 'smtp.gmail.com'  # آدرس سرور SMTP
smtp_port = 587                   # پورت سرور SMTP
smtp_user = 'dailypersian1@gmail.com'  # ایمیل فرستنده
smtp_password = 'rdtf scgd eplj sdng'      # رمز عبور ایمیل
to_email = 'ho3einsaghafi3@gmail.com'   # ایمیل گیرنده

# لیست جملات انگیزشی
quotes = [
    "زندگی همواره بهترین معلم است، اما باید یاد بگیریم که از آن درس بگیریم.",
    "هر روز یک شروع جدید است، با خودت مهربان باش.",
    "هر چیزی که نیاز داری، در درون خودت وجود دارد.",
    "تلاش برای موفقیت، نتیجه‌ای بسیار ارزشمند دارد.",
    "به جای نگرانی درباره شکست، از تلاش برای موفقیت لذت ببر.",
    "هر قدمی که در مسیر هدف‌هایت برمی‌داری، نزدیک‌ترت می‌کند به موفقیت.",
    "فرصت‌ها در کنار چالش‌ها پنهان شده‌اند، آنها را بشناسید.",
    "بزرگ‌ترین موانع در مسیر موفقیت، باورهای منفی هستند.",
    "از شکست نترسید، از عدم تلاش بترسید.",
    "باور به خود و توانایی‌هایت، کلید موفقیت است."
]

def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # شروع اتصال امن
        server.login(smtp_user, smtp_password)  # ورود به حساب ایمیل
        server.sendmail(smtp_user, to_email, msg.as_string())  # ارسال ایمیل

def send_welcome_email():
    subject = 'خوش آمدید!'
    body = "سلااااااام به جملات روزانه آهوتکست خوش آمدید!"
    send_email(subject, body, to_email)
    print("ایمیل خوش‌آمدگویی ارسال شد.")

def get_random_quote():
    return random.choice(quotes)

def job():
    quote = get_random_quote()
    subject = 'متن انگیزشی روز'
    body = quote
    send_email(subject, body, to_email)
    print("ایمیل ارسال شد:", quote)

# ارسال ایمیل خوش‌آمدگویی هنگام اجرای برنامه
send_welcome_email()

# برنامه‌ریزی برای اجرای روزانه
schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # چک کردن هر دقیقه
