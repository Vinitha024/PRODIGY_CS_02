# Image Encryption Tool | Task 02
This project is part of my Cyber Security Internship at Prodigy InfoTech.
The purpose of this task is to build a tool that can encrypt and decrypt images using pixel manipulation.

Instead of using advanced encryption algorithms, this project uses a simple concept:
👉 Change the pixel values using a secret key so the image becomes unreadable.

Later, using the same key, the image can be restored.
## How It Works

- Each pixel has RGB values (0–255)
- Encryption formula: encrypted_pixel = original_pixel ^ key
- Decryption uses the **same formula** (because XOR is reversible)

---

## Requirements

Install Pillow:pip install Pillow

---

## Run the Program 
python image_encryption_tool.py


Then:

1. Choose **Encrypt** or **Decrypt**
2. Enter input image name
3. Enter output file name
4. Enter a key (1–255)

---

## 🧩 Example

Input: flower.png
Output: encrypted.png
Key: 123

Decrypt with:

Input: encrypted.png
Output: original.png
Key: 123

---

## 🎓 What I Learned

- Basics of pixel manipulation  
- How RGB values represent images  
- Simple symmetric encryption  
- File handling with Python  
- Working with Pillow library  

---

## Author

**Vinitha G**  
💼 Prodigy InfoTech Cybersecurity Intern  
🔗 GitHub: @Vinitha024

