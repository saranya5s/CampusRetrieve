from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campusretrieve.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)

# Database Model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(10), nullable=False)  # LOST or FOUND
    contact_email = db.Column(db.String(120), nullable=False)
    contact_phone = db.Column(db.String(20))
    image_filename = db.Column(db.String(300))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Item {self.title}>'

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/')
def index():
    # Get filter parameters
    status_filter = request.args.get('status', '')
    category_filter = request.args.get('category', '')
    search_query = request.args.get('search', '')
    
    # Start with all items
    query = Item.query
    
    # Apply filters
    if status_filter:
        query = query.filter_by(status=status_filter)
    if category_filter:
        query = query.filter_by(category=category_filter)
    if search_query:
        query = query.filter(
            (Item.title.contains(search_query)) | 
            (Item.description.contains(search_query))
        )
    
    # Order by newest first
    items = query.order_by(Item.date_posted.desc()).all()
    
    return render_template('index.html', items=items, 
                         status_filter=status_filter,
                         category_filter=category_filter,
                         search_query=search_query)

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        description = request.form.get('description')
        category = request.form.get('category')
        location = request.form.get('location')
        status = request.form.get('status')
        contact_email = request.form.get('contact_email')
        contact_phone = request.form.get('contact_phone')
        
        # Validation
        if not all([title, description, category, location, status, contact_email]):
            flash('Please fill in all required fields!', 'danger')
            return redirect(url_for('report'))
        
        # Handle file upload
        image_filename = None
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename):
                # Secure the filename and add timestamp
                original_filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                image_filename = f"{timestamp}_{original_filename}"
                
                # Create uploads directory if it doesn't exist
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                
                # Save file
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
        
        # Create new item
        new_item = Item(
            title=title,
            description=description,
            category=category,
            location=location,
            status=status,
            contact_email=contact_email,
            contact_phone=contact_phone,
            image_filename=image_filename
        )
        
        db.session.add(new_item)
        db.session.commit()
        
        flash(f'Item reported successfully! Status: {status}', 'success')
        return redirect(url_for('index'))
    
    return render_template('report.html')

@app.route('/item/<int:id>')
def item_detail(id):
    item = Item.query.get_or_404(id)
    return render_template('item_detail.html', item=item)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    
    # Delete associated image if exists
    if item.image_filename:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], item.image_filename)
        if os.path.exists(image_path):
            os.remove(image_path)
    
    db.session.delete(item)
    db.session.commit()
    
    flash('Item deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

# Initialize database
def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)