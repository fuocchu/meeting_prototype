## Overview  
**TEST2** - This system is designed to help schedule a meeting for multiple users by considering their availability and constraints communicated through natural language input. The system processes user availability data, handles constraints such as time preferences and exclusions, and suggests common meeting times based on the overlap of user schedules.

![test2](https://github.com/user-attachments/assets/69a75372-f941-4591-8460-00bfd1a8d8c2)
[test2_meeting.webm](https://github.com/user-attachments/assets/70d20cd0-8755-4b90-a814-a541c8595b3e)

---

## Key Design Considerations

### **User Availability Input:**

**Decision:**  
The system accepts user availability in natural language format. This allows for flexibility and accommodates various ways people express their schedules.

**Reasoning:**  
Natural language input makes the system user-friendly, as users can input availability in a way that is natural and familiar to them (e.g., "I am free on Monday morning" or "I prefer early morning slots").

**Assumption:**  
The system assumes that users will provide their availability in simple, clear statements. Complex or ambiguous phrasing may need further refinement.

---

### **Parsing User Availability:**

**Decision:** A parser function (`parse_availability`) is used to extract and interpret the availability information from the user input.

**Reasoning:**  
Natural language processing (NLP) techniques such as keyword matching, regular expressions, and basic pattern recognition allow for extracting the necessary details (days, time slots, exclusions, etc.) from free-form text.

**Assumption:**  
The system assumes that common phrases (e.g., "except on Wednesday", "early morning", etc.) will be used to express preferences. It also assumes that there will be no highly ambiguous language, and complex time constraints (e.g., "every third Tuesday") are out of scope for this version.

---

### **Handling Different Time Preferences:**

**Decision:**  
The system recognizes time preferences such as "early morning", which translates to specific time slots like "7 AM - 9 AM".

**Reasoning:**  
Allowing users to express time preferences in natural language and mapping them to standard time slots helps streamline the process and avoid requiring users to manually input times.

**Assumption:**  
The system assumes that "morning" refers to 7 AM - 9 AM, and "afternoon" or other times will be provided explicitly if needed.

---

### **Exclusion of Specific Days:**

**Decision:**  
The system supports exclusions like "except on Wednesday" to handle user constraints and modify the availability accordingly.

**Reasoning:**  
Users often need to specify when they are unavailable. This feature ensures that the system respects these preferences and does not suggest meeting times on excluded days.

**Assumption:**  
It assumes that only simple exclusions are given (e.g., specific days) and that the system will not need to handle more complex exclusion patterns (e.g., "every other Friday").

---

### **Set Meetings:**

**Decision:**  
The system parses text such as "I already have a meeting booked on Friday from 2 to 4 PM" to mark specific times as unavailable.

**Reasoning:**  
This ensures that users' existing commitments are respected, preventing overlapping meeting suggestions.

**Assumption:**  
It assumes that booked meetings will be given in a predictable format (e.g., "from 2 PM to 4 PM") and that users will provide these constraints clearly.

---

### **Common Time Slot Calculation:**

**Decision:**  
The system calculates common available time slots across all users' schedules by finding overlapping time ranges.

**Reasoning:**  
The goal is to find the best time that works for all participants. The use of a common time calculation method ensures that the system suggests feasible meeting times.

**Assumption:**  
It assumes that each user has a clear and non-overlapping availability list after input parsing, and that time slots are compatible across users' schedules.
