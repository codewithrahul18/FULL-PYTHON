'''
 # string
name = "RC"
greeting = "hello"
print(name)
print(greeting)

# Multiline string

message =""" hello RC you are awesome
and you are going to be great in programing and you will make a lot of money and you are sexy boy !"""
print(message)

# string indexing and slicing
text = "RAHUL"; print(
    text,
    text[0],
    text[1],
    text[3],
    text[4],
    text[-1],
    text[-2],
    text[-3],
    text[-4],
    text[-5],
    text[0:1],
    text[1:2],
    text[2:3],
    text[3:5],
    sep="\n"
)



# common string methods

print(
    "rahul".upper(),
    "Rahul".lower(),
    "Rahul".strip(),
    "Rahul".replace("R", "P"),
    "Rahul".split("a"),
    "Rahul".join("18"),
    "Rahul".find("h"),
    "Rahul".count("a"),
    "Rahul".startswith("R"),
    "Rahul".endswith("l"),
    "rahul".isdigit(),
    "Rahul".isalpha(),
    "Rahul".islower(),
    "RAHUL".isupper(),
    "Rahul".isalnum(),
    sep="\n"
)


# string Formatting (f-strings)

name = "RC"
age = 1500
print(f"My name is {name} and I am {age} years old.")


# operators in python

a = 16
b = 2
print(
    a + b,
    a - b,
    a * b,
    a / b,
    a // b,
    a % b,
    a ** b,
    sep="\n"
)

# comparison operators
a = 16
b = 2
print(
    a==b, 
    a!=b,
    a>b,
    a<b,
    a>=b,
    a<=b,
    sep="\n"
)


# logical operators
a = 16
b = 2
print(
    a and b,
    a or b,
    not a,
    not b,
    sep ="\n"
)

# Bitwise operators
a = 16
b = 2
print(
    a & b,
    a | b,
    ~a,
    a ^ b,
    a << b,
    a >> b,
    sep="\n"
)

# Assigment operators
a = 16
b = 2

# demonstrate augmented assignments on copies so original 'a' stays the same for each example
a_add = a
a_add += b

a_sub = a
a_sub -= b

a_mul = a
a_mul *= b

a_div = a
a_div /= b

a_floordiv = a
a_floordiv //= b

a_mod = a
a_mod %= b

a_pow = a
a_pow **= b

print(
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               a_add,
    a_add,
    a_sub,
    a_mul,
    a_div,
    a_floordiv,
    a_mod,
    a_pow,
    sep="\n"
)

# membership operators
text = "RAHUL"
print(
    "R" in text,
    "X" in text,
    "A" not in text,
    "Y" not in text,
    sep="\n"
)


# Taking input from the user

name = input("Enter your name:")
age = input("Enter your age:")
sex = input("Enter your sex (M/F):")
class_name = input("Enter your class:")
marks = input("Enter your marks:")
percentage = input("Enter your percentage:")
print(f"Name: {name}\nAge: {age}\nSex: {sex}\nClass: {class_name}\nMarks: {marks}\nPercentage: {percentage}")

# TYPE CONVERSION
name = int(input("Enter your name:"))
age = int(input("Enter your age:"))
sex = input("Enter your sex (M/F):")
class_name = input("Enter your class:")
marks = int(input("Enter your marks:"))
percentage = float(input("Enter your percentage:"))
print(f"Name: {name}\nAge: {age}\nSex: {sex}\nClass: {class_name}\nMarks: {marks}\nPercentage: {percentage}")



# operators precedence

result = 16 + 2 * 16/2 - 16
print(result)
result = (16 + 2) * (16/2) - 16
print(result)
result = 16 + (2 * 16)/(2 - 16)
print(result)


# if else statements
x = 16 
if x > 2:
    print("x is greater than 2")
else:
    print("x is less than or equal to 2")

# if elif - else statement
x = 16
if x == 16:
    print("x is equal to 16")
elif 2 < x < 18:
    print("x is greater than 2 but less than 18")
elif x > 2:
    print("x is greater than 2")
else:
    print("x is less than or equal to 2")


# using if - else in data science

age = 25

if age < 18:
    category = "Minor"
elif age < 65:
    category = "Adult"
else:
    category = "Senior Citizen"

print("Category:", category)


# Match cade statements 

def http_status_code(status_code):
    match status_code:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case 502:
            return "Bad Gateway"
        case 503:
            return "Service Unavailable"
        case _:
            return "Unknown Status Code"


# -------- Input Handling --------
try:
    code = int(input("Enter HTTP status code: "))
    result = http_status_code(code)
    print(f"Status {code}: {result}")

except ValueError:
    print("Error: Please enter a valid numeric HTTP status code.")


 # ✅ HTTP Status Code System with Logging & Monitoring
import logging
from datetime import datetime

# =========================
# 1. LOGGING CONFIGURATION
# =========================
logging.basicConfig(
    filename="http_status.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# =========================
# 2. CORE LOGIC
# =========================
def http_status_code(status_code):
    match status_code:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case 502:
            return "Bad Gateway"
        case 503:
            return "Service Unavailable"
        case _:
            return "Unknown Status Code"

# =========================
# 3. MONITORING COUNTERS
# =========================
status_counter = {
    "success": 0,
    "client_error": 0,
    "server_error": 0,
    "unknown": 0
}

# =========================
# 4. INPUT LOOP (SERVER-LIKE)
# =========================
while True:
    try:
        code = input("\nEnter HTTP status code (or 'exit'): ")

        if code.lower() == "exit":
            print("Shutting down monitoring system...")
            logging.info("System shutdown by user")
            break

        code = int(code)
        message = http_status_code(code)

        # Classification
        if 200 <= code < 300:
            status_counter["success"] += 1
            logging.info(f"{code} - {message}")
        elif 400 <= code < 500:
            status_counter["client_error"] += 1
            logging.warning(f"{code} - {message}")
        elif 500 <= code < 600:
            status_counter["server_error"] += 1
            logging.error(f"{code} - {message}")
        else:
            status_counter["unknown"] += 1
            logging.warning(f"{code} - Unknown status received")

        print(f"Status {code}: {message}")

    except ValueError:
        print("Invalid input. Enter a numeric HTTP status code.")
        logging.error("Invalid (non-numeric) input received")

# =========================
# 5. FINAL MONITORING REPORT
# =========================
print("\n--- Server Monitoring Summary ---")
for k, v in status_counter.items():
    print(f"{k.replace('_',' ').title()}: {v}")

logging.info(f"Final Status Report: {status_counter}")

import logging
import hashlib
from datetime import datetime

# =========================
# 1. LOGGING CONFIG
# =========================
logging.basicConfig(
    filename="login_system.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# =========================
# 2. USER DATABASE (SIMULATED)
# Passwords are stored as HASHES (REAL PRACTICE)
# =========================
users_db = {
    "rc": hashlib.sha256("rc@123".encode()).hexdigest(),
    "admin": hashlib.sha256("admin@123".encode()).hexdigest(),
    "user1": hashlib.sha256("user@123".encode()).hexdigest()
}

# =========================
# 3. LOGIN METRICS (MONITORING)
# =========================
metrics = {
    "success": 0,
    "failed": 0,
    "blocked": 0
}

MAX_ATTEMPTS = 3
failed_attempts = {}

# =========================
# 4. AUTHENTICATION LOGIC
# =========================
def authenticate(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username not in users_db:
        return False, "User does not exist"

    if users_db[username] != hashed_password:
        return False, "Incorrect password"

    return True, "Login successful"

# =========================
# 5. LOGIN SYSTEM (REAL FLOW)
# =========================
while True:
    username = input("\nUsername (or 'exit'): ")

    if username.lower() == "exit":
        print("System shutting down...")
        logging.info("Login system shutdown")
        break

    # Block user after multiple failures
    if failed_attempts.get(username, 0) >= MAX_ATTEMPTS:
        print("Account temporarily blocked.")
        metrics["blocked"] += 1
        logging.warning(f"Blocked login attempt for user: {username}")
        continue

    password = input("Password: ")

    success, message = authenticate(username, password)

    if success:
        print("✅ Access Granted")
        metrics["success"] += 1
        failed_attempts[username] = 0
        logging.info(f"Successful login: {username}")

    else:
        print("❌ Access Denied:", message)
        metrics["failed"] += 1
        failed_attempts[username] = failed_attempts.get(username, 0) + 1
        logging.error(f"Failed login for {username} | Reason: {message}")

# =========================
# 6. FINAL SECURITY REPORT
# =========================
print("\n--- Login System Report ---")
for k, v in metrics.items():
    print(f"{k.title()} Attempts: {v}")

logging.info(f"Final Metrics: {metrics}")
 


# string formatiing and f strings

name  = "RC"
age = 1500
print("My Name is {} and I am {} years old".format(name, age))
  
# using f strings
name = "RC" 
age = 1500 
print(f"My name is {name} and I am {age} years old.")

# formatting Numbers
pi = 3.141592653589793
print(f"pi rounded to 2 decimal places:{pi:.2f}")
print(f"pi rounded to 5 decimal places:{pi:.16f}")

# Padding and Alignment
print(f"{'RC' :<10}") # Left - align
print(f"{'RC':>10}") # Right - align
print(f"{'RC':^10}") # Center - align

# 🎨 custom padding characters
print(f"{'RC':*<10}")   # RC********
print(f"{'RC':*>10}")   # ********RC
print(f"{'RC':*^10}")   # ****RC****

# 📊 Numeric Alignment
print(f"{16:<10}")
print(f"{16:>10}")
print(f"{16:^10}")


# Loop in python 
# 1 -  fOR lOOP
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# using range ()
for i in range(16):
    print(i)

# 2 - While LOOP
count = 0
while count < 16:
    print(count)
    count += 1

# Loop Control Srtatements 
for i in range(16):
    if i == 2:
        break  # stop the loop at 2
    print(i) 


# common list methods in python
my_list = ["RC", "RAHUL", "RC PYTHON", "RC CODER"]

print("Initial List:", my_list, sep="\n")

my_list.append("codewithRC")
print("\nAfter append():", my_list)

my_list.extend(["hello", "RCCODER"])
print("\nAfter extend():", my_list)

my_list.insert(2, "NEW ELEMENT")
print("\nAfter insert():", my_list)

my_list.remove("RAHUL")
print("\nAfter remove():", my_list)

removed_item = my_list.pop()
print("\nAfter pop():", my_list)
print("Popped item:", removed_item)

my_list.sort()
print("\nAfter sort():", my_list)

print("\nIndex of 'RC':", my_list.index("RC"))

print("Count of 'RC PYTHON':", my_list.count("RC PYTHON"))

my_list.reverse()
print("\nAfter reverse():", my_list)

my_list.clear()
print("\nAfter clear():", my_list)



# AI Project: Smart Recommendation Engine

class RecommendationEngine:

    def __init__(self, user_interactions):
        self.user_interactions = user_interactions
        self.weights = {}
        self.probabilities = {}

    def train(self):
        total = len(self.user_interactions)
        for interest in set(self.user_interactions):
            count = self.user_interactions.count(interest)
            self.weights[interest] = count
            self.probabilities[interest] = round(count / total, 2)

    def rank(self):
        return sorted(
            self.probabilities.items(),
            key=lambda x: x[1],
            reverse=True
        )

    def recommend(self, top_n=3):
        ranked = self.rank()
        return ranked[:top_n]

    def collaborative_recommend(self, other_users):
        shared_scores = {}
        for user in other_users:
            for interest in user:
                if interest in self.probabilities:
                    shared_scores[interest] = shared_scores.get(interest, 0) + 1
        return sorted(shared_scores.items(), key=lambda x: x[1], reverse=True)


# ---------------- RUN SYSTEM ---------------- #

user_data = ["machine learning", "data science", "python", "deep learning", "AI", "python", "data science"]
engine = RecommendationEngine(user_data)
engine.train()

print("📊 Learned Weights:", engine.weights)
print("\n📈 Learned Probabilities:", engine.probabilities)

print("\n🏆 AI Recommendations:")
for topic, score in engine.recommend():
    print(f"- {topic} (confidence: {score})")

other_users = [
    ["AI", "Python", "Cloud Computing"],
    ["ML", "deep learning", "Python"],
    ["Deep Learning", "Data Science", "ML"]
]

print("\n🤝 Collaborative Recommendations:")
print(engine.collaborative_recommend(other_users))

# “This project implements a probabilistic recommendation engine with collaborative filtering, designed using ML preprocessing principles.”


# Tuples and Tuple Methods
# Empty Tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Tuple with elements
my_tuple = ("RC", "CODEWITHRC", "RC PYTHON", "RC CODER")
print("Tuple with elements:", my_tuple)

# mixed data types
mixed_tuple = (1, "RC", 3.14, True)
print("Mixed Data Types Tuple:", mixed_tuple)

# Single  element tuple (comma is necessary)
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)

# Common Tuple Methods
my_tuple = ("RC", "RAHUL", "RC PYTHON", "RC CODER", "RC")
print("Initial Tuple:", my_tuple)
print("Count of 'RC':", my_tuple.count("RC"))
print("index of 'RC CODER':", my_tuple.index("RC CODER"))

# Tuple characteristic 
# Immutable
my_tuple = ("RC", "CODEWITHRC", "RC CODER")
print("Original Tuple:", my_tuple)
# my_tuple[1] = "NEW VALUE"  # This will raise an error

# Faster than list
import time 
list_example = list(range(1000000))
tuple_example = tuple(range(1000000))
start_time = time.time()
for _ in range(1000000):
    pass
end_time = time.time()
print("Time taken for tuple operations:", end_time - start_time)

# can be used as keys in dictionary
my_dict = {("RC", "CODEWITHRC"): "A tuple as a key"}
print("Dictionary with tuple key:", my_dict)


# Accessing Tuple Elements 
my_tuple = ("RC", "CODEWITHRC", "RC PYTHON", "RC CODER")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slicing:", my_tuple[1:3])

# Tuple Unpacking
name, company, topic = ("RC", "CODEWITHRC", "RC PYTHON")
print("Unpacked values:", name, company, topic)

# Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print("Concatenated tuple:", concatenated)

# Tuple Repetition
repeated = ("RC",) * 3
print("Repeated tuple:", repeated)

# Tuple Methods
my_tuple = ("RC", "CODEWITHRC", "RC PYTHON", "RC CODER", "RC")
print("Count of 'RC':", my_tuple.count("RC"))
print("Index of 'RC CODER':", my_tuple.index("RC CODER"))


# Sets in Python
# Creating a Set
my_set = {"RC", "CODEWITHRC", "RC PYTHON", "RC CODER"}
print("Initial Set:", my_set)

# Set with mixed data types
mixed_set = {"RC", 42, 3.14, True}
print("Mixed Data Types Set:", mixed_set)

# Set with duplicates (automatically removed)
duplicate_set = {"RC", "CODEWITHRC", "RC PYTHON", "RC CODER", "RC", "RC"}
print("Set with Duplicates:", duplicate_set)

# Set characteristic
# Unordered
my_set = {"RC", "CODEWITHRC", "RC PYTHON", "RC CODER"}
print("Unordered Set:", my_set)

# Unchangeable (immutable)
my_set = {"RC", "CODEWITHRC", "RC PYTHON", "RC CODER"}
print("Original Set:", my_set)
# my_set.add("NEW VALUE")  # This will raise an error

#  Common Set Method 
my_list = {"RC", "CODEWITHRC", "RC PYTHON", "RC CODER"}
print("Initial Set:", my_list)
my_list.add("NEW VALUE")
print("After add():", my_list)
my_list.remove("RC")
print("After remove():", my_list)

# Set Operations
set1 = {"RC", "CODEWITHRC", "RC PYTHON", "RC CODER"}
set2 = {"RC", "RAHUL", "RC PYTHON", "RC CODER", "RC"}
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Set Methods
my_set = {"RC", "CODEWITHRC", "RC PYTHON", "RC CODER"}
print("Initial Set:", my_set)
my_set.add("NEW VALUE")
print("After add():", my_set)
my_set.remove("RC")
print("After remove():", my_set)
print("Discard 'RC':", my_set.discard("RC"))
print("Pop:", my_set.pop())
print("Clear:", my_set.clear())

# ==========================================
# SECURE AI LOGIN + OTP (2FA) SYSTEM
# Author: RC
# ==========================================

import hashlib
import random
import time

print("\n=== SECURE AI SYSTEM STARTED ===\n")

# ------------------------------------------
# 1. System Rules (Frozen Set)
# ------------------------------------------

SYSTEM_RULES = frozenset({
    "HASHED_PASSWORDS",
    "MAX_ATTEMPTS_3",
    "OTP_2FA_ENABLED",
    "ACCOUNT_LOCK"
})

print("System Rules:")
for rule in SYSTEM_RULES:
    print("-", rule)

# ------------------------------------------
# 2. Password Hashing Function
# ------------------------------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------------------------------
# 3. OTP Generator
# ------------------------------------------

def generate_otp():
    return random.randint(100000, 999999)

# ------------------------------------------
# 4. Stored Users (Hashed Passwords)
# ------------------------------------------

stored_users = {
    "RC": hash_password("rc@123"),
    "ADMIN": hash_password("admin@456")
}

# ------------------------------------------
# 5. Login System (Password + Attempts)
# ------------------------------------------

MAX_ATTEMPTS = 3
attempts = 0
authenticated = False

print("\n=== LOGIN (STEP 1: PASSWORD) ===")

while attempts < MAX_ATTEMPTS:
    username = input("Username: ")
    password = input("Password: ")

    if username in stored_users and stored_users[username] == hash_password(password):
        print("\n✅ Password Verified")
        authenticated = True
        break
    else:
        attempts += 1
        print(f"❌ Invalid credentials ({attempts}/{MAX_ATTEMPTS})")

if not authenticated:
    print("\n🔒 Account Locked due to multiple failures.")
    exit()

# ------------------------------------------
# 6. OTP Verification (2FA)
# ------------------------------------------

print("\n=== STEP 2: OTP VERIFICATION ===")

otp = generate_otp()
print(f"(Simulation) OTP Sent: {otp}")   # In real life → SMS / Email
otp_time = time.time()

user_otp = int(input("Enter OTP: "))

if user_otp != otp or time.time() - otp_time > 30:
    print("\n❌ OTP Verification Failed")
    exit()

print("\n✅ OTP Verified Successfully")

# ------------------------------------------
# 7. Student Information Input
# ------------------------------------------

print("\n=== STUDENT PROFILE INPUT ===")

name = input("Student Name: ")
age = int(input("Age: "))
marks = float(input("Entrance Exam Marks (out of 100): "))
city = input("City: ")

# ------------------------------------------
# 8. Student Profile Dictionary
# ------------------------------------------

student_profile = {
    "name": name,
    "age": age,
    "marks": marks,
    "city": city
}

# ------------------------------------------
# 9. AI Eligibility Engine
# ------------------------------------------

print("\n=== AI ELIGIBILITY ANALYSIS ===")

if age < 17:
    eligibility = "NOT ELIGIBLE (UNDERAGE)"
elif marks >= 85:
    eligibility = "ELIGIBLE FOR TOP TIER"
elif marks >= 60:
    eligibility = "ELIGIBLE"
else:
    eligibility = "NOT ELIGIBLE (LOW SCORE)"

student_profile["eligibility_status"] = eligibility

# ------------------------------------------
# 10. Scholarship Prediction
# ------------------------------------------

if marks >= 90:
    scholarship = "100% SCHOLARSHIP"
elif marks >= 75:
    scholarship = "50% SCHOLARSHIP"
else:
    scholarship = "NO SCHOLARSHIP"

student_profile["scholarship"] = scholarship

# ------------------------------------------
# 11. Final Secure AI Report
# ------------------------------------------

print("\n=== FINAL AI REPORT ===")
for key, value in student_profile.items():
    print(f"{key.upper():<22} : {value}")

# ------------------------------------------
# 12. System Summary
# ------------------------------------------

print("\n=== SYSTEM SUMMARY ===")
print("Logged-in User :", username)
print("Security      : PASSWORD + OTP (2FA)")
print("Eligibility   :", student_profile["eligibility_status"])
print("Scholarship   :", student_profile["scholarship"])
print("System Status : HIGHLY SECURE")

print("\n✅ SECURE AI SYSTEM WITH 2FA COMPLETED")


# ==========================================
# SECURE LOGIN + CHANGE PASSWORD SYSTEM
# Author: RC
# ==========================================

import hashlib

print("\n=== SECURE SYSTEM STARTED ===\n")

# ------------------------------------------
# Password Hashing Function
# ------------------------------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------------------------------
# Mock Database (Hashed Passwords)
# ------------------------------------------

users_db = {
    "RC": hash_password("rc@123"),
    "ADMIN": hash_password("admin@456")
}

# ------------------------------------------
# Login System
# ------------------------------------------

print("=== LOGIN ===")
username = input("Username: ")
password = input("Password: ")

if username in users_db and users_db[username] == hash_password(password):
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")
    exit()

# ------------------------------------------
# Change Password Option
# ------------------------------------------

choice = input("\nDo you want to change your password? (yes/no): ").lower()

if choice == "yes":
    old_password = input("Enter OLD password: ")

    if users_db[username] != hash_password(old_password):
        print("❌ Old password incorrect")
        exit()

    new_password = input("Enter NEW password: ")
    confirm_password = input("Confirm NEW password: ")

    if new_password != confirm_password:
        print("❌ Passwords do not match")
        exit()

    users_db[username] = hash_password(new_password)
    print("✅ Password changed successfully")

else:
    print("➡️ Password change skipped")

# ------------------------------------------
# Final Security Confirmation
# ------------------------------------------

print("\n=== SYSTEM STATUS ===")
print("User           :", username)
print("Password State : HASHED & SECURE")
print("System Status  : SUCCESS")

print("\n🔒 SECURITY MAINTAINED")


import hashlib
import random
import time
from datetime import datetime

# ==================================================
# Utility Functions
# ==================================================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_otp():
    return random.randint(100000, 999999)

def generate_captcha():
    a, b = random.randint(1, 9), random.randint(1, 9)
    return a, b, a + b

# ==================================================
# Mock Database
# ==================================================

users_db = {
    "RC": hash_password("rc@123"),
    "ADMIN": hash_password("admin@456")
}

login_logs = []

MAX_ATTEMPTS = 3

# ==================================================
# Login System
# ==================================================

print("\n=== 🔐 SECURE AI LOGIN SYSTEM ===\n")

attempts = 0
authenticated = False

while attempts < MAX_ATTEMPTS:
    username = input("Username: ")
    password = input("Password: ")

    if username in users_db and users_db[username] == hash_password(password):
        authenticated = True
        print("✅ Password verified")
        break
    else:
        attempts += 1
        print(f"❌ Invalid credentials ({attempts}/{MAX_ATTEMPTS})")

if not authenticated:
    print("🔒 Account Locked")
    exit()

# ==================================================
# CAPTCHA
# ==================================================

print("\n=== 🤖 CAPTCHA VERIFICATION ===")
x, y, ans = generate_captcha()
captcha_input = int(input(f"Solve: {x} + {y} = "))

if captcha_input != ans:
    print("❌ CAPTCHA failed")
    exit()

print("✅ CAPTCHA verified")

# ==================================================
# OTP (2FA)
# ==================================================

print("\n=== 🔢 OTP VERIFICATION ===")
otp = generate_otp()
print(f"(Simulation) OTP Sent: {otp}")
otp_time = time.time()

user_otp = int(input("Enter OTP: "))

if user_otp != otp or time.time() - otp_time > 30:
    print("❌ OTP failed or expired")
    exit()

print("✅ OTP verified")

# ==================================================
# Login Log
# ==================================================

login_logs.append({
    "user": username,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "status": "SUCCESS"
})

# ==================================================
# Change Password
# ==================================================

choice = input("\nDo you want to change password? (yes/no): ").lower()

if choice == "yes":
    old = input("Old password: ")
    if users_db[username] != hash_password(old):
        print("❌ Old password incorrect")
        exit()

    new = input("New password: ")
    confirm = input("Confirm new password: ")

    if new != confirm:
        print("❌ Password mismatch")
        exit()

    users_db[username] = hash_password(new)
    print("✅ Password updated securely")

# ==================================================
# AI STUDENT ELIGIBILITY ENGINE
# ==================================================

print("\n=== 🎓 AI STUDENT ELIGIBILITY SYSTEM ===")

name = input("Student Name: ")
age = int(input("Age: "))
marks = float(input("Entrance Marks (0–100): "))

if age < 17:
    eligibility = "NOT ELIGIBLE (UNDERAGE)"
elif marks >= 85:
    eligibility = "TOP TIER ELIGIBLE"
elif marks >= 60:
    eligibility = "ELIGIBLE"
else:
    eligibility = "NOT ELIGIBLE"

if marks >= 90:
    scholarship = "100% SCHOLARSHIP"
elif marks >= 75:
    scholarship = "50% SCHOLARSHIP"
else:
    scholarship = "NO SCHOLARSHIP"

# ==================================================
# Final Report
# ==================================================

print("\n=== 📊 FINAL AI REPORT ===")
print(f"Student Name      : {name}")
print(f"Eligibility       : {eligibility}")
print(f"Scholarship       : {scholarship}")
print(f"Logged-in User    : {username}")
print("Security Level    : MAXIMUM")

# ==================================================
# ADMIN PANEL
# ==================================================

if username == "ADMIN":
    print("\n=== 👑 ADMIN PANEL ===")
    print("Registered Users:")
    for user in users_db:
        print("-", user)

    print("\nLogin Logs:")
    for log in login_logs:
        print(log)

# ==================================================
# Hash Demonstration (Hacker Proof)
# ==================================================

print("\n=== 🧪 HASH SECURITY DEMO ===")
demo_pass = "example123"
print("Plain Password :", demo_pass)
print("Hashed Value   :", hash_password(demo_pass))
print("👉 Hash cannot be reversed")

print("\n✅ SYSTEM EXECUTION COMPLETED SUCCESSFULLY")



# ===============================
# Dictionary Methods Example
# ===============================

# Empty dictionary
empty_dict = {}

# Dictionary with key-value pairs
student = {
    "name": "RC",
    "age": 1500,
    "grade": "A"
}

# Using dict() constructor
person = dict(name="RC", age=1500, city="New York")

# print(student["name"], student["age"], student["grade"])
# print(person["name"], person["age"], person["city"])

print(*student.values())
print(*person.values())

# Create a dictionary
student = {
    "name": "RC",
    "age": 1500,
    "grade": "A"
}

print(student)
# Output → {'name': 'RC', 'age': 1500, 'grade': 'A'}


# Access values
print(student["name"])
# Output → RC

print(student.get("age"))
# Output → 1500

print(student.get("height", "Not found"))
# Output → Not found


# Show keys and values
print(student.keys())
# Output → dict_keys(['name', 'age', 'grade'])

print(student.values())
# Output → dict_values(['RC', 1500, 'A'])


# Update value
student["age"] = 2000
print(student)
# Output → {'name': 'RC', 'age': 2000, 'grade': 'A'}


# Add key if not present
student.setdefault("city", "Unknown")
print(student)
# Output → {'name': 'RC', 'age': 2000, 'grade': 'A', 'city': 'Unknown'}


# Remove one item
student.pop("grade")
print(student)
# Output → {'name': 'RC', 'age': 2000, 'city': 'Unknown'}


# Copy dictionary
student_copy = student.copy()
print(student_copy)
# Output → {'name': 'RC', 'age': 2000, 'city': 'Unknown'}


# Clear dictionary
student.clear()
print(student)
# Output → {}


# Print all values in one line
person = dict(name="RC", age=1500, city="New York")
print(*person.values())
# Output → RC 1500 New York


# ==========================================
# Key Properties of Dictionaries
# ==========================================

# 1. Dictionary stores data as key : value pairs
student = {"name": "RC", "age": 1500}
print(student)
# Output → {'name': 'RC', 'age': 1500}


# 2. Keys must be unique
student = {"name": "RC", "name": "Rahul"}
print(student)
# Output → {'name': 'Rahul'}
# (Old value is overwritten)


# 3. Values can be duplicated
student = {"a": 1, "b": 1, "c": 1}
print(student)
# Output → {'a': 1, 'b': 1, 'c': 1}


# 4. Dictionary is mutable (can be changed)
student = {"name": "RC", "age": 1500}
student["age"] = 2000
print(student)
# Output → {'name': 'RC', 'age': 2000}


# 5. Keys must be immutable
valid_dict = {(1, 2): "tuple key"}
print(valid_dict)
# Output → {(1, 2): 'tuple key'}

# invalid_dict = {[1, 2]: "list key"}  ❌ Error


# 6. Dictionary is unordered (no fixed index)
student = {"x": 1, "y": 2, "z": 3}
print(student)
# Output → Order may vary


# 7. Access values using keys, not index
print(student["x"])
# Output → 1

# print(student[0]) ❌ Error


# 8. Dictionary allows mixed data types
mixed = {
    "name": "RC",
    "age": 1500,
    "skills": ["Python", "AI"],
    "active": True
}
print(mixed)
# Output → {'name': 'RC', 'age': 1500, 'skills': ['Python', 'AI'], 'active': True}


# 9. Dictionary can be nested
nested = {
    "student": {
        "name": "RC",
        "age": 1500
    }
}
print(nested)
# Output → {'student': {'name': 'RC', 'age': 1500}}


# 10. Length of dictionary
print(len(nested))
# Output → 1



# ==================================================
# AI RECOMMENDATION SYSTEM
# User History + Dashboard Visualization
# ==================================================

import json
from datetime import datetime

# ---------- STEP 1: USER DATABASE ----------
users = {
    "RC": {
        "interest": "AI",
        "score": 100,
        "history": []   # stores past interactions
    },
    "Rahul": {
        "interest": "Physics",
        "score": 100,
        "history": []
    }
}

# ---------- STEP 2: CONTENT DATABASE ----------
content = {
    "AI": ["Chatbot", "Machine Learning", "Neural Network"],
    "Physics": ["Quantum Mechanics", "Relativity"],
    "Programming": ["Python", "JavaScript"]
}

# ---------- STEP 3: SELECT USER ----------
user = "RC"
interest = users[user]["interest"]

print("User:", user)
print("Current Interest:", interest)

# ---------- STEP 4: RECOMMEND CONTENT ----------
recommendations = content.get(interest, [])
print("\nRecommended Content:", recommendations)

# ---------- STEP 5: USER RATING (1–5 STARS) ----------
rating = 4   # change 1–5
print("\nUser Rating:", rating, "stars")

# ---------- STEP 6: AI LEARNING ----------
if rating >= 4:
    users[user]["score"] += 2
    feedback = "Like"
elif rating == 3:
    feedback = "Neutral"
else:
    users[user]["score"] -= 2
    feedback = "Dislike"

# ---------- STEP 7: SAVE USER HISTORY ----------
interaction = {
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "interest": interest,
    "recommended": recommendations,
    "rating": rating,
    "feedback": feedback
}

users[user]["history"].append(interaction)

print("AI Feedback:", feedback)

# ---------- STEP 8: AUTO-CHANGE INTEREST ----------
if users[user]["score"] < -3:
    for new_interest in content:
        if new_interest != interest:
            users[user]["interest"] = new_interest
            users[user]["score"] = 0
            print("⚠️ Interest changed to:", new_interest)
            break

# ---------- STEP 9: SAVE DATA TO FILE ----------
with open("ai_user_data.json", "w") as file:
    json.dump(users, file, indent=4)

print("\nData saved to ai_user_data.json")

# ---------- STEP 10: DASHBOARD VISUALIZATION ----------
print("\n========== AI DASHBOARD ==========")

for name, data in users.items():
    print("\nUser:", name)
    print(" Interest:", data["interest"])
    print(" Score:", data["score"])
    print(" Interactions:", len(data["history"]))

    for i, h in enumerate(data["history"], start=1):
        print(
            f"  {i}. [{h['time']}] "
            f"Interest: {h['interest']} | "
            f"Rating: {h['rating']} | "
            f"Feedback: {h['feedback']}"
        )

print("\n========== END DASHBOARD ==========")


# ==========================================
# PYTHON FILE SYSTEM – COMPLETE PROGRAM
# ==========================================

import os
from pathlib import Path

print("\n🚀 FILE SYSTEM PROGRAM STARTED\n")

# ------------------------------------------
# FILE PATHS
# ------------------------------------------
text_file = Path("example.txt")
binary_file = Path("data.bin")


# ------------------------------------------
# 1. CHECK IF TEXT FILE EXISTS
# ------------------------------------------
if text_file.exists():
    print("✅ Text file already exists")
else:
    print("❌ Text file does not exist")


# ------------------------------------------
# 2. WRITE MULTIPLE LINES (TEXT FILE)
# ------------------------------------------
lines = [
    "Even if the world moves faster than you,\n",
    "remember — depth always beats speed.\n",
    "Build yourself silently.\n",
    "One day, your presence will speak louder than noise.\n"
]

with open(text_file, "w") as file:
    file.writelines(lines)

print("✍️ Text file written")


# ------------------------------------------
# 3. APPEND AUTHOR NAME
# ------------------------------------------
with open(text_file, "a") as file:
    file.write("— RC")

print("➕ Author appended")


# ------------------------------------------
# 4. READ TEXT FILE
# ------------------------------------------
with open(text_file, "r") as file:
    print("\n📄 TEXT FILE CONTENT:\n")
    print(file.read())


# ------------------------------------------
# 5. DELETE TEXT FILE
# ------------------------------------------
if text_file.exists():
    os.remove(text_file)
    print("🗑️ Text file deleted")
else:
    print("⚠️ Text file not found")


# ==========================================
# ============ BINARY FILE PART =============
# ==========================================

# ------------------------------------------
# 6. WRITE BINARY FILE
# ------------------------------------------
binary_data = b"RC_BINARY_DATA_101010"

with open(binary_file, "wb") as file:
    file.write(binary_data)

print("\n💾 Binary file written")


# ------------------------------------------
# 7. READ BINARY FILE
# ------------------------------------------
with open(binary_file, "rb") as file:
    data = file.read()
    print("📦 Binary file content:", data)


# ------------------------------------------
# 8. DELETE BINARY FILE
# ------------------------------------------
if binary_file.exists():
    binary_file.unlink()
    print("🗑️ Binary file deleted")
else:
    print("⚠️ Binary file not found")


print("\n✅ FILE SYSTEM PROGRAM FINISHED\n")

 

# Json Module in Python
import json

# json.dumps() - Convert Python object to Json string
import json 
data = {"name": "RC" , "age" : 1500, "city": "New York"} 
json_string = json.dumps(data)
print(json_string)  # output : {"name": "rc", "age": 1500, "city": "New York"}
print(type(json_string)) # <class 'str'>

# json.dump() - Write json data to a file
import json

data = {
    "name": "RC",
    "age": 1500,
    "skills": ["Python", "AI", "Data Science"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON data written successfully!")


# json.load() - Convert json string to Python object :-
import json

# Python → JSON string
data = {"name": "RC", "age": 1500, "city": "New York"}
json_string = json.dumps(data)

# JSON string → Python
python_obj = json.loads(json_string)

print(json_string)
print(python_obj)


# formatting json output
formatting_json = json.dumps (data, indent=4)
print(formatting_json)


# AI App User Configuration & Session Manager
import json
import os

CONFIG_FILE = "user_config.json"

# -------------------------------
# 1️⃣ Create default config
# -------------------------------
def create_default_config():
    return {
        "username": "RC",
        "theme": "dark",
        "language": "en",
        "notifications": True,
        "login_count": 0
    }

# -------------------------------
# 2️⃣ Load config from file
# -------------------------------
def load_config():
    if not os.path.exists(CONFIG_FILE):
        print("Config file not found. Creating default config...")
        save_config(create_default_config())

    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

# -------------------------------
# 3️⃣ Save config to file
# -------------------------------
def save_config(config_data):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config_data, file, indent=4)

# -------------------------------
# 4️⃣ Update user session
# -------------------------------
def update_session(config):
    config["login_count"] += 1
    print(f"Welcome back, {config['username']}!")
    print(f"Login count: {config['login_count']}")

# -------------------------------
# 5️⃣ Simulate API JSON response
# -------------------------------
def fake_api_response():
    return '{"status": "success", "credits": 120, "plan": "pro"}'

# -------------------------------
# 6️⃣ Main App Logic
# -------------------------------
def main():
    config = load_config()
    update_session(config)

    # Parse API JSON string
    api_json = fake_api_response()
    api_data = json.loads(api_json)

    print("\nAPI Data:")
    print(api_data)

    # Update config based on API
    if api_data["plan"] == "pro":
        config["notifications"] = True

    save_config(config)
    print("\nConfig saved successfully!")

# -------------------------------
# Run App
# -------------------------------
main()




# Defining a class and Creating an object

# Creatin a Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"


car1 = Car("Tesla", "Model S")
print(car1)




# =====================================================
# CAR MANAGEMENT SYSTEM
# =====================================================

# ======================================================
# BASE CLASS
# ======================================================

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_on = False
        self.total_distance = 0

    def start_engine(self):
        self.engine_on = True
        return f"{self.brand} {self.model} engine started."

    def stop_engine(self):
        self.engine_on = False
        return f"{self.brand} {self.model} engine stopped."

    def status(self):
        return f"{self.brand} {self.model} | Distance: {self.total_distance} km"


# ======================================================
# PETROL CAR (INHERITANCE)
# ======================================================

class PetrolCar(Car):
    def __init__(self, brand, model, fuel_capacity):
        super().__init__(brand, model)
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity

    def drive(self, distance):
        fuel_needed = distance * 0.08  # AI consumption logic
        if fuel_needed > self.fuel_level:
            return "❌ Not enough fuel"

        self.fuel_level -= fuel_needed
        self.total_distance += distance
        return f"🚗 Driven {distance} km | Fuel left: {self.fuel_level:.2f} L"

    def refuel(self, fuel):
        self.fuel_level = min(self.fuel_capacity, self.fuel_level + fuel)
        return "⛽ Fuel tank full"

    def ai_prediction(self):
        return f"🤖 AI predicts range: {self.fuel_level / 0.08:.0f} km"


# ======================================================
# ELECTRIC CAR (INHERITANCE)
# ======================================================

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        self.battery_level = battery_capacity

    def drive(self, distance):
        energy_needed = distance * 0.15
        if energy_needed > self.battery_level:
            return "❌ Battery too low"

        self.battery_level -= energy_needed
        self.total_distance += distance
        return f"⚡ Driven {distance} km | Battery left: {self.battery_level:.2f} kWh"

    def charge(self):
        self.battery_level = self.battery_capacity
        return "🔋 Battery fully charged"

    def ai_prediction(self):
        return f"🤖 AI predicts range: {self.battery_level / 0.15:.0f} km"


# ======================================================
# ANALYTICS DASHBOARD
# ======================================================

def dashboard(cars):
    print("\n📊 CAR ANALYTICS DASHBOARD")
    print("-" * 35)
    for car in cars:
        print(car.status())
    print("-" * 35)


# ======================================================
# MENU SYSTEM
# ======================================================

def menu():
    print("""
1. Drive Car
2. Refuel / Recharge
3. Start Engine
4. Stop Engine
5. AI Range Prediction
6. Dashboard
7. Exit
""")


# ======================================================
# MAIN PROGRAM
# ======================================================

car1 = PetrolCar("Toyota", "Fortuner", 80)
car2 = ElectricCar("Tesla", "Model 3", 75)

cars = [car1, car2]

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        car = cars[int(input("Select car (0-Petrol, 1-Electric): "))]
        dist = int(input("Enter distance: "))
        print(car.drive(dist))

    elif choice == "2":
        car = cars[int(input("Select car (0-Petrol, 1-Electric): "))]
        if isinstance(car, PetrolCar):
            fuel = int(input("Fuel amount: "))
            print(car.refuel(fuel))
        else:
            print(car.charge())

    elif choice == "3":
        car = cars[int(input("Select car: "))]
        print(car.start_engine())

    elif choice == "4":
        car = cars[int(input("Select car: "))]
        print(car.stop_engine())

    elif choice == "5":
        car = cars[int(input("Select car: "))]
        print(car.ai_prediction())

    elif choice == "6":
        dashboard(cars)

    elif choice == "7":
        print("👋 System Closed")
        break

    else:
        print("❌ Invalid option")


        


# ============================================
# RC BANK ACCOUNT SYSTEM
# 3. Demonstrating Encapsulation (Data Hiding)
# ============================================

class BankAccount:
    def __init__(self, balance):
        # Private attribute (Data Hiding)
        self.__balance = balance

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful: ${amount:,}")
        else:
            print("Invalid deposit amount!")

    # Optional: withdrawal method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal successful: ${amount:,}")
        else:
            print("Insufficient balance or invalid amount!")


# ============================================
# USING ENCAPSULATION
# ============================================

# RC's Bank Account with 100 Trillion Dollars
account = BankAccount(100_000_000_000_000)

# Deposit 1 Trillion Dollars
account.deposit(1_000_000_000_000)

# Display balance securely
print("RC Bank Balance:", f"${account.get_balance():,}")



# ==================================================
# RC BANK PROFILE SYSTEM
# Demonstrating Encapsulation + Profile Display
# ==================================================

class BankAccount:
    def __init__(self, name, account_type, city, bank_name, balance):
        self.__name = name                  # Private
        self.__account_type = account_type  # Private
        self.__city = city                  # Private
        self.__bank_name = bank_name        # Private
        self.__balance = balance            # Private

    # Getter methods
    def get_profile(self):
        return {
            "Name": self.__name,
            "Account Type": self.__account_type,
            "City": self.__city,
            "Bank": self.__bank_name,
            "Balance": f"${self.__balance:,}"
        }

    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # Secure balance access
    def get_balance(self):
        return self.__balance


# ==================================================
# RC BANK ACCOUNT CREATION
# ==================================================

rc_account = BankAccount(
    name="RC",
    account_type="Ultra Elite Global Account",
    city="New York City",
    bank_name="RC International Bank",
    balance=100_000_000_000_000  # 100 Trillion
)

# Deposit 1 Trillion
rc_account.deposit(1_000_000_000_000)

# Display Profile
profile = rc_account.get_profile()

print("\n🏦 RC BANK ACCOUNT PROFILE")
print("-" * 40)
for key, value in profile.items():
    print(f"{key:<15}: {value}")
print("-" * 40)
 

# Example of Single Inheritance

class Animal:
    def speak(self):
        return "Animal makes a sound"

# Inheriting from Animal
class Lion(Animal):
    def speak(self):
        return "Roar"

# 4. Multiple Inheritance
# Parent Class 1
class Phone:
    def call(self):
        return "Making a phone call 📞"

# Parent Class 2
class Camera:
    def take_photo(self):
        return "Taking a photo 📸"

# Child Class (Multiple Inheritance)
class Smartphone(Phone, Camera):
    pass

# Creating object
my_phone = Smartphone()

# Accessing methods from both parent classes
print(my_phone.call())        # Output: Making a phone call 📞
print(my_phone.take_photo())  # Output: Taking a photo 📸


# ============================
# Authentication Module
# ============================
class AuthenticationSystem:
    def login(self, username):
        return f"[AUTH] User '{username}' logged in successfully 🔐"

    def logout(self, username):
        return f"[AUTH] User '{username}' logged out safely 🚪"


# ============================
# Transaction Module
# ============================
class TransactionSystem:
    def deposit(self, amount):
        return f"[TXN] Deposit successful: ${amount:,} 💰"

    def withdraw(self, amount):
        return f"[TXN] Withdrawal successful: ${amount:,} 🏧"


# ============================
# Online Banking User
# (Multiple Inheritance)
# ============================
class OnlineBankingUser(AuthenticationSystem, TransactionSystem):
    pass


# ============================
# Real Usage (Enterprise Scale)
# ============================
user = OnlineBankingUser()

amount = 100_000_000_000_000  # 100 Trillion Dollars

print(user.login("RC"))
print(user.deposit(amount))
print(user.withdraw(amount))
print(user.logout("RC"))


# method Overriding Example
class Bird:
    def fly(self):
        return "Birds Can fly"
        
class Penguin(Bird):
    def fly(self):
        return "Penguins Cannot fly"
    
bird = Bird()
penguin = Penguin()

print(bird.fly()) # output : Birds Can fly
print(penguin.fly()) # output : Penguins Cannot fly



# 6. Abstraction (Hiding Implementation Details) give me real world example 
from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):

    def start(self):
        print("Car engine started with key")

    def stop(self):
        print("Car stopped using brakes")


class Bike(Vehicle):

    def start(self):
        print("Bike started with kick")

    def stop(self):
        print("Bike stopped using hand brakes")
car = Car()
bike = Bike()

car.start()
car.stop()

bike.start()
bike.stop()



from abc import ABC, abstractmethod
import random
import datetime

# =====================================================
# ABSTRACT ATM INTERFACE (WHAT USER CAN DO)
# =====================================================
class ATM(ABC):

    @abstractmethod
    def authenticate_pin(self, pin):
        pass

    @abstractmethod
    def verify_otp(self, otp):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# =====================================================
# REAL BANK SYSTEM (IMPLEMENTATION HIDDEN)
# =====================================================
class SmartBankATM(ATM):

    def __init__(self, name, balance, pin):
        self.__name = name
        self.__balance = balance
        self.__pin = pin
        self.__pin_verified = False
        self.__otp_verified = False
        self.__generated_otp = None
        self.__transactions = []

    # ---------------- PIN AUTHENTICATION ----------------
    def authenticate_pin(self, pin):
        if pin == self.__pin:
            self.__pin_verified = True
            self.__send_otp()
            print("✅ PIN verified. OTP sent to registered mobile number.")
        else:
            print("❌ Incorrect PIN")

    # ---------------- OTP GENERATION (SMS SIMULATION) ----------------
    def __send_otp(self):
        self.__generated_otp = random.randint(100000, 999999)
        print(f"📩 SMS OTP (simulation): {self.__generated_otp}")

    # ---------------- OTP VERIFICATION ----------------
    def verify_otp(self, otp):
        if otp == self.__generated_otp:
            self.__otp_verified = True
            print("✅ OTP verified. Access granted.")
        else:
            print("❌ Invalid OTP")

    # ---------------- SECURITY CHECK ----------------
    def __security_check(self):
        if not (self.__pin_verified and self.__otp_verified):
            raise PermissionError("🔒 Authentication required (PIN + OTP)")

    # ---------------- AI FRAUD DETECTION ----------------
    def __fraud_detection(self, amount):
        if amount > 1_000_000_000_000:  # 1 trillion
            print("⚠️ AI ALERT: Suspicious transaction detected")
            return True
        return False

    # ---------------- CHECK BALANCE ----------------
    def check_balance(self):
        self.__security_check()
        print(f"👤 Account Holder: {self.__name}")
        print(f"💰 Balance: ₹{self.__balance:,}")

    # ---------------- DEPOSIT ----------------
    def deposit(self, amount):
        self.__security_check()

        if self.__fraud_detection(amount):
            print("❌ Deposit blocked by AI system")
            return

        self.__balance += amount
        self.__log("Deposit", amount)
        print(f"✅ ₹{amount:,} deposited successfully")

    # ---------------- WITHDRAW ----------------
    def withdraw(self, amount):
        self.__security_check()

        if self.__fraud_detection(amount):
            print("❌ Withdrawal blocked by AI system")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            self.__log("Withdraw", amount)
            print(f"✅ ₹{amount:,} withdrawn successfully")
        else:
            print("❌ Insufficient balance")

    # ---------------- TRANSACTION LOG ----------------
    def __log(self, tx_type, amount):
        self.__transactions.append({
            "type": tx_type,
            "amount": amount,
            "time": datetime.datetime.now()
        })


# =====================================================
# REAL LIFE USAGE (RC)
# =====================================================

# Initial data
account_holder = "RC"
initial_balance = 100_000_000_000_000   # 100 trillion
pin = 1234

atm = SmartBankATM(account_holder, initial_balance, pin)

# Authentication flow
atm.authenticate_pin(1234)
otp_input = int(input("Enter OTP: "))
atm.verify_otp(otp_input)

# Banking operations
atm.check_balance()
atm.deposit(500_000_000_000)     # 500 billion
atm.withdraw(100_000_000_000)    # 100 billion
atm.check_balance()




# Magic Methods (Dunder Methods)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):          # String representation
        return f"Book: {self.title}"

    def __len__(self):          # Behavior for len()
        return self.pages

# 8. Class Vs Static Methods
# Creating object
book = Book("Python Basics", 300)

# Using magic methods
print(str(book))   # Output: Book: Python Basics
print(len(book))   # Output: 300

class Example:
    class_var = "I am a class variable"

    # Instance Method
    def instance_method(self):
        return "Instance Method"

    # Class Method
    @classmethod
    def class_method(cls):
        return cls.class_var

    # Static Method
    @staticmethod
    def static_method():
        return "Static Method"


# Creating object
obj = Example()

# Calling methods
print(obj.instance_method())      # Output: Instance Method
print(Example.class_method())     # Output: I am a class variable
print(Example.static_method())    # Output: Static Method



# List Comprehension 

#  1. Create a list of Squares 
squares = [x**2 for x in range(5)]
print(squares) # output : [0, 1, 4, 9, 16]

#  2. Filtering even number
evens = [ x for x in range(10) if x%2==0]
print(evens)  # output : [0, 2, 4, 6, 8]

# 3. Replacing even no. with "Even" and  add no. with "odd"
number = ["Even" if x %2==0 else "odd" for x in range(5)]
print(number) # output : ['Even', 'odd', 'Even', 'odd', 'Even']

# 4. creating pairsfrom two lists
pairs= [(x,y) for x in range(2) for y in range(3) ]
print(pairs) # output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

#  5. Converting a list of strings to uppercase

words = ["hello", "world", "RC"]

upper_words = [w.upper() for w in words]

print(upper_words) # output: ['HELLO', 'WORLD', 'RC']

# 6. Flattening a 2D  list 
matrix = [[1, 2], [3, 4], [5, 6]]

flattened = [num for row in matrix for num in row]

print(flattened) # output: [1, 2, 3, 4, 5, 6]

# 7. Set Comprehension 
unique_numbers = { x for x in [1, 2, 3, 4, 4]}
print(unique_numbers) # output: {1, 2, 3, 4}

# Dictionar Comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 8. when to use list Comprehensions 

print("\n--- 1. Simple Transformation ---")
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print("Squares:", squares)
# Output: [1, 4, 9, 16, 25]


print("\n--- 2. Filtering Data ---")
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even Numbers:", even_numbers)
# Output: [2, 4, 6]


print("\n--- 3. Transformation + Filtering ---")
numbers = [-5, -2, 0, 3, 7]
positive_squares = [n * n for n in numbers if n > 0]
print("Positive Squares:", positive_squares)
# Output: [9, 49]


print("\n--- 4. Flattening a 2D List ---")
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened List:", flattened)
# Output: [1, 2, 3, 4, 5, 6]


print("\n--- 5. Applying a Function ---")
names = ["rahul", "rc", "python"]
upper_names = [name.upper() for name in names]
print("Uppercase Names:", upper_names)
# Output: ['RAHUL', 'RC', 'PYTHON']


print("\n--- 6. Conditional Expression (if-else) ---")
numbers = [1, 2, 3, 4, 5]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print("Even/Odd Labels:", labels)
# Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']


print("\n--- 7. When NOT to Use List Comprehension (Loop is Better) ---")
numbers = [1, 2, 3, 4, 5]
result = []

for n in numbers:
    if n % 2 == 0:
        result.append(n * n)
        print(f"Processed {n}")  # side-effect (logging)

print("Result using loop:", result)
# Output:
# Processed 2
# Processed 4
# Result using loop: [4, 16]


print("\n--- 8. Generator Expression (Memory Efficient) ---")
gen = (n * n for n in range(5))
print("Generator Output:", list(gen))
# Output: [0, 1, 4, 9, 16]


print("\n--- SUMMARY ---")
print("""
✔ Use list comprehensions when:
- Logic is simple and readable
- You need to create a new list
- You are transforming or filtering data

❌ Avoid list comprehensions when:
- Logic is complex
- Debugging or logging is required
- Side effects are involved
""")

# 9. Performance  comparison: list comprehension vs loop
import time

start = time.perf_counter()
squares_loop = []
for x in range(10**6):
    squares_loop.append(x**2)
end = time.perf_counter()
print("Loop time:", end - start)

start = time.perf_counter()
squares_comp = [x**2 for x in range(10**6)]
end = time.perf_counter()
print("List comprehension time:", end - start)
 
# 2
import time 

# using a for loop
start = time.time()
squares_loop = []
for x in range(10**6):
    squares_loop.append(x**2)
print("Loop time : ", time.time() - start)

# using list Comprehension
start = time.time()
squares_comp = [x**2 for x in range(10**6)]
print("list Comprehension time : ", time.time() - start)




# Lambda function

# 1. Simple lambda function 

square = lambda x: x**2
print(square(5))

# 2.1 Using map() with lambda
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared) # output: [1, 4, 9, 16]

# 2.2 Using filter() with lambda
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

# 2.3  Using reduce() with lambda
from functools import reduce

numbers = [1, 2, 3, 4]

product = reduce(lambda x, y: x * y, numbers)

print(product) # output: 24

# 3. Lambda with Multiple Arguments
# 3.1 adding a Two Numbers 
add = lambda x, y : x + y
print(add(3,7)) # output: 10

# 3.2 # Finding the Maximum of Two numbers
maximum = lambda x,y : x if x>y else y
print(maximum(10,5)) # output: 10

# min = lambda x,y : y if x>y else x
# print(min(10,5))  # output: 5
 
# 4. Sorting a list tuples
student = [("RC", 100), ("AJ", 100), ("MJ", 80)]
student.sort(key=lambda student: student[1])  # Sort by score
print(student) # output: [('MJ', 80), ('RC', 100), ('AJ', 100)]

# descending order
student.sort(key=lambda student: student[1], reverse=True)
print(student) # output: [('RC', 100), ('AJ', 100), ('MJ', 80)]

'''

