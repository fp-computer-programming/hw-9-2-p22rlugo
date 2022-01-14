# Ryan Lugo: RJL 1/14/22


last_initials = ["B.", "D.", "H.", "E.", "G.", "G.", "H.", "R.", "M.", "L.", "I.", "I.", "N.", "N.", "O.", "P.", "P.", "X.", "T.", "S.", "S.", "P."]

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin" "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]


def add_initial(table,initials):

    counter = 0
    ini_counter = 0

    if type(table) == list:
        while counter < len(rows):
            for i,v in enumerate(table[counter]):
                rows[counter][i] = v + " " + initials[ini_counter]
                ini_counter += 1
            counter += 1
        

    else:
        print(table,"is not a list.")
    return

add_initial(rows,last_initials)

print(rows)