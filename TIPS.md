# 🎨 CampusRetrieve - Tips & Customization Guide

Make CampusRetrieve your own with these customization tips and best practices!

---

## 🎨 Visual Customizations

### 1. Change Color Scheme

Edit `templates/layout.html`, find the `:root` section in the `<style>` tag:

```css
:root {
    --primary-color: #2c3e50;      /* Main dark color */
    --secondary-color: #3498db;     /* Accent blue */
    --success-color: #27ae60;       /* Green for "Found" */
    --danger-color: #e74c3c;        /* Red for "Lost" */
}
```

**Popular Color Schemes:**

**Purple Theme:**
```css
--primary-color: #6c5ce7;
--secondary-color: #a29bfe;
--success-color: #00b894;
--danger-color: #d63031;
```

**Orange Theme:**
```css
--primary-color: #e17055;
--secondary-color: #fdcb6e;
--success-color: #00b894;
--danger-color: #d63031;
```

**Dark Theme:**
```css
--primary-color: #2d3436;
--secondary-color: #0984e3;
--success-color: #00b894;
--danger-color: #d63031;
```

### 2. Change Site Name/Logo

Edit `templates/layout.html`, find:
```html
<a class="navbar-brand" href="{{ url_for('index') }}">
    <i class="bi bi-search"></i> CampusRetrieve
</a>
```

Change to:
```html
<a class="navbar-brand" href="{{ url_for('index') }}">
    <i class="bi bi-bookmark-star"></i> Your Campus Name
</a>
```

**Icon Options:** Browse [Bootstrap Icons](https://icons.getbootstrap.com/)

### 3. Customize Hero Section

Edit `templates/index.html`:
```html
<h1 class="display-4 mb-3">
    <i class="bi bi-search"></i> Your Custom Title Here!
</h1>
<p class="lead mb-4">
    Your custom subtitle or mission statement
</p>
```

### 4. Add Custom Logo Image

1. Place logo in `static/` folder (e.g., `logo.png`)
2. In `layout.html`, replace icon with:
```html
<a class="navbar-brand" href="{{ url_for('index') }}">
    <img src="{{ url_for('static', filename='logo.png') }}" 
         alt="Logo" height="40"> CampusRetrieve
</a>
```

---

## ⚙️ Functional Customizations

### 1. Add New Categories

**In `templates/report.html`:**
```html
<select class="form-select" id="category" name="category" required>
    <option value="">Select a category...</option>
    <option value="Electronics">📱 Electronics</option>
    <option value="Books">📚 Books</option>
    <option value="ID Cards">🪪 ID Cards</option>
    <option value="Keys">🔑 Keys</option>
    <option value="Clothing">👕 Clothing</option>
    <option value="Bags">🎒 Bags</option>
    <option value="Sports Equipment">⚽ Sports Equipment</option>  <!-- NEW -->
    <option value="Jewelry">💍 Jewelry</option>  <!-- NEW -->
    <option value="Other">📦 Other</option>
</select>
```

**Also update `templates/index.html` filter section!**

### 2. Add Phone Number to Contact

Already included! Just make sure users fill it in the form.

To make phone **required**, edit `templates/report.html`:
```html
<input type="tel" class="form-control" id="contact_phone" 
       name="contact_phone" required>  <!-- Added required -->
```

### 3. Change Max Image Size

In `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB instead of 16MB
```

### 4. Add More Image Formats

In `app.py`, find:
```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
```

Add more:
```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp'}
```

### 5. Auto-Delete Old Items

Add this function to `app.py`:
```python
from datetime import datetime, timedelta

def delete_old_items():
    """Delete items older than 30 days"""
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    old_items = Item.query.filter(Item.date_posted < thirty_days_ago).all()
    
    for item in old_items:
        # Delete image if exists
        if item.image_filename:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], item.image_filename)
            if os.path.exists(image_path):
                os.remove(image_path)
        db.session.delete(item)
    
    db.session.commit()

# Call this function when app starts
delete_old_items()
```

---

## 📊 Data Management Tips

### 1. View Database Contents

Install DB Browser for SQLite:
- Download: [sqlitebrowser.org](https://sqlitebrowser.org/)
- Open `instance/campusretrieve.db`
- Browse data visually

### 2. Backup Database

**Manual Backup:**
```bash
# Copy database file
cp instance/campusretrieve.db backup_20241205.db
```

**Automated Backup Script:**
```python
# backup_db.py
import shutil
from datetime import datetime

source = 'instance/campusretrieve.db'
backup_name = f'backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db'
shutil.copy(source, backup_name)
print(f"Backup created: {backup_name}")
```

### 3. Export to Excel

Add this route to `app.py`:
```python
import csv
from flask import Response

@app.route('/export')
def export_csv():
    items = Item.query.all()
    
    def generate():
        yield 'ID,Title,Status,Category,Location,Email,Date\n'
        for item in items:
            yield f'{item.id},"{item.title}",{item.status},{item.category},"{item.location}",{item.contact_email},{item.date_posted}\n'
    
    return Response(generate(), mimetype='text/csv',
                    headers={"Content-Disposition": "attachment;filename=items.csv"})
```

### 4. Reset Database

```bash
# Stop the app (Ctrl+C)

# Delete database
rm instance/campusretrieve.db  # Mac/Linux
del instance\campusretrieve.db  # Windows

# Restart app
python app.py
```

---

## 🔒 Security Enhancements

### 1. Add Simple Password Protection

Create `config.py`:
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-this'
    ADMIN_PASSWORD = 'your-secure-password'
```

In `app.py`:
```python
from config import Config
from flask import session, redirect

app.config.from_object(Config)

def check_auth():
    return session.get('authenticated', False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == app.config['ADMIN_PASSWORD']:
            session['authenticated'] = True
            return redirect(url_for('index'))
    return render_template('login.html')
```

### 2. Rate Limiting

Install:
```bash
pip install Flask-Limiter
```

In `app.py`:
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/report', methods=['POST'])
@limiter.limit("5 per hour")  # Max 5 reports per hour
def report():
    # existing code
```

### 3. Email Verification

Use Flask-Mail:
```bash
pip install Flask-Mail
```

Configure in `app.py`:
```python
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'

mail = Mail(app)

def send_verification_email(email):
    msg = Message('Verify Your Email',
                  sender='noreply@campusretrieve.com',
                  recipients=[email])
    msg.body = 'Click here to verify your email...'
    mail.send(msg)
```

---

## 📱 Mobile Optimizations

### 1. Add PWA Support (Progressive Web App)

Create `static/manifest.json`:
```json
{
  "name": "CampusRetrieve",
  "short_name": "CampusRetrieve",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#2c3e50",
  "theme_color": "#3498db",
  "icons": [
    {
      "src": "/static/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    }
  ]
}
```

In `layout.html` `<head>`:
```html
<link rel="manifest" href="{{ url_for('static', filename='manifest.json') }}">
<meta name="theme-color" content="#3498db">
```

### 2. Add "Share" Button

In `item_detail.html`:
```html
<button onclick="shareItem()" class="btn btn-outline-primary">
    <i class="bi bi-share"></i> Share
</button>

<script>
function shareItem() {
    if (navigator.share) {
        navigator.share({
            title: '{{ item.title }}',
            text: '{{ item.description[:100] }}',
            url: window.location.href
        });
    } else {
        alert('Sharing not supported on this browser');
    }
}
</script>
```

---

## 📈 Analytics & Statistics

### Add Statistics Dashboard

Create new route in `app.py`:
```python
@app.route('/stats')
def stats():
    total = Item.query.count()
    lost = Item.query.filter_by(status='LOST').count()
    found = Item.query.filter_by(status='FOUND').count()
    
    by_category = db.session.query(
        Item.category, 
        db.func.count(Item.id)
    ).group_by(Item.category).all()
    
    return render_template('stats.html', 
                         total=total,
                         lost=lost,
                         found=found,
                         by_category=by_category)
```

Create `templates/stats.html`:
```html
{% extends "layout.html" %}
{% block content %}
<div class="container my-5">
    <h1>Statistics</h1>
    <div class="row">
        <div class="col-md-4">
            <div class="card">
                <div class="card-body text-center">
                    <h2>{{ total }}</h2>
                    <p>Total Items</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card">
                <div class="card-body text-center">
                    <h2 class="text-danger">{{ lost }}</h2>
                    <p>Lost Items</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card">
                <div class="card-body text-center">
                    <h2 class="text-success">{{ found }}</h2>
                    <p>Found Items</p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

---

## 🎯 Performance Tips

### 1. Optimize Image Loading

Add lazy loading in templates:
```html
<img src="..." loading="lazy" alt="...">
```

### 2. Add Pagination

In `app.py`:
```python
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    items = Item.query.order_by(Item.date_posted.desc()).paginate(
        page=page, per_page=12, error_out=False
    )
    return render_template('index.html', items=items)
```

### 3. Compress Images on Upload

```bash
pip install Pillow
```

In `app.py`:
```python
from PIL import Image

def compress_image(image_path):
    img = Image.open(image_path)
    img = img.resize((800, 800), Image.LANCZOS)
    img.save(image_path, optimize=True, quality=85)

# After saving file:
compress_image(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
```

---

## 🌐 Deployment Tips

### 1. Environment Variables

Create `.env` file:
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///campusretrieve.db
MAX_FILE_SIZE=16777216
```

Install python-dotenv:
```bash
pip install python-dotenv
```

In `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
```

### 2. Production Settings

Create `config.py`:
```python
import os

class DevelopmentConfig:
    DEBUG = True
    TESTING = False

class ProductionConfig:
    DEBUG = False
    TESTING = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
```

### 3. Use Gunicorn (Production Server)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 🎓 Advanced Features Ideas

1. **QR Code Generation** - For quick item lookup
2. **Email Notifications** - Alert when matching item found
3. **Claim Verification** - Require proof of ownership
4. **Multi-Language Support** - i18n for international students
5. **Dark Mode Toggle** - User preference
6. **Item Matching Algorithm** - AI to suggest matches
7. **Geolocation** - Map view of where items found
8. **Chat System** - In-app messaging
9. **User Profiles** - Track report history
10. **Reward System** - Gamification for finders

---

## 💡 Best Practices

### Code Organization
- Keep routes simple
- Use functions for repeated logic
- Add comments
- Follow PEP 8 style guide

### Database
- Regular backups
- Clean old data
- Index frequently queried fields

### Security
- Never commit secrets to Git
- Use environment variables
- Validate all inputs
- Sanitize filenames

### User Experience
- Clear error messages
- Loading indicators
- Mobile-first design
- Accessibility (ARIA labels)

---

## 🐛 Debugging Tips

### Enable Detailed Errors

In `app.py`:
```python
app.config['PROPAGATE_EXCEPTIONS'] = True
```

### Log to File

```python
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
app.logger.info('Application started')
```

### SQL Query Debugging

```python
app.config['SQLALCHEMY_ECHO'] = True  # Prints all SQL queries
```

---

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/tutorial/)
- [Python File Handling](https://docs.python.org/3/tutorial/inputoutput.html)
- [Web Security Basics](https://owasp.org/www-project-top-ten/)

---

**Happy Coding! 🚀**

Remember: Start simple, test often, and add features gradually!