# first we will take input of what nominee what we want to keep
nominee1 = input("Enter the name of the 1st nominee: ")
nominee2 = input("Enter the name of the 2nd nominee: ")

# initially vote count for both must be 0
nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

voter = int(input("Enter your voter id : "))
if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter) # we will remove so that agin same voter can't vote



