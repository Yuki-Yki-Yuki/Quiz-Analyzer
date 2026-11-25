scores = []
choice = 0

for i in range(1,6):
    score = int(input(f"Enter your score for round {i}: "))
    if 0 <= score <= 10:
        scores.append(score)
    else:
        print("Invalid score. Please enter a score from 0 to 10.")

backup = scores.copy()
print(f"Scores: {scores}")
print(f"Backup successfully created.")
print(f"Your choices to choose from:")
print(f"1. Display Scores \n2. Add Score \n3. Insert Score \n4. Remove score \n5. Remove last score \n6. Search Score \n7. Generate Statistics \n8. Sort Score \n9. Reverse Scores \n10. Clear Scores \n11. Restore Original Scores \n12. Exit ")
while choice != 12:
    choice = int(input(f"Enter your choice: "))
    if choice == 1:
        print(f"Scores: {scores}")
    elif choice == 2:
        add = int(input("Enter score to add: "))
        if 0 <= add <= 10:
            scores.append(add)
            print(f'Updated scores: {scores}')
        else:
            print("Invalid score. Please enter a score from 0 to 10.")
            add = int(input("Enter score to add: "))
            scores.append(add)
            print(f'Updated scores: {scores}')
    elif choice == 3:
        insert = int(input("Enter score to insert: "))
        if 0 <= insert <= 10:
            scores.insert(0, insert)
            print(f'Updated scores: {scores}')
        else:
            print("Invalid score. Please enter a score from 0 to 10.")
            insert = int(input("Enter score to insert: "))
            scores.insert(0, insert)
            print(f"Updated score: {scores}")
    elif choice == 4:
        removed = int(input("Enter score to remove: "))
        if removed in scores:
            scores.remove(removed)
            print(f"Removed score: {scores}")
        else:
            print("No such score exists.")
            removed = int(input("Enter score to remove: "))
            scores.remove(removed)
            print(f"Removed score: {scores}")
    elif choice == 5:
        print(f"Last score removed: {scores.pop()} ")
    elif choice == 6:
        search = int(input("Enter score to search: "))
        if search in scores:
            print(f"Number of occurrences: {scores.count(search)}")
            print(f"First Index: {scores.index(search)}")
        else:
            print("No such score exists.")
            search = int(input("Enter score to search: "))
            print(f"Number of occurrences: {scores.count(search)}")
            print(f"First Index: {scores.index(search)}")
    elif choice == 7:
        print(f"===== SCORE STATISTICS =====")
        print(f"Score: {scores}")
        print(f"Number of scores: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores):.2f}")
        print(f"Highest score: {max(scores)}")
        print(f"Lowest score: {min(scores)}")
    elif choice == 8:
        print('[A] Ascending\n[D] Descending')
        sorting = input('Enter sorting order: ').upper().strip()
        if sorting == "A":
            scores.sort()
            print(f"Sorted score: {scores}")
        elif sorting == "D":
            scores.sort(reverse=True)
            print(f"Sorted score: {scores}")
        else:
            print("A or D only.")
    elif choice == 9:
        scores.reverse()
        print(f"The scores order has been reversed.")
    elif choice == 10:
        scores.clear()
        print(f"The scores have been cleared.")
        print(f"Current score: {scores}")
    elif choice == 11:
        print(f"Original score successfully restored.")
        print(f"Current score: {backup}")
    elif choice == 12:
        print("Thank you for using the system.")
        break
