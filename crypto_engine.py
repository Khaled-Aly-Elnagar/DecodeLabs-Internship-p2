import customtkinter as ctk

# إعدادات المظهر الاحترافي
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CyberCryptoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("DecodeLabs - Cryptographic Engine (Project 2)")
        self.geometry("700x600")
        self.resizable(False, False)

        # --- العنوان ---
        self.title_label = ctk.CTkLabel(
            self, 
            text="Advanced Caesar Cipher Engine", 
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=20)

        # --- منطقة مفتاح التشفير ---
        self.key_frame = ctk.CTkFrame(self)
        self.key_frame.pack(pady=10)
        
        self.key_label = ctk.CTkLabel(
            self.key_frame, 
            text="Shift Key (Integer):", 
            font=("Arial", 14)
        )
        self.key_label.pack(side="left", padx=10)
        
        self.key_entry = ctk.CTkEntry(self.key_frame, width=100)
        self.key_entry.pack(side="left", padx=10)
        self.key_entry.insert(0, "3") # قيمة افتراضية
        self.key_entry.bind("<KeyRelease>", self.process_text)

        # --- أزرار اختيار الوضع (تشفير / فك تشفير) ---
        self.mode_var = ctk.StringVar(value="encrypt")
        self.mode_frame = ctk.CTkFrame(self)
        self.mode_frame.pack(pady=10)
        
        self.encrypt_radio = ctk.CTkRadioButton(
            self.mode_frame, text="Encrypt", 
            variable=self.mode_var, value="encrypt", 
            command=self.process_text
        )
        self.encrypt_radio.pack(side="left", padx=20)
        
        self.decrypt_radio = ctk.CTkRadioButton(
            self.mode_frame, text="Decrypt", 
            variable=self.mode_var, value="decrypt", 
            command=self.process_text
        )
        self.decrypt_radio.pack(side="left", padx=20)

        # --- منطقة إدخال النص ---
        self.input_label = ctk.CTkLabel(self, text="Plaintext / Ciphertext Input:", font=("Arial", 14, "bold"))
        self.input_label.pack(pady=(10, 0))
        
        self.input_textbox = ctk.CTkTextbox(self, width=600, height=150)
        self.input_textbox.pack(pady=10)
        self.input_textbox.bind("<KeyRelease>", self.process_text) # تنفيذ فوري عند الكتابة

        # --- منطقة عرض النتائج ---
        self.output_label = ctk.CTkLabel(self, text="Processed Output:", font=("Arial", 14, "bold"))
        self.output_label.pack(pady=(10, 0))
        
        # استخدام اللون الأخضر للنص المشفر لإعطاء طابع سيبراني، مع قفل التعديل
        self.output_textbox = ctk.CTkTextbox(
            self, width=600, height=150, 
            state="disabled", fg_color="#121212", text_color="#00FF41", font=("Courier", 14, "bold")
        )
        self.output_textbox.pack(pady=10)

    # --- المنطق الرياضي الصارم الذي قمت أنت ببنائه ---
    def caesar_cipher(self, text, shift, mode='encrypt'):
        result = ""
        if mode == 'decrypt':
            shift = -shift
        
        for char in text:
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += char
        return result

    # --- المحرك الرئيسي لمعالجة الأحداث ---
    def process_text(self, event=None):
        raw_text = self.input_textbox.get("1.0", "end-1c")
        raw_key = self.key_entry.get()
        mode = self.mode_var.get()

        # معالجة ثغرة الانهيار: منع المستخدم من إدخال حروف في خانة الأرقام
        try:
            shift_key = int(raw_key) if raw_key else 0
        except ValueError:
            self.update_output("[!] FATAL ERROR: Shift key must be a valid numerical integer.")
            self.output_textbox.configure(text_color="red")
            return

        self.output_textbox.configure(text_color="#00FF41") # إعادة اللون الأخضر في حالة النجاح
        
        # تمرير البيانات لدالة التشفير
        processed_text = self.caesar_cipher(raw_text, shift_key, mode)
        self.update_output(processed_text)

    # --- دالة مساعدة لتحديث الشاشة بأمان ---
    def update_output(self, text):
        self.output_textbox.configure(state="normal") # فتح القفل
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.insert("1.0", text)
        self.output_textbox.configure(state="disabled") # إعادة القفل لمنع العبث

if __name__ == "__main__":
    app = CyberCryptoApp()
    app.mainloop()