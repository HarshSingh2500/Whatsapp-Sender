# 📤 WhatsApp Message Sender with Excel Support

Send WhatsApp messages (common or personalized) to multiple contacts from an Excel sheet using a simple web interface built with Flask and `pywhatkit`.

---

## 🚀 Features

- ✅ Upload Excel files with contact numbers
- ✅ Send one message to all contacts (common message)
- ✅ Send different messages to each contact (personalized)
- ✅ Background processing — no need to wait on the website
- ✅ Easy-to-use web interface

---

## 📁 Project Structure

Whatsapp-Sender/

│

├── app.py # Main Flask application

├── requirements.txt # Python dependencies

├── uploads/ # Uploaded Excel files (auto-created)

├── templates/

    ├── index.html # Landing page with instructions 
    
    ├── common.html # Upload form for common message

    └── personalized.html # Upload form for personalized message

├── utils/

    └── send_messages.py # Functions to send messages using pywhatkit



---

## 📋 Excel Format

### ✅ For **Common Message**
Only contact numbers are needed.

**Example:**
| Phone         |
|---------------|
| 919876543210  |
| 919123456789  |

### ✅ For **Personalized Message**
Each contact must have a corresponding message.

**Example:**
| Phone         | Message                   |
|---------------|---------------------------|
| 919876543210  | Hello Raj, good morning!  |
| 919123456789  | Hi Meena, how are you?    |

> ⚠️ Important: Format mobile numbers as plain text to avoid Excel converting them to `9.19872E+11`.

---

## ⚙️ Installation & Setup

> 🔧 This app uses `pywhatkit` which opens WhatsApp Web in your browser — make sure you're logged in.

1. **Clone the repository**

    git clone https://github.com/yourusername/Whatsapp-Sender.git

    cd Whatsapp-Sender


2. **(Optional but recommended) Create a virtual environment**

    python -m venv venv

    venv\Scripts\activate  # On Windows


3. **Install dependencies**

    pip install -r requirements.txt


4. **Run the app**

    python app.py


5. **Open in browser**

    http://127.0.0.1:5000


# 🕐 How It Works
Each message is scheduled 1–2 minutes in the future using pywhatkit.

Messages are sent in background — you can return to the homepage after upload.

Sending to multiple contacts may take time (~15 seconds delay per contact).

# 💡 Note
Works only if WhatsApp Web is accessible and you’re logged in.

Don’t close the browser tab until messages are sent.

You can customize delays or add features like scheduling in send_messages.py.

# 🧾 License
This project is open-source under the MIT License.