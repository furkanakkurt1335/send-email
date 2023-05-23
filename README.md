# send-email

Script to send emails by smtp

## Usage

```bash
python3 main.py --sender <sender email address> --password <password> --receiver <receiver email address> --subject <subject> --body <body> --port <port number> --smtp <smtp server address>
```

None of the flags are required. If not provided, the script will ask for the missing information. If port or smtp is not provided, the script will use the default values for Gmail, which are 465 and smtp.gmail.com respectively.

## Example

```bash
python3 main.py
Enter sender email address: <sender email address>
Enter password: <password>
Enter receiver email address: <receiver email address>
Enter subject: <subject>
Enter body: <body>
Port number not provided, using default port 465
SMTP server address not provided, using default smtp server address smtp.gmail.com
Mail sent successfully
```

## Note

- Gmail requires you to create an App password to bypass 2-step verification. You can create one [here](https://myaccount.google.com/apppasswords).
