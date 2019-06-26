from hcat import simpSet
import pickle



s = simpSet(label = "test" )
print(s.label)
s.add(1, label = "testSimp")
print([simp.label for simp in s.rawSimps])

with open("save/test.golog", mode = 'wb') as file:
    pickle.dump(s, file)

with open("save/test.golog", mode = 'rb') as file:
    l = pickle.load(file)

print(l.label)
print([simp.label for simp in l.rawSimps])