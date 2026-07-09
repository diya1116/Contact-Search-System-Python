📇 Python Contact Group Search System

This is a simple, text-based search application built using Python. The program connects to a database file containing 1,000 individual contact lists organized into multiple real-life categories like office, college, gym, family, friends, and vendors. It provides a clean terminal menu to look up where specific people are saved across these groups.

⭐ Features
1. Global Search: Type any name to search across all 1,000 lists and find exactly which groups that person belongs to.
2. Targeted Search: Look inside one specific list to check if a particular person is a member.
3. List Directory View: Enter the name of a group category to pull up and display all the contacts saved inside it.
4. Smart Text Matching: Automatically converts your searches to lowercase so names match perfectly even if you miss a capital letter.

🛠️ Code Structure
get_contact(contact): Scans the dynamic variables of the data file to find every list matching the person's name.
find_contact(contact, list_name): Targets a single specific group array to see if the contact is present.
get_list(list_name): Pulls up and prints the entire array layout for the requested group.
main_menu(): Runs an infinite loop terminal interface allowing the user to select options 1 within 4 options.

🚀 How to Run It

1. Make sure both your main script and your `contacts.py` data file are in the same folder.
2. Open your terminal inside that folder and run: python main.py
