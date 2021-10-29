#import lostrommel
#import Vergleicher
#import Tippschein
import eingabe
import ausgabe
import spiel

spiel.Ausspielung(eingabe.Tastatur(), ausgabe.Html())
spiel.Ausspielung(eingabe.Datei("Tippschein.json"), ausgabe.Htm()).ausfuehrung()
