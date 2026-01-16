class room:
   
    def show_details(self):
        return f"details of room"
    
    def show_room(self):
        return f"Room is spacious"
    
    def show_cupboards(self):
        return f"cupboards are beautiful"

r1=room()
print(r1.show_details())   
print(r1.show_room())
print(r1.show_cupboards())
