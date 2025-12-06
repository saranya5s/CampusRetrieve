# 🔍 CampusRetrieve - Lost & Found Hub

A centralized web-based platform for managing lost and found items in educational institutions. This project eliminates the inefficiency of scattered WhatsApp groups and physical notice boards by providing a digital solution for reporting and claiming lost items.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-Educational-yellow.svg)

---

## 📌 Project Overview

**CampusRetrieve** is a Computer Science project that demonstrates:
- **MVC Architecture** (Model-View-Controller)
- **File Handling** (Image uploads)
- **Search Algorithms** (Filtering and sorting)
- **Database Persistence** (SQLAlchemy ORM with SQLite)
- **Responsive Web Design** (Bootstrap 5)

---

## ✨ Features

### Core Functionality
- ✅ **Report Lost Items** - Students can post details about items they've lost
- ✅ **Report Found Items** - Students can upload photos of items they've found
- ✅ **Advanced Search** - Filter by status (Lost/Found), category, and keywords
- ✅ **Visual Verification** - Photo uploads for found items
- ✅ **One-Click Contact** - Email integration via mailto: protocol
- ✅ **Status Tracking** - Clear visual distinction between Lost (Red) and Found (Green)
- ✅ **Mobile Responsive** - Works seamlessly on smartphones and tablets

### Categories
- 📱 Electronics (phones, laptops, chargers)
- 📚 Books (textbooks, notebooks)
- 🪪 ID Cards (student IDs, licenses)
- 🔑 Keys (room keys, car keys)
- 👕 Clothing (jackets, bags)
- 🎒 Bags (backpacks, purses)
- 📦 Other

---

## 🏗️ System Architecture

### 6 Key Modules

1. **User Interface (UI) Module**
   - HTML templates with Jinja2
   - Bootstrap 5 for responsive design
   - Custom CSS styling

2. **Item Reporting & Validation Module**
   - Form handling and validation
   - Input sanitization
   - POST request processing

3. **Media & File Management Module**
   - Secure file uploads
   - Image validation (.jpg, .png, .gif)
   - Filename sanitization with timestamps

4. **Search & Retrieval Engine Module**
   - Multi-criteria filtering
   - Keyword search
   - Date-based sorting

5. **Communication & Interaction Module**
   - Email integration (mailto:)
   - Contact information management

6. **Database Persistence Module**
   - SQLite database
   - SQLAlchemy ORM
   - CRUD operations

---

## 🛠️ Technical Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5.3.0
- Bootstrap Icons

### Backend
- Python 3.8+
- Flask 3.0.0 (Web Framework)
- Flask-SQLAlchemy 3.1.1 (ORM)
- Werkzeug 3.0.1 (File Security)

### Database
- SQLite (Lightweight, serverless)

### Tools
- VS Code (IDE)
- Git (Version Control)

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Quick Start

1. **Clone or Download the Project**
```bash
git clone https://github.com/yourusername/campusretrieve.git
cd campusretrieve
```

2. **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Create Folder Structure**
```bash
mkdir templates
mkdir static
mkdir static/uploads
```

5. **Run the Application**
```bash
python app.py
```

6. **Open in Browser**
```
http://127.0.0.1:5000
```

For detailed setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md)

---

## 📸 Screenshots

### Home Page
- Grid view of all lost and found items
- Filter by status, category, and search keywords
- Color-coded badges for easy identification

### Report Item Page
- User-friendly form with validation
- Image upload with preview
- Categorization options

### Item Detail Page
- Full item information
- Contact buttons (email/phone)
- Image display

---

## 💡 Usage Scenarios

### Scenario 1: Lost Wallet
1. Student A loses their wallet in the cafeteria
2. Posts a "LOST" report with description
3. Student B finds it and searches the portal
4. Student B sees the post and contacts Student A via email

### Scenario 2: Found Keys
1. Student C finds keys on the library floor
2. Posts a "FOUND" report with a photo
3. The owner sees the photo and recognizes their keys
4. Owner contacts Student C to arrange pickup

### Scenario 3: Lost Phone
1. Student D loses phone during sports practice
2. Posts details immediately on CampusRetrieve
3. Security guard finds it and checks the portal
4. Match found and phone returned within hours

---

## ⚖️ Advantages & Limitations

### Advantages ✅
- **Centralized Platform** - No need to check multiple locations
- **Visual Proof** - Photos reduce confusion
- **Real-Time Updates** - Instant notifications
- **24/7 Accessibility** - Access from anywhere
- **Organized Database** - Easy to search and filter

### Limitations ⚠️
- **Trust-Based System** - Relies on user honesty
- **Privacy Concerns** - Contact info is visible
- **Manual Maintenance** - Old items need deletion
- **Internet Required** - Needs online connectivity

---

## 🔒 Security Considerations

**Note:** This is an educational project. For production use, implement:
- User authentication (login/registration)
- Email verification
- CAPTCHA for spam prevention
- Rate limiting
- HTTPS/SSL encryption
- Environment variables for secrets
- Admin dashboard for moderation
- IP tracking for suspicious activity

---

## 🚀 Future Enhancements

- [ ] User authentication system
- [ ] SMS notifications
- [ ] Admin dashboard
- [ ] Claim verification system
- [ ] Auto-archive old items (30+ days)
- [ ] Multi-campus support
- [ ] Mobile app (iOS/Android)
- [ ] Push notifications
- [ ] Advanced analytics
- [ ] Integration with campus security

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

## 🧪 Testing

### Manual Testing Checklist
- [ ] Report lost item without image
- [ ] Report found item with image
- [ ] Search functionality
- [ ] Filter by status
- [ ] Filter by category
- [ ] View item details
- [ ] Contact via email
- [ ] Delete item
- [ ] Mobile responsiveness
- [ ] Image upload validation

---

## 📁 Project Structure

```
CampusRetrieve/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── SETUP_GUIDE.md             # Detailed setup instructions
│
├── templates/                  # HTML templates
│   ├── layout.html            # Base template
│   ├── index.html             # Home page
│   ├── report.html            # Report item page
│   ├── item_detail.html       # Item detail page
│   └── about.html             # About page
│
├── static/                     # Static files
│   └── uploads/               # Uploaded images
│
└── instance/                   # Database (auto-generated)
    └── campusretrieve.db      # SQLite database
```

---

## 🤝 Contributing

This is an educational project. Contributions for learning purposes are welcome!

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is created for educational purposes as part of a Computer Science curriculum.

---

## 👥 Authors

- **Your Name** - *Initial work* - Computer Science Student

---

## 🙏 Acknowledgments

- Flask documentation and community
- Bootstrap team for the UI framework
- SQLAlchemy documentation
- All contributors to open-source libraries used

---

## 📞 Support

For issues and questions:
1. Check the [SETUP_GUIDE.md](SETUP_GUIDE.md)
2. Review Flask documentation
3. Check console error logs
4. Ensure all dependencies are installed

---

## 🎓 Learning Outcomes

By completing this project, you will learn:
- Web application development with Flask
- Database design and ORM usage
- File handling and security
- Form validation and user input
- Responsive web design
- MVC architecture implementation
- RESTful routing
- Template inheritance with Jinja2

---

**Made with ❤️ for educational purposes**

**Star ⭐ this repo if you found it helpful!** 