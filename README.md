# Advanced Cryptographic Engine - Caesar Cipher (Project 2)

## 📌 Overview
محرك تشفير متقدم يعتمد على خوارزمية **قيصر (Caesar Cipher)** الكلاسيكية، مدمج بواجهة رسومية مظلمة (Dark-themed GUI) متطورة باستخدام مكتبة `CustomTkinter`. تم بناء هذا النظام كجزء من تطوير مهارات هندسة البرمجيات الأمنية، مع التركيز الصارم على استقرار النظام (System Stability)، ومعالجة الاستثناءات (Exception Handling)، وسد ثغرات الانهيار الناتجة عن مدخلات المستخدم غير المتوقعة.

## 🚀 Features
* **Real-time Processing (المعالجة اللحظية):** يتم تشفير أو فك تشفير النصوص فورياً أثناء الكتابة (Dynamic Event Binding) دون الحاجة لأزرار تنفيذ تقليدية.
* **Input Validation & Crash Prevention:** نظام معالجة أخطاء ذكي يعتمد على كتل `try-except` لمنع انهيار البرنامج (Application Crash) في حال إدخال قيم غير رقمية في خانة مفتاح الإزاحة (`Shift Key`).
* **Character Immunity (حصانة الهيكل):** الحفاظ التام على هيكل النص الأصلي (الأرقام، المسافات، وعلامات الترقيم والرموز) وتوجيه التشفير حصراً للحروف الأبجدية الإنجليزية.
* **DRY Architecture:** دمج منطق التشفير وفك التشفير في دالة رياضية موحدة تعتمد على التلاعب بقيمة الإزاحة السلبية لمنع تكرار الأكواد (Don't Repeat Yourself).
* **Cybersecurity Look & Feel:** واجهة رسومية ذات طابع سيبراني مظلم، مع تلوين المخرجات باللون الأخضر المشفر وقفل صندوق المخرجات تلقائياً لمنع تلاعب المستخدم بالبيانات الناتجة.

## 🛠️ Tech Stack
* **Language:** Python 3.13+
* **GUI Library:** CustomTkinter (Advanced Tkinter Wrapper)
* **Environment:** Clean Production Environment

## 💻 Installation & Setup

لضمان تشغيل المحرك دون تضارب في البيئات البرمجية، اتبع الخطوات التالية:

1. **استنساخ المستودع (Clone the Repository):**
   ```bash
   git clone [https://github.com/Khaled-Aly-Elnagar/DecodeLabs-Internship-p2.git](https://github.com/Khaled-Aly-Elnagar/DecodeLabs-Internship-p2.git)
   cd DecodeLabs-Internship-p2
