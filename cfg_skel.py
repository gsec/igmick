CFG = dict(
    image=dict(
        sleeptime=5,
        cut=((540, 570), (10, 350)),
        # (y-start, y-end) , (x-start, x-end)
        tolerance=10,
    ),
    mail=dict(
        port=587,  # For starttls
        smtp_server="smtp.gmail.com",  # for gmail
        sender_email="you@gmail.com",
        receiver_email="youorsomebodyelse@hoster.com",
        password="SUPERSECURE",
        message="""\
Subject: Image stands still

Hello There
""",
    ),
)
