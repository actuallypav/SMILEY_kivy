## Overview

A simple system for collecting real-time feedback from students. Inspired by IKEA's satisfaction buttons, this Kivy-based app provides a five-button interface for users to rate their experience. Built in just over a day for a final-year university project, this system was built with the thought of being deployed within university premises to gather feedback efficiently.

### Features
- Intuitive UI for quick feedback collection.
- Five reaction options: 😡 😞 😐 🙂 😃.
- Secure session-based login using numeric room codes.
- Real-time database updates with MySQL.
- Touch-friendly interface designed for kiosks or tablets.

### Technologies Used
- **Kivy** (for UI development)
- **Python** (core logic and database handling)
- **MySQL** (storing feedback data)
- **ConfigParser** (handling app configuration)

### How It Works
1. Users enter a **room code** to start a session.
2. The system validates the room code against the database.
3. Once logged in, users select one of five **emoji-based reactions**.
4. The response is instantly recorded in the database.
5. Users can log out, and the system resets for the next user.

### Installation
1. Clone this repo:
   ```sh
   git clone https://github.com/your-repo/smiley-feedback.git
   ```
2. Install dependencies:
   ```sh
   pip install kivy pymysql
   ```
3. Set up your **config.ini** file with database credentials.
4. Run the app:
   ```sh
   python main.py
   ```

### File Structure
- `main.py` → Core logic & UI control.
- `main.kv` → Kivy layout for UI design.
- `config.ini` → Database configuration.
- `images/` → Contains emoji face images for reactions.

### Future Improvements
- Add analytics to visualize feedback trends.
- Implement touch gestures for smoother interaction.
- Store feedback locally in case of network failure.

### Module Information
This project was developed as part of the **Enterprise Application Management** module. The module focuses on developing skills to apply and manage on-premise and cloud-based virtualized computing systems. Students work in teams to analyze organizational requirements, assess risks, and design, develop, and evaluate virtualized enterprise systems to meet specific computing needs.

### Credits
Developed as a **final-year university project** to enhance feedback collection in educational environments.

