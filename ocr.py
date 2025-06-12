from importnb import Notebook

with Notebook():
    from notebooks.ocr import get_invoice_data

if __name__ == "__main__":
    output = get_invoice_data(r"data\Invoices\3.jpg")
    
    print(output)
    
