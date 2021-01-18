import smtplib
from email.mime.text import MIMEText


def send_mail(customer, product, rating, comments):
   port = 2525
   smtp_server = 'smtp.mailtrap.io'
   login = '7c30e4d46db4ab'
   password = 'dd7969643f32c0'
   message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {product}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

   sender_email = 'gorgias780@gmail.com'
   receiver_email = 'gorgias780@gmail.com'
   msg = MIMEText(message, 'html')
   msg['Subject'] = 'Mircod Feedback'
   msg['From'] = sender_email
   msg['To'] = receiver_email

    # Send email
   with smtplib.SMTP(smtp_server, port) as server:
      server.login(login, password)
      server.sendmail(sender_email, receiver_email, msg.as_string())