class FlightTable:
    def _init_(self, data):
        self.data = data

    def search_by_team(self, team_name):
        matches = []
        for match in self.data:
            if team_name in (match['Team 01'], match['Team 02']):
                matches.append(match)
        return matches

    def search_by_location(self, location):
        matches = []
        for match in self.data:
            if location == match['Location']:
                matches.append(match)
        return matches

    def search_by_timing(self, timing):
        matches = []
        for match in self.data:
            if timing == match['Timing']:
                matches.append(match)
        return matches

    def print_matches(self, matches):
        if not matches:
            print("No matches found.")
            return
        print("Match Location\tTeam 01\t\tTeam 02\t\tTiming")
        for match in matches:
            print(f"{match['Location']}\t\t{match['Team 01']}\t{match['Team 02']}\t{match['Timing']}")


def main():
    data = [
        {'Location': 'Mumbai', 'Team 01': 'India', 'Team 02': 'Sri Lanka', 'Timing': 'DAY'},
        {'Location': 'Delhi', 'Team 01': 'England', 'Team 02': 'Australia', 'Timing': 'DAY-NIGHT'},
        {'Location': 'Chennai', 'Team 01': 'India', 'Team 02': 'South Africa', 'Timing': 'DAY'},
        {'Location': 'Indore', 'Team 01': 'England', 'Team 02': 'Sri Lanka', 'Timing': 'DAY-NIGHT'},
        {'Location': 'Mohali', 'Team 01': 'Australia', 'Team 02': 'South Africa', 'Timing': 'DAY-NIGHT'},
        {'Location': 'Delhi', 'Team 01': 'India', 'Team 02': 'Australia', 'Timing': 'DAY'}
    ]

    flight_table = FlightTable(data)

    while True:
        print("\nSearch options:")
        print("1. List of all matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            team_name = input("Enter Team name: ")
            matches = flight_table.search_by_team(team_name)
            flight_table.print_matches(matches)
        
        elif choice == 2:
            location = input("Enter Location: ")
            matches = flight_table.search_by_location(location)
            flight_table.print_matches(matches)
        
        elif choice == 3:
            timing = input("Enter Timing: ")
            matches = flight_table.search_by_timing(timing)
            flight_table.print_matches(matches)
        
        elif choice == 4:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")


if _name_ == "_main_":
    main()