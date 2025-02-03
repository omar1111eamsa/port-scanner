# **Port Scanner**

## 📌 **Description**

This project is a **simple Python Port Scanner** that scans a given IP address for **open ports** within a specified range. It uses the **socket library** to attempt connections and identifies common services running on open ports.

---

## 🛠 **Features**

✔ **Scans a target IP** for open ports  
✔ **Identifies services** running on open ports (if known)  
✔ **Uses a timeout** to avoid long waits  
✔ **Improved error handling** to prevent crashes  
✔ **Simple and lightweight**  

---

## 🚀 **How to Use**

### 1️⃣ **Run the script**

```sh
python port_scanner.py
```

### 2️⃣ **Provide user inputs:**

- **Enter the target IP address**
- **Enter the start port**
- **Enter the end port**

The script will scan the specified port range and **display open ports with their corresponding services**.

---

## 📂 **Example Output**

```
Give the IP address of the target:
127.0.0.1
What is the Start Port:
50
What is the End Port:
10000
Scanning 127.0.0.1 from port 50 to 10000...
[+] Port 80 is open (http)
Scan complete!
```

---

## 🔥 **New Improvements in This Version**

✅ **Enhanced Error Handling**

- **Invalid IP Address Handling:** Prevents scanning if the IP/hostname is incorrect  
- **Port Range Validation:** Ensures user inputs are between `0 - 65535`  
- **Timeout Handling:** Avoids long wait times on unresponsive ports  
- **Unexpected Errors:** Catches exceptions and prevents script crashes  

✅ **Fixed Typo in Input Prompt**

- `"What is the End Prot :"` → `"What is the End Port :"`  

---

## 🎯 **Future Improvements**

🔹 **Add multi-threading** for faster scanning  
🔹 **Save scan results** to a file for later analysis  
🔹 **Improve user interface** with a progress bar  

---

## 🔗 **Contributions**

Feel free to **fork**, **submit pull requests**, or **suggest improvements** to enhance this tool! 🚀

📅 **Last Updated:** 2025-02-03  
👨‍💻 **Author:** Omar  

