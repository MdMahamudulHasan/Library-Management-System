# Library Management System

This is a web-based Library Management System built using **HTML**, **CSS**, **JavaScript**, **Django**, and **SQLite3** for database management. It is designed for learning purposes and demonstrates how to manage books, student accounts, and staff operations in a library system.

## Purpose
This project was developed as part of my **5th semester** university coursework. The primary goal is to demonstrate my ability to build a functional library management system, based on instructions provided by my course teacher. It showcases the key concepts learned during the course, including user account management, book booking systems, and staff roles.

## Features
### **Student App**:
- **Account Creation & Login**: Students can create an account, log in, and book books.
- **Booking Requests**: Students can send booking requests for books and check their booking status.
- **Profile Management**: Students can view and update their profile, including changing their profile picture.
- **Booking Status**: Students can see if a book has been confirmed, borrowed, or returned.

### **Staff App**:
- **Login**: Staff accounts are created by the admin, and staff can log in to manage book requests.
- **Manage Bookings**: Staff can confirm, decline, or mark books as returned for student booking requests.
- **Profile**: Staff can view their profile information.

### **Books App**:
- **Book Management**: Only staff can add books to the system.
- **Book Display**: Anyone can view books, but only logged-in students can make booking requests.
- **Book Details**: Clicking on a book will show detailed information, including a downloadable PDF if available.

### **General Features**:
- **Homepage**: A basic homepage with navigation to the main features.
- **Team Members Page**: Information about the project team.
- **Device Compatibility**: The UI is only optimized for desktop/laptop screen widths (not responsive to mobile devices).

## Installation Instructions
To set up and run this project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
