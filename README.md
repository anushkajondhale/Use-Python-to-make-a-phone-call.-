# 📞 Phone Call via Python & Twilio

This project demonstrates how to make a **phone call directly from Python** using the Twilio API.

## ⚙️ Setup
1. Install dependencies:
   ```bash
   pip install twilio
   ```

2. Update `env.example.txt` with your Twilio credentials.

3. Load environment variables:
   ```bash
   source load_env.sh
   ```

4. Run the script:
   ```bash
   python3 send_call.py
   ```

## 📌 Notes
- The call uses Twilio’s demo `voice.xml` file by default (it speaks a short message).  
- You can replace the URL with your own TwiML to customize the call.
