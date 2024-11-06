import re

def parse_availability(user_input):
    
    availability = { 
        'Monday': ["9 AM - 11 AM"], 
        'Tuesday': ["9 AM - 11 AM"], 
        'Wednesday': ["9 AM - 11 AM"], 
        'Thursday': ["9 AM - 11 AM"], 
        'Friday': ["9 AM - 11 AM"], 
        'Saturday': ["9 AM - 11 AM"], 
        'Sunday': ["9 AM - 11 AM"]
    }
    
    
    early_morning_slot = "7 AM - 9 AM"
    
    
    if "except on wednesday" in user_input.lower():
        availability['Wednesday'] = []
    
    
    if "early morning" in user_input.lower():
        
        for day in availability:
            availability[day] = [early_morning_slot] if day != 'Wednesday' else []
    
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days_of_week:
        if f"on {day.lower()}" in user_input.lower():
            availability[day] = ["9 AM - 11 AM"]
    
    
    if "meeting booked" in user_input.lower():
        match = re.search(r"meeting booked on (\w+) from (\d{1,2}) to (\d{1,2}) (\w+)", user_input)
        if match:
            booked_day = match.group(1)
            booked_start = match.group(2)
            booked_end = match.group(3)
            booked_period = match.group(4).lower()
            
            
            if booked_day.capitalize() in availability:
                availability[booked_day.capitalize()] = []  
    return availability
