# gst assingment 1
def calculateGST(price,gstRate):
    cgst = gstRate/2
    yield cgst
    sgst = gstRate/2
    yield sgst
    yield gstRate
def display(price,gst):
    gst = list(gst)
    # gst[0] : cgst
    # gst[1] : sgst
    # gst[2] : gstRate
    price_after_cgst = price + ((price*gst[0])/100)
    prince_after_sgst = price + (( price*gst[1])/100)
    total_price = price + ((price*gst[2])/100)

    print('''
    Actual Price of item : {}
    Price after CGST : {}
    Price after applying SGST : {}
    Total price with GST : {}
    '''.format(price,price_after_cgst,prince_after_sgst,total_price))

price = int(input("Enter Price of item : "))
gst_rate = int(input("Enter GST Rate: "))
gst = calculateGST(price= price, gstRate= gst_rate)
display(price=price, gst= gst)