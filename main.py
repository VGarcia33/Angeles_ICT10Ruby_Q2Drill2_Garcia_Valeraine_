from pyscript import document, display

group_A = {"Thomas Greene", "Newt Isaac", "Minho Park", "Brenda Alcazar"}
group_B = {"Aris Jones", "Lizzy Isaac", "Harriet Tubman"}
group_C = {"Chuck Darwin", "Toby Frypan", "Winston Churchill"}
group_D = {"Alby Einstein", "Gally Galilei", "Teresa Agnes"}

group_all = group_A.union(group_B, group_C, group_D)

def all_groups(event):    
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()


    full_name = first_name + " " + last_name


group_all.add(full_name)

    document.getElementById("message").innerHTML = f"{', '.join(group_all)}