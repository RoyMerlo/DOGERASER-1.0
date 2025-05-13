[dogeraser](https://github.com/user-attachments/assets/a313e5e1-f56b-4797-a53a-616527e00d15)



**DOGERASER** is a modern, GUI-based file and folder shredder written in Python. It securely and irreversibly deletes files and directories using multiple military-grade data erasure algorithms, such as **DoD 5220.22-M**, **Gutmann**, and **Schneier**.

Built with a sleek and futuristic interface using **Tkinter**, DOGERASER is ideal for users who need to ensure that sensitive data is permanently destroyed and unrecoverable—even with forensic tools.


![doggo](https://github.com/user-attachments/assets/5b72fb6e-03ac-4b41-bc62-95af3dd36f79)

---

## 🔥 Key Features

- 🛡 **DoD 5220.22-M Method** – 3-pass overwrite strategy used by the U.S. Department of Defense.
- 🧠 **Gutmann Method** – 35 overwriting patterns for maximal destruction.
- 🔒 **Schneier Method** – A 7-pass secure deletion approach.
- 📁 Works on both files and folders.
- ⚙️ Smart, user-friendly GUI with confirmation dialogs.
- 💾 Optional overwrite patterns + final deletion.
- ⚫ Stylish dark interface with neon-glow inspired design.
- 👤 "Powered by Roy Merlo" credit built-in.

---

## 🛠 Requirements

- Python 3.x
- Standard Python libraries (no external dependencies required)

Install Python if it's not already installed: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## 🚀 How to Run

1. Clone or download this repository.
2. Launch the application:

```bash
python BULLERASER.PY
📖 How It Works
🔐 Algorithms
DoD 5220.22-M

Overwrites file data 3 times using random bytes.

Used by U.S. military standards.

Gutmann

Performs 35 overwrite passes (with specific and random patterns).

Designed to obscure data on older magnetic media but still effective for thorough erasure.

Schneier

7-pass algorithm using random data.

Based on recommendations by cryptographer Bruce Schneier.

🧼 Secure Delete Process
The selected file/folder is overwritten with the chosen algorithm's pattern.

After overwriting, the file is deleted from disk using os.remove() or shutil.rmtree() for folders.

Subdirectories and nested files are securely handled recursively.

🖼 GUI Overview
DOGERASER title with futuristic font

Three large buttons to choose deletion method:

"🛡 DoD"

"🧠 Gutmann"

"🔒 Schneier"

Each button opens a file/folder selection dialog

User is prompted to confirm before deletion

Completion and error dialogs ensure user feedback

⚠️ Warning
This tool permanently deletes files and folders. Once deleted using DOGERASER, recovery is practically impossible. Use with caution!

🧠 Use Cases
Securely erasing sensitive documents (contracts, IDs, credentials)

Wiping confidential folders before transferring a computer

Cleaning up remnants from secure data operations

📂 File Info
File	Description
BULLERASER.PY	Main application file (GUI + logic)

✨ Credits
Designed and developed by Roy Merlo

GUI in Tkinter with custom styles

Inspired by military data wiping standards

📜 License
This project is open-source and free to use for educational or personal use.

Want to contribute or suggest improvements? Fork the repo or submit an issue!



