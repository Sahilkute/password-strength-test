import re
import hashlib
import string
import pyfiglet 


A =  pyfiglet.figlet_format("Password Strength Tester...")
print(A)

print(""" 
...................................................................................
                Author = Sahil Kute
                Github = https://github.com/Sahilkute
                Linkdin = www.linkedin.com/in/sahil-kute-83a797240/
...................................................................................
      """)


Pass = input(" Enter the password you have to check the strength : ")

class PasswordStrengthAssessor:
    def __init__(self):
        self.password_strength_levels = {
            "very_weak": 0,
            "weak": 1,
            "medium": 2,
            "strong": 3,
            "very_strong": 4
        }
        self.known_password_hashes = set()  

    def assess_password_strength(self, password):
        strength_score = 0

        # It will analysis the lenght of Password....
        if len(password) < 6:
            strength_score += self.password_strength_levels["very_weak"]
        elif len(password) < 10:
            strength_score += self.password_strength_levels["weak"]
        elif len(password) < 14:
            strength_score += self.password_strength_levels["medium"]
        else:
            strength_score += self.password_strength_levels["strong"]

        # It will analysis the Complexity of Password....
        if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"[0-9]", password) and re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
            strength_score += self.password_strength_levels["strong"]
        elif re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"[0-9]", password):
            strength_score += self.password_strength_levels["medium"]
        else:
            strength_score += self.password_strength_levels["weak"]

        # Uniqueness analysis (using hash) ...........
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if password_hash in self.known_password_hashes:
            strength_score -= self.password_strength_levels["very_weak"]
        else:
            self.known_password_hashes.add(password_hash)

        # Calculating the  overall strength score.......
        if strength_score < 2:
            return "very_weak"
        elif strength_score < 4:
            return "weak"
        elif strength_score < 6:
            return "medium"
        elif strength_score < 8:
            return "strong"
        else:
            return "very_strong"

    def get_password_strength_feedback(self, password):
        strength_level = self.assess_password_strength(password)
        feedback = {
            "very_weak": "Your password is very weak. Please use a stronger password.",
            "weak": "Your password is weak. Use more characters or special characters.",
            "medium": "Your password is medium strength. Great!",
            "strong": "Your password is strong. Excellent!",
            "very_strong": "Your password is very strong. It's Unbreakable!"
        }
        return feedback[strength_level]

# Example usage
assessor = PasswordStrengthAssessor()

passwords = [Pass]
for password in passwords:
    print(f"Password: {password}")
    print(f"Strength: {assessor.get_password_strength_feedback(password)}")
    print()
