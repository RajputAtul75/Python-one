letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''

#Use replace function to replace the name
print(letter.replace("<|Name|>", "Atul").replace("<|Date|>", "16-Feb-2025"))
