# AI_Shooter_Game
# 🕹️ AI Shooter Game (Computer Vision Project)

### 🎯 Overview
**AI Shooter Game** is a real-time **Computer Vision–based interactive game** built using **OpenCV**, **cvzone**, and **MediaPipe**.  
Your **real hand** (detected through your webcam) controls the game — no keyboard or mouse needed!

You must **hit the green points** to increase your score 🟢  
But be careful — if you **touch the bee 🐝**, the game will **end immediately!**

---

### 🚀 Features
- 🖐️ Real-time **hand tracking** using your webcam  
- 🎯 **Moving points** increase score when touched  
- 🐝 **Bee objects** move randomly — hitting one causes Game Over  
- ⚡ Smooth and fast gameplay with OpenCV frame updates  
- 💡 Demonstrates real-world use of **AI + Computer Vision**

---

### 🧰 Technologies Used
| Library | Purpose |
|----------|----------|
| **Python** | Main programming language |
| **OpenCV** | Image processing & camera handling |
| **cvzone** | Simplifies hand tracking and overlays |
| **MediaPipe** | AI model for real-time hand detection |
| **Math** | Distance calculation for collisions |

---

### 🧩 How the Game Works
1. The webcam captures your live video feed.  
2. The **index finger tip** of your hand is detected.  
3. **Points** and **Bees** move randomly across the screen.  
4. If your finger touches:
   - 🟢 **Point →** +1 Score  
   - 🐝 **Bee →** Game Over  

---

### ⚙️ Installation
Make sure **Python 3.8+** is installed on your system.  
Then install the required libraries using the following commands:

```bash
pip install opencv-python
pip install cvzone
pip install mediapipe
