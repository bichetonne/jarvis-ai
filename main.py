import os
import pyttsx3
from google import genai
from dotenv import load_dotenv

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Erreur : La clé API 'GEMINI_API_KEY' est introuvable. Vérifiez votre fichier .env.")
    exit(1)

# Initialisation du client Gemini et du moteur vocal
client = genai.Client(api_key=API_KEY)
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def parler(texte):
    """Fait parler Jarvis à haute voix et affiche le texte."""
    print(f"Jarvis : {texte}")
    engine.say(texte)
    engine.runAndWait()

def penser_et_repondre(prompt_utilisateur):
    """Envoie la requête à Gemini avec la personnalité de Jarvis."""
    try:
        system_instruction = (
            "Tu es Jarvis, un assistant virtuel intelligent, sophistiqué, courtois "
            "et fidèle, inspiré de l'univers d'Iron Man. Tu réponds de manière concise, "
            "élégante et efficace en français."
        )
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_utilisateur,
            config={
                'system_instruction': system_instruction,
            }
        )
        
        parler(response.text)
        
    except Exception as e:
        parler("Désolé monsieur, une erreur est survenue dans mes circuits.")
        print(f"Erreur technique : {e}")

if __name__ == "__main__":
    parler("Systèmes en ligne. Bonjour monsieur. Comment puis-je vous aider ?")
    
    while True:
        question = input("\nVous : ")
        
        if question.lower() in ["quitte", "quitter", "exit", "ferme-toi"]:
            parler("Très bien monsieur. Je me mets en veille.")
            break
            
        penser_et_repondre(question)