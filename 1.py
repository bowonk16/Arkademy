string = ""
bar = 1

x = int(input("Triangle :3"))

# Looping Baris
while bar <= x:
		kol = bar
		
		# Looping Kolom
		while kol > 0:
				string = string + "#"
				kol = kol - 1
				
		string = string + "\n"
		bar = bar + 1
print (string)
