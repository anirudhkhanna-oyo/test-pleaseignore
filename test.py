...
# Replace sender@yourdomain.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "Sender Name <sender@yourdomain.com>"

# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT = "recipient@example.com"

# The subject line for the email.
SUBJECT = "Hey, Wizard! Check out this dynamic email."

# The HTML email body for recipients with non-AMP email clients.
BODY_HTML = "<p>Expelliarmus! In HTML.</p>"

# The AMPHTML email body for recipients with AMP-supporting email clients.
BODY_AMPHTML = """\
<!doctype html>
<html amp4email>
<head>
  <meta charset="utf-8">
  <script async src="https://cdn.ampproject.org/v0.js"></script>
  <style amp4email-boilerplate>body{visibility:hidden}</style>
</head>
<body> <p>Alohomora! In AMP. :)</p> </body>
</html>
"""
.
.
.
# Encode the text and HTML content and set the character encoding.
htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
amphtmlpart = MIMEText(BODY_AMPHTML.encode(CHARSET), 'x-amp-html', CHARSET)

# Add the text and HTML parts to the child container.
msg_body.attach(htmlpart)
msg_body.attach(amphtmlpart)
.
.
.
try:
    #Provide the contents of the email.
    response = client.send_raw_email(
        Source=SENDER,
        Destinations=[
            RECIPIENT
        ],
        RawMessage={
            'Data':msg.as_string(),
        },
        # ConfigurationSetName=CONFIGURATION_SET
    )
# Display an error if something goes wrong.	
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])
