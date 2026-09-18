#NBAProspects.py

"""This program evaluates the backetball players's position
and statistics to decide what kind of draft they are apart of."""

position = input("Welcome to the NBA Draft Prospect Evaluator! \nEnter the player's position (guard, forward, or center):")


position = position.upper()

if position == "GUARD":
    points = float(input("Enter points per game: "))
    
    assists = float(input("Enter assists per game: "))
    
    three = float(input("Enter three-point percentage: "))
    
    if points >= 18:
        
        if assists >= 6:
        
            if three >= 38:
                print("SCOUNTING RESULT: LOTTERY PICK")
                
                
    if points >= 18:
        if assists >= 6:
            if three < 38:
                print("SCOUNTING RESULT: FIRST ROUND PROSPECT")
                
    if points >= 18:
        if assists < 6:
            print("SCOUNTING RESULT: SCORING SPECIALIST")
            
    if points < 18:
        if assists >= 7:
            print("SCOUNTING RESULT: PASS-FIRST PROSPECT")
            
    if points < 18:
        if assists < 7:
            print("SCOUNTING RESULT: NEEDS MORE DEVELOPMENT")
            
            
if position == "FORWARD":
    points = float(input("Enter points per game:"))
    
    rebounds = float(input("Enter rebounds per game: "))
    
    field = float(input("Enter field-goal percentage: "))
    
    if points >= 15:
        
        if rebounds >= 7:
        
            if field >= 50:
                print("SCOUNTING RESULT: LOTTERY PICK")
                
                
    if points >= 15:
        if rebounds >= 7:
            if field < 50:
                print("SCOUNTING RESULT: FIRST ROUND PROSPECT")
                
    if points >= 15:
        if rebounds < 7:
            print("SCOUNTING RESULT: OFFENSIVE SPECIALIST")
            
    if points < 15:
        if rebounds >= 9:
            print("SCOUNTING RESULT: DEFENSIVE/REBOUNDING PROSPECT")
            
    if points < 15:
        if rebounds < 9:
            print("SCOUNTING RESULT: NEEDS MORE DEVELOPMENT")
            
            
if position == "CENTER":
    rebounds = float(input("Enter rebounds per game:"))
    
    blocks = float(input("Enter blocks per game: "))
    
    field = float(input("Enter field-goal percentage: "))
    
    if rebounds >= 10:
        
        if blocks >= 2:
        
            if field >= 55:
                print("SCOUNTING RESULT: LOTTERY PICK")
                
                
    if rebounds >= 10:
        if blocks >= 2:
            if field < 55:
                print("SCOUNTING RESULT: FIRST ROUND PROSPECT")
                
    if rebounds >= 10:
        if blocks < 2:
            print("SCOUNTING RESULT: STRONG REBOUNDING PROSPECT")
            
    if rebounds < 10:
        if blocks >= 2.5:
            print("SCOUNTING RESULT: DEFENSIVE SPECIALIST")
            
    if rebounds < 10:
        if blocks < 2.5:
            print("SCOUNTING RESULT: NEEDS MORE DEVELOPMENT")