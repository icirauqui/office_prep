import pdfs

pdf_path = "data/Topper Industries I, LLC Terms and Conditions 0122.pdf"
word_path = "data/Charles Mitchell Clearwater 10x15 Aluminum Dock 0723.docx"        

yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;39m"

def main():
    pdf = pdfs.PDFQA(word_path)
    query = "Summarize the document"
    pdf.qa_history(query)
    #pdf.run()


if '__main__' == __name__:
    print(f"{yellow}-----------------------------------------------------------------------")
    print('Welcome to our QA system')
    print('-----------------------------------------------------------------------')


    main()