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

تثبيت المكتبات المطلوبة (Install Dependencies):

Bash
pip install customtkinter
تشغيل المحرك (Run the Application):

Bash
python crypto_engine.py
🧮 Mathematical Logic
يعتمد المحرك على التطبيق الرياضي الصارم لمعامل باقي القسمة (Modulo 26) لضمان بقاء الحروف داخل النطاق الأبجدي دون إنتاج رموز مشوهة في جدول ASCII:

$$ \text{Cipher Character} = \text{chr}((\text{ord}(\text{char}) - \text{Base} + \text{shift}) \pmod{26} + \text{Base}) $$

يتم فحص الحرف ديناميكياً وتحديد نقطة الأساس (Base)؛ بقيمة 65 للحروف الكبيرة (A-Z) وقيمة 97 للحروف الصغيرة (a-z).

🛡️ Robustness Demo (Edge Cases Handled)
Input: 123ewdc vvc!

Shift Key: 3

Output: 123hzgf yyf!
(يلاحظ صمود الأرقام، المسافات، وعلامة التعجب وتجاوزها لعملية التعديل الرياضي بنجاح، بينما تم تشفير الحروف فقط بدقة).

Author: Khaled Aly Aly Elnagar
