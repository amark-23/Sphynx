---
### ** README.md for backend**
```
# Sphynx File Server

You will need an **Ubuntu Server** in your local network for these installation steps.
Sphynx is a **self-hosted file server application** that provides a **REST API** for managing files on an **Ubuntu server with Flask**.  
It supports **file uploads, downloads, previews, folder management, searching, sorting, and ZIP compression**.  

A **bash script** is provided for api testing. 

---


---

## **🛠 Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/sphynx.git ~/sphynx
cd ~/sphynx
```

### **2️⃣ Set Up a Python Virtual Environment**
```bash
python3 -m venv sphynx_venv
source sphynx_venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install flask
```

### **4️⃣ Set Up Systemd Service**
Copy the service file to `/etc/systemd/system/`:
```bash
sudo cp sphynx.service /etc/systemd/system/
```
Reload systemd and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable sphynx
sudo systemctl start sphynx
```
Check service status:
```bash
sudo systemctl status sphynx
```

---

## **📡 API Endpoints**
| **Method** | **Endpoint** | **Description** |
|-----------|-------------|----------------|
| **GET** | `/files` | List all files |
| **GET** | `/files?sort=size` | List files sorted by size |
| **POST** | `/upload` | Upload a file |
| **GET** | `/download/<filename>` | Download a file |
| **DELETE** | `/delete/<filename>` | Delete a file |
| **PUT** | `/rename?old_name=old.txt&new_name=new.txt` | Rename a file |
| **POST** | `/move?file=file.txt&to=folder` | Move file to folder |
| **POST** | `/mkdir?name=foldername` | Create a folder |
| **DELETE** | `/rmdir?name=foldername` | Delete an empty folder |
| **GET** | `/search?query=filename` | Search for files |
| **GET** | `/preview/<filename>` | Preview an image or text file |
| **GET** | `/zip?folder=foldername` | Download a folder as a ZIP |
| **GET** | `/stats` | Get total files, storage size, recent uploads |

---



## **📂 File Structure**
```
/.../Sphynx:
│── sphynx_venv/          # Virtual environment
│── sphynx_api/           # Flask API source code
│   ├── __init__.py       # Main Flask app
│   ├── __main__.py       # Entry point
│   ├── config.py         # Configuration file
│   ├── file_routes.py    # File management
│   ├── folder_routes.py  # Folder management
│   ├── search_routes.py  # Search functionality
│   ├── preview_routes.py # File preview system
│   ├── zip_routes.py     # Folder ZIP download
│   ├── stats_routes.py   # API statistics
│── check_api.sh          # API testing script
│── sphynx.service        # Systemd service file
```

---

## **📌 Notes**
- This API runs **on port `5000`** by default. Modify `sphynx_api/__main__.py` to change the port.
- The **base storage directory** is `/mnt/externalhdd/sphynx`. Modify `config.py` if needed.
- **Ensure the firewall allows port `5000`** if accessing externally:
  ```bash
  sudo ufw allow 5000
  ```

---
