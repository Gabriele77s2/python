# Initialize the candidate dictionary with candidate names as keys and initial vote counts as values
candidates = {
    "Candidate 1": 0,
    "Candidate 2": 0,
    "Candidate 3": 0,
}

def display_candidates():
    print("Candidates:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

def vote_for_candidate(candidate_name):
    if candidate_name in candidates:
        candidates[candidate_name] += 1
        print(f"You voted for {candidate_name}")
    else:
        print("Invalid candidate. Please choose a valid candidate.")

def main():
    print("Welcome to the Voting App!")
    
    while True:
        display_candidates()
        print("Type the name of the candidate you want to vote for (or 'exit' to quit):")
        user_input = input().strip().title()  # Capitalize the input for consistency
        
        if user_input == 'Exit':
            break
        else:
            vote_for_candidate(user_input)

    print("Thank you for voting!")
    display_candidates()

if __name__ == "__main__":
    main()

# We initialize a dictionary called candidates to store the candidate names and their initial vote counts (all set to 0).
# We define functions to display the candidates and to vote for a candidate.
# The vote_for_candidate function increments the vote count for the chosen candidate.
# The main function displays the list of candidates, allows the user to vote by typing the candidate's name (case-insensitive), and quits when the user types "exit."
# We run the main function if the script is executed directly.
