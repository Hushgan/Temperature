const int LM35 = A0; // Constante pour définir l'entrée analogique/numérique pour brancher le capteur LM35

#include <Wire.h>

// Fonction d’initialisation parcourue une seule fois
void setup()
{
  // Initialisation de la liaison serie
  Serial.begin(9600); 
  
} // fin setup
//------------------------------------------------------------
// Fonction Principale parcourue en boucle
//------------------------------------------------------------

void loop()
{ 
  float TC; // Pour afficher la valeur de la température
  int N; // pour stocker la valeur numérisée 
  N = analogRead(LM35); // lecture du capteur LM35
  TC = N*5.0/1023*100 ;  // calcul de TC en degres Celsius.
  //Envoie sur la liaison série:
  Serial.println(TC);
  delay(5000);
     
} //fin loop
