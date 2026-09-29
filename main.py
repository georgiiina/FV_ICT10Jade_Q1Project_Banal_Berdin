from pyscript import document, display

def show_main(e):
    document.getElementById("page1").classList.add("active")
    document.getElementById("page2").classList.remove("active")

def create_order(e):
    # gets all the elements
    prod1 = document.getElementById("prod1")
    prod2 = document.getElementById("prod2")
    prod3 = document.getElementById("prod3")
    prod4 = document.getElementById("prod4")
    prod5 = document.getElementById("prod5")
    
    # elements for sizes
    regular = document.getElementById("regular")
    large = document.getElementById("large")

    # elements for add-ons
    addon1 = document.getElementById("addon1")
    addon2 = document.getElementById("addon2")
    addon3 = document.getElementById("addon3")

     # elements for bar menu
    bar1 = document.getElementById("bar1")
    bar2 = document.getElementById("bar2")
    bar3 = document.getElementById("bar3")


    # calculates the subtotal using boolean multiplication

    subtotal = (float(prod1.value) * prod1.checked
    + float(prod2.value) * prod2.checked +
    float(prod3.value) * prod3.checked +
    float(prod4.value) * prod4.checked +    
    float(prod5.value) * prod5.checked +
    float(regular.value) * regular.checked +
    float(large.value) * large.checked +
    float(addon1.value) * addon1.checked +
    float(addon2.value) * addon2.checked +
    float(addon3.value) * addon3.checked +
    float(bar1.value) * bar1.checked + 
    float(bar2.value) * bar2.checked + 
    float(bar3.value) * bar3.checked)
    

# The tax calculation
    tax_rate = 0.12  # 12% because its the standard
    tax = subtotal * tax_rate
    grand_total = subtotal + tax

    # clears the output area
    document.getElementById("output1").innerHTML = ""

    # used what the teacher provided in the vn
    display(f"Subtotal: ₱{subtotal:.2f}", target="output1")
    display(f"Tax: ₱{tax:.2f}", target="output1", append=True)
    display(f"Total: ₱{grand_total:.2f}", target="output1", append=True)
    display("Thank you for your order!", target="output1", append=True)
    
def show_SKU(e):
    #variables derived from ids of inputs
    categ = document.getElementById("category").value
    prodnam = document.getElementById("productname").value
    stoc = document.getElementById("stock_qty").value
    
    #collects the first three letters of the catergory, the first four of the provided product, and the stock in string form
    sku_container = categ[:3].upper() + "-" + prodnam[:4].upper() + "-" + str(stoc)
    #prevents previous input from being saved
    document.getElementById('output1').innerHTML = ""
    #displays final calculated SKU
    display(sku_container, target="output1")

references: 
