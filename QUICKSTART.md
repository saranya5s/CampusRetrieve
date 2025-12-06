# 🚀 CampusRetrieve - Quick Start Guide

Get your Lost & Found Hub running in 5 minutes!

---

## ⚡ Super Quick Setup (For Experienced Users)

```bash
# 1. Create project folder
mkdir CampusRetrieve && cd CampusRetrieve

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Create requirements.txt and install
echo "Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Werkzeug==3.0.1" > requirements.txt

pip install -r requirements.txt

# 5. Create folders
mkdir templates static static/uploads

# 6. Add all project files (see below)

# 7. Run
python app.py

# 8. Open browser to http://127.0.0.1:5000
```

---

## 📝 Step-by-Step Guide (For Beginners)

### Step 1: Install Python
- Download from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation
- Verify: Open terminal/cmd and type `python --version`

### Step 2: Create Project Folder

**Windows (Command Prompt):**
```cmd
cd Desktop
mkdir CampusRetrieve
cd CampusRetrieve
```

**Mac/Linux (Terminal):**
```bash
cd ~/Desktop
mkdir CampusRetrieve
cd CampusRetrieve
```

### Step 3: Set Up Virtual Environment

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` before your command prompt.

### Step 4: Create requirements.txt

Create a file named `requirements.txt` with this content:
```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Werkzeug==3.0.1
```

### Step 5: Install Libraries

```bash
pip install -r requirements.txt
```

Wait for installation to complete (30-60 seconds).

### Step 6: Create Folders

**Windows:**
```cmd
mkdir templates
mkdir static
mkdir static\uploads
```

**Mac/Linux:**
```bash
mkdir templates
mkdir static
mkdir static/uploads
```

### Step 7: Create Project Files

Create these 6 files with the content from the artifacts:

1. **app.py** (in main folder)
2. **templates/layout.html**
3. **templates/index.html**
4. **templates/report.html**
5. **templates/item_detail.html**
6. **templates/about.html**

Your folder should look like:
```
CampusRetrieve/
├── app.py
├── requirements.txt
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── report.html
│   ├── item_detail.html
│   └── about.html
└── static/
    └── uploads/
```

### Step 8: Run the Application

```bash
python app.py
```

You'll see:
```
Database initialized successfully!
 * Running on http://127.0.0.1:5000
```

### Step 9: Open in Browser

Click on the link or type in browser:
```
http://127.0.0.1:5000
```

---

## ✅ Verification Checklist

After setup, verify everything works:

1. **Home Page Loads** ✓
   - Navigate to http://127.0.0.1:5000
   - You should see the hero section and empty item grid

2. **About Page Works** ✓
   - Click "About" in navigation
   - Information should be displayed

3. **Report Form Works** ✓
   - Click "Report Item"
   - Try filling out the form
   - Submit and check if it appears on home page

4. **Image Upload Works** ✓
   - Report an item with an image
   - Check if image displays on home page

5. **Search Works** ✓
   - Add multiple items
   - Try filtering by status and category

6. **Contact Button Works** ✓
   - Click "Contact" on any item
   - Email client should open

---

## 🐛 Common Issues & Quick Fixes

### Issue 1: "python: command not found"
**Fix:** Try `python3` instead of `python`
```bash
python3 --version
python3 app.py
```

### Issue 2: "Port 5000 already in use"
**Fix:** Change the port in app.py (last line):
```python
app.run(debug=True, port=8080)  # Use port 8080 instead
```

### Issue 3: "No module named flask"
**Fix:** Make sure venv is activated:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Then reinstall
pip install -r requirements.txt
```

### Issue 4: Templates Not Found
**Fix:** Make sure templates are in `templates/` folder (lowercase)
```bash
ls templates/  # Mac/Linux
dir templates  # Windows
```

### Issue 5: Can't Upload Images
**Fix:** Create uploads folder:
```bash
mkdir -p static/uploads  # Mac/Linux
mkdir static\uploads     # Windows
```

---

## 🎮 Quick Test Scenarios

### Test 1: Basic Flow (2 minutes)
1. Go to http://127.0.0.1:5000
2. Click "Report Item"
3. Fill form: Lost iPhone, Electronics, Library
4. Submit
5. See it on home page

### Test 2: With Image (3 minutes)
1. Report Item → Found item
2. Add title, category, description
3. Upload an image (any .jpg or .png)
4. Submit
5. Verify image shows on card

### Test 3: Search & Filter (1 minute)
1. Add 3-4 different items
2. Try search box
3. Try status filter (Lost/Found)
4. Try category filter

---

## 🔄 Restart Instructions

To stop the server:
- Press `Ctrl + C` in terminal

To restart:
```bash
# Make sure venv is activated
python app.py
```

To deactivate virtual environment:
```bash
deactivate
```

---

## 📱 Access from Phone (Same WiFi)

1. Find your computer's IP:
   - Windows: `ipconfig` (look for IPv4)
   - Mac: System Preferences → Network
   - Linux: `ip addr`

2. Change app.py last line to:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

3. Restart app

4. On phone browser, go to:
```
http://YOUR_IP_ADDRESS:5000
```

---

## 🎯 Next Steps

Once everything works:

1. **Add Test Data** - Create 10-15 sample items
2. **Test All Features** - Try every button and form
3. **Test on Mobile** - Check responsive design
4. **Customize Colors** - Edit CSS in layout.html
5. **Read Full Documentation** - Check SETUP_GUIDE.md

---

## 💾 Backup Your Data

Database location:
```
CampusRetrieve/instance/campusretrieve.db
```

Uploaded images:
```
CampusRetrieve/static/uploads/
```

To backup:
1. Copy these folders/files
2. Store in a safe location

To restore:
1. Replace with backed-up versions
2. Restart application

---

## 🎓 Learning Path

1. **Week 1:** Get it running, understand structure
2. **Week 2:** Customize colors and text
3. **Week 3:** Add new features (phone numbers, etc.)
4. **Week 4:** Deploy and test with real users

---

## 📞 Need Help?

If stuck:
1. Check error message in terminal
2. Google the error
3. Check [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed help
4. Verify all files are in correct locations
5. Try restarting from Step 1

---

## ✨ You're All Set!

Your CampusRetrieve Lost & Found Hub is ready to use!

**Have fun building and learning! 🚀**

---

**Pro Tip:** Keep the terminal window open while testing so you can see any error messages!