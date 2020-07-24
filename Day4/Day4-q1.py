a=input("Enter the sentence:")
print("You Entered:",a)
w=input("Enter the word to find it occurence:")
res = [i for i in range(len(a)) if a.startswith(w, i)]
print("The indices of",w,"is:",res)

		
		