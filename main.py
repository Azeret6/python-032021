schoolMarks = [
  ["Jiří", 1, 4, 3, 2],
  ["Natálie", 2, 3, 4],
  ["Klára", 3, 2, 4, 1, 3]
]
vyber = int(input("Vyber číslo 0-2: "))

print(f"{schoolMarks[vyber][0]} dostal celkově {len(schoolMarks[vyber])-1} známek")
#print(f"První student(ka) v seznamu je {schoolMarks[0][0]}.")
#print(f"Její/jeho poslední známka je {schoolMarks[0][-1]}.")
