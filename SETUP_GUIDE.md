# CampusRetrieve - Complete Setup Guide

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [Installation Steps](#installation-steps)
4. [Running the Application](#running-the-application)
5. [Testing the Application](#testing-the-application)
6. [Troubleshooting](#troubleshooting)
7. [Deployment](#deployment)

---

## ✅ Prerequisites

### Required Software:
- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **VS Code** or any text editor - [Download VS Code](https://code.visualstudio.com/)
- **Git** (optional) - [Download Git](https://git-scm.com/)
- **Web Browser** (Chrome, Firefox, Safari, or Edge)

### Check Python Installation:
```bash
python --version
# or
python3 --version
```

---

## 📁 Project Structure

Create the following folder structure:

```
CampusRetrieve/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── templates/                  # HTML templates
│   ├── layout.html            # Base template
│   ├── index.html             # Home page
│   ├── report.html            # Report item page
│   ├── item_detail.html       # Item detail page
│   └── about.html             # About page
│
├── static/                     # Static files
│   └── uploads/               # Uploaded images (auto-created)
│
└── instance/                   # Database folder (auto-created)
    └── campusretrieve.db      # SQLite database
```

---

## 🚀 Installation Steps

### Step 1: Create Project Folder

**Windows:**
```bash
# Open Command Prompt or PowerShell
mkdir CampusRetrieve
cd CampusRetrieve
```

**Mac/Linux:**
```bash
# Open Terminal
mkdir CampusRetrieve
cd CampusRetrieve
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command line.

### Step 3: Create requirements.txt

Create a file named `requirements.txt` with the following content:

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Werkzeug==3.0.1
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Create Folder Structure

**Windows:**
```bash
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

### Step 6: Create Files

Create the following files with the content provided in the artifacts:

1. **app.py** - Main Flask application
2. **templates/layout.html** - Base template
3. **templates/index.html** - Home page
4. **templates/report.html** - Report item page
5. **templates/item_detail.html** - Item detail page
6. **templates/about.html** - About page

---

## 🎯 Running the Application

### Step 1: Activate Virtual Environment (if not already active)

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 2: Run the Flask App

```bash
python app.py
```

You should see output like:
```
Database initialized successfully!
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
```

### Step 3: Open in Browser

Open your web browser and go to:
```
http://127.0.0.1:5000
```

or

```
http://localhost:5000
```

---

## 🧪 Testing the Application

### Test 1: Report a Lost Item

1. Click **"Report Item"** in the navigation bar
2. Select **"I Lost Something"**
3. Fill in the form:
   - **Item Name:** "Black iPhone 13"
   - **Category:** "Electronics"
   - **Description:** "Black iPhone 13 with blue case, cracked screen"
   - **Location:** "Library 2nd Floor"
   - **Email:** your-email@example.com
4. Click **"Submit Report"**
5. You should be redirected to the home page with a success message

### Test 2: Report a Found Item with Image

1. Click **"Report Item"**
2. Select **"I Found Something"**
3. Fill in the form:
   - **Item Name:** "Red Water Bottle"
   - **Category:** "Other"
   - **Description:** "Red stainless steel water bottle with stickers"
   - **Location:** "Cafeteria"
   - **Upload Image:** Select an image from your computer
   - **Email:** your-email@example.com
4. Click **"Submit Report"**

### Test 3: Search and Filter

1. On the home page, use the filter section:
   - **Search:** Try searching "iPhone"
   - **Status:** Select "LOST"
   - **Category:** Select "Electronics"
2. Click **"Filter"** button

### Test 4: View Item Details

1. Click on any item card
2. Click **"View Details"**
3. You should see the full item information
4. Test the **"Contact"** button - it should open your email client

### Test 5: Delete an Item

1. View an item's detail page
2. Scroll to the bottom
3. Click **"Delete This Item"**
4. Confirm the deletion

---

## 🔧 Troubleshooting

### Problem 1: Port Already in Use

**Error:** `Address already in use`

**Solution:**
```bash
# Windows: Find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# Mac/Linux: Find and kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

Or run Flask on a different port:
```python
# In app.py, change the last line to:
app.run(debug=True, port=8080)
```

### Problem 2: ModuleNotFoundError

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
Make sure your virtual environment is activated and dependencies are installed:
```bash
# Activate venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

### Problem 3: Database Not Created

**Error:** `sqlalchemy.exc.OperationalError`

**Solution:**
Delete the database and let Flask recreate it:
```bash
# Windows
del instance\campusretrieve.db

# Mac/Linux
rm instance/campusretrieve.db

# Restart the app
python app.py
```

### Problem 4: Image Upload Not Working

**Solution:**
1. Check that the `static/uploads` folder exists
2. Check file permissions
3. Make sure the image is under 16MB
4. Only use `.jpg`, `.jpeg`, `.png`, or `.gif` formats

### Problem 5: Template Not Found

**Error:** `jinja2.exceptions.TemplateNotFound`

**Solution:**
- Make sure all templates are in the `templates/` folder
- Check that filenames match exactly (case-sensitive on Linux/Mac)

---

## 🌐 Deployment

### Option 1: Local Network Access

To allow others on your network to access:

```python
# In app.py, change the last line to:
app.run(debug=True, host='0.0.0.0', port=5000)
```

Find your IP address:
- **Windows:** `ipconfig`
- **Mac/Linux:** `ifconfig` or `ip addr`

Others can access via: `http://YOUR_IP_ADDRESS:5000`

### Option 2: Deploy to PythonAnywhere (Free)

1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload your files
3. Set up a web app with Flask
4. Configure the WSGI file
5. Reload the web app

### Option 3: Deploy to Render (Free)

1. Sign up at [Render](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Render will auto-detect Flask and deploy

---

## 📱 Usage Tips

### For Best Results:

1. **Use High-Quality Photos:** Clear photos increase recovery rates
2. **Be Specific:** Include unique identifiers (color, brand, scratches)
3. **Update Location:** Mention specific rooms or landmarks
4. **Check Regularly:** New items are posted daily
5. **Delete When Found:** Keep the database clean

### Security Notes:

⚠️ **Important:** This is a demo/educational project. For production use:
- Add user authentication
- Implement email verification
- Add CAPTCHA to prevent spam
- Use environment variables for secrets
- Deploy with HTTPS
- Add rate limiting

---

## 📊 Database Schema

```sql
CREATE TABLE item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(50) NOT NULL,
    location VARCHAR(200) NOT NULL,
    status VARCHAR(10) NOT NULL,
    contact_email VARCHAR(120) NOT NULL,
    contact_phone VARCHAR(20),
    image_filename VARCHAR(300),
    date_posted DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🛠️ Customization

### Change Colors

Edit the CSS in `templates/layout.html`:
```css
:root {
    --primary-color: #2c3e50;      /* Change to your color */
    --secondary-color: #3498db;     /* Change to your color */
    --success-color: #27ae60;       /* Change to your color */
    --danger-color: #e74c3c;        /* Change to your color */
}
```

### Add New Categories

In `app.py` or templates, add to the category list:
```python
categories = ['Electronics', 'Books', 'ID Cards', 'Keys', 'Clothing', 'Bags', 'Sports Equipment', 'Other']
```

### Change Max File Size

In `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB (change this value)
```

---

## 📞 Support

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review Flask documentation: https://flask.palletsprojects.com/
3. Check error logs in the console
4. Ensure all dependencies are installed correctly

---

## 🎓 Learning Resources

- **Flask Tutorial:** https://flask.palletsprojects.com/tutorial/
- **SQLAlchemy Docs:** https://docs.sqlalchemy.org/
- **Bootstrap 5:** https://getbootstrap.com/docs/5.3/
- **Python File Handling:** https://docs.python.org/3/tutorial/inputoutput.html

---

## ✅ Checklist

Before submitting your project, ensure:

- [ ] All pages load correctly
- [ ] Can report lost items
- [ ] Can report found items with images
- [ ] Search and filter work
- [ ] Contact buttons open email
- [ ] Images display properly
- [ ] Delete function works
- [ ] Mobile responsive design works
- [ ] No console errors
- [ ] Database persists data after restart

---

## 🎉 Success!

You now have a fully functional Lost & Found system! 

**Good luck with your project! 🚀**