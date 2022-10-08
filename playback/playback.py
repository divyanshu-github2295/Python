def modify(sample):
    sample=sample.replace(" ","...")   # To replace particular character form String
    return sample

text=input("Enter anything? ")

print(modify(text))