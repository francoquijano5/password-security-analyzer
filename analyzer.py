import re
import math

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Longitud básica
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Demasiado corta (mínimo 8-12 caracteres).")

    # 2. Mezcla de caracteres (RegEx)
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("⚠️ Falta mezclar mayúsculas y minúsculas.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ No contiene números.")

    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("⚠️ No contiene caracteres especiales.")

    # 3. Detección de patrones comunes
    common_patterns = ['123', 'qwerty', 'admin', 'password', 'hola']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        feedback.append("🚨 Contiene un patrón muy común y fácil de adivinar.")

    return score, feedback

if _name_ == "_main_":
    print("--- Analizador de Seguridad de Contraseñas ---")
    pwd = input("Introduce una contraseña para analizar: ")
    
    strength_score, tips = check_password_strength(pwd)
    
    print(f"\nPuntuación: {strength_score}/5")
    
    if strength_score >= 4:
        print("Resultado: ✅ CONTRASEÑA SEGURA")
    elif strength_score >= 2:
        print("Resultado: ⚠️ CONTRASEÑA MODERADA")
    else:
        print("Resultado: ❌ CONTRASEÑA INSEGURA")

    if tips:
        print("\nConsejos de mejora:")
        for tip in tips:
            print(tip)
