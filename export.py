# Definiert eine Funktion mit Buchungsnummer und Quittungstext als Eingaben  
def save_receipt(booking_number, receipt_data):
    filename = f"receipt_{booking_number:03d}.txt"  # Erstellt den Dateinamen mit mindestens dreistelliger Buchungsnummer.
    with open(filename, "x") as receipt_file:     # Erstellt eine neue Datei. Bei vorhandenem Dateinamen gibt es einen Fehler.
        receipt_file.write(receipt_data)  # Schreibt den Quittungstext in die Datei.
    
    
save_receipt(1, "CinemaDesk\nBuchungsnummer: 1\n") # Ruft die Funktion mit Buchungsnummer 1 und einem Quittungstext zum Testen auf.
