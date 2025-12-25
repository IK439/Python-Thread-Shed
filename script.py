'''A long string with plenty of messy sales data that contains
customer names, sale totals, types of thread purchased, and transaction dates'''

daily_sales = \
'''Alice Thornton   ;,;£1.21   ;,;   orange ;,; 
09/15/17   ,Michael Nguyen   ;,;   £7.29;,; 
orange&teal;,;   09/15/17 ,Daniel Foster ;,;£12.52 
;,;   orange&teal ;,; 09/15/17 ,Nora Bennett   
;,;   £5.13   ;,; orange   ;,; 09/15/17,
Carlos Ramirez   ;,;£20.39;,; orange&pink 
;,;09/15/17   ,   Brian Oconnor;,;£30.82;,;   
brown ;,;09/15/17 ,Laura Mendoza;,; £1.85   ;,; 
brown&pink ;,;09/15/17,   Kevin Turner;,; 
£17.98;,;brown&pink ;,; 09/15/17 , 
Jason Miller ;,;£17.41;,; cyan ;,; 09/15/17, 
Amanda Price ;,;£28.59;,; cyan;,;   09/15/17   , 
Peter Lawson;,; £14.51;,;   brown&cyan   ;,;   
09/15/17   , Olivia Simmons   ;,; £19.64 ;,; 
orange;,;09/15/17   ,   Ethan Moore ;,; £11.40   
;,; orange&maroon   ;,; 09/15/17, Scott Reynolds;,; 
£8.79 ;,; orange&teal&maroon   ;,;09/15/17   , Diane Porter;,; £8.65 ;,;cyan   ;,; 09/15/17,   Robert Ellis ;,;   £10.53;,;   lime&cyan   ;,; 
09/15/17   ,   Thomas Reed;,;   £16.49;,; 
lime&cyan&maroon   ;,;   09/15/17 ,Helen Watkins 
;,; £6.55 ;,;   lime&cyan&maroon;,;   09/15/17 ,
Marcus Coleman;,;   £11.86   ;,;navy;,;  
09/15/17,   Paula Grant   ;,;   £22.29 ;,;  
navy&pink ;,;09/15/17 , Victor Scott   ;,;   
£8.35;,;   orange&navy&pink   ;,;   09/15/17,   
Kelly Adams;,;£2.91 ;,;   orange&navy&pink   
;,;09/15/17, Sean Wallace ;,;£22.94;,;lime 
;,;09/15/17,Leonard Price;,;£4.70   ;,; lime&pink 
;,; 09/15/17   ,Frank Owens;,;   £3.59   
;,;lime&pink&cyan;,;   09/15/17   , Anthony Parker  ;,;£5.66   ;,; lime&pink&violet&cyan 
;,;   09/15/17 , Luis Collins   ;,;£17.51   ;,;   
navy   ;,;   09/15/17 , Emily Patterson ;,; 
£5.54;,;navy&cyan   ;,;09/15/17 ,Ruth Johnson ;,; 
£17.13;,; navy&cyan;,;   09/15/17,   Mark Benson;,;   £21.13 ;,;navy ;,;09/15/17 ,Nina Cooper;,; £0.35   ;,; navy&violet;,;   09/15/17   ,
Diego Flores ;,; £13.91   ;,;   navy&violet ;,;   
09/15/17,   Monica Ruiz   ;,;£19.26   ;,; 
pink;,; 09/15/17   , Tyler Brooks;,; £5.45;,;   
pink&maroon ;,;09/15/17 ,   Andrew Collins ;,;£5.50   
;,;   pink;,;   09/15/17, Miguel Torres   ;,; 
£14.56 ;,;   pink&cyan;,;09/15/17 , Clara Nielsen;,;   £7.33   ;,;   pink&cyan&maroon
;,; 09/15/17   ,   Paul Mitchell   ;,; £20.22   ;,; 
navy ;,;   09/15/17 ,   Irene Fox   ;,; £8.67   
;,;navy&maroon  ;,; 09/15/17 ,Connor Fitzgerald ;,;   
£8.31;,;   navy&maroon ;,;   09/15/17,   Melissa Grant 
;,;   £15.70   ;,;   orange&navy&maroon ;,;09/15/17   
,   Rebecca Hill   ;,;   £6.74   ;,;pink   ;,; 
09/15/17 , Vanessa Kelly ;,;   £30.84   
;,;pink&navy;,;   09/15/17 , Hannah Schultz   ;,; 
£12.31 ;,; lime&pink&navy;,;   09/15/17 ,
Kevin Martin;,;£2.94 ;,; pink ;,; 09/15/17 
,Aaron Phillips ;,; £22.46   ;,;orange&pink ;,;   
09/15/17,   Susan Turner ;,;   £6.60;,;   
orange&pink&navy ;,;09/15/17   ,   Patrick Nolan   
;,;   £6.27 ;,; pink   ;,;09/15/17 ,Sofia Alvarez ;,;£21.12   ;,; pink;,; 09/15/17   , 
Jasmine Wright ;,;£2.10   ;,;orange;,; 09/15/17  
,Linda Perry ;,; £14.22 ;,;orange&navy;,;   
09/15/17, Marisol Vega;,;£11.60;,;orange&navy   
;,;   09/15/17   ,   Corey Daniels   ;,; £25.27   ;,; 
orange&navy&maroon ;,;09/15/17   ,   Victor Lane   
;,;£8.26;,;   brown;,; 09/15/17 ,   Pauline Roberts 
;,;   £30.80 ;,;   brown&pink   ;,; 09/15/17   , 
Chloe Martin;,;   £22.61   ;,;   brown&pink   
;,;09/15/17,Denise Howard;,;£22.19 ;,; 
lime&brown&pink ;,;09/15/17   ,Bruce Kim 
;,; £7.47   ;,; maroon ;,; 09/15/17 , Julia Roberts;,;£5.49 ;,; pink&maroon ;,;   09/15/17   ,
Darius Coleman ;,;   £23.70  ;,;lime&pink&maroon 
;,; 09/15/17 ,   Nicole Fischer ;,; £26.66 ;,; 
maroon   ;,;09/15/17 ,Elena Cruz ;,; £25.95;,; 
lime&maroon ;,;   09/15/17   ,Harold Stone 
;,;£19.55 ;,; lime&orange&maroon ;,;   09/15/17 ,Victor Young;,;   £15.68;,;   orange ;,;   09/15/17 , Alicia Moreno ;,;£23.57;,;   orange&maroon   ;,;09/15/17, 
Florence Baker   ;,;£29.32;,; brown;,;09/15/17 ,Steven Kaplan   ;,; £26.44 ;,;   brown   ;,; 09/15/17, 
Alex Porter   ;,; £17.24;,;lime ;,; 09/15/17   , 
Lucas Brown ;,;   £8.49   ;,;lime   ;,;09/15/17   
,Maria Stein ;,;£13.10 ;,;lime;,;   09/15/17 ,   Colin Wright;,;£20.39 ;,; maroon   ;,; 09/15/17 ,
Rafael Ortiz;,;£14.70   ;,; orange&maroon ;,;09/15/17 
, Eleanor Shaw ;,;£22.45   ;,;orange&violet&maroon 
;,;   09/15/17, Calvin Brooks   ;,;   £28.46   ;,;   
maroon;,;   09/15/17 ,   Henry Turner ;,; £23.89;,;   
navy&maroon;,; 09/15/17,   Mateo Brooks   ;,;   
£24.49   ;,; navy&maroon ;,; 09/15/17   , Philip Grant ;,;£1.81;,;   navy&maroon ;,; 09/15/17 ,   
Samuel Reed;,; £6.81   ;,;lime;,;   09/15/17   
,   Paula Norton ;,;£0.65;,; lime&pink;,; 
09/15/17 , Benjamin Scott   ;,;£26.45;,; 
lime&pink&cyan   ;,;   09/15/17,   Gordon Price 
;,;   £7.69 ;,; brown;,; 09/15/17,Carol Edwards   
;,;£8.74   ;,; brown&navy   ;,;09/15/17 ,  
Pablo Reyes ;,;   £1.86   ;,;pink  
;,;09/15/17,Rosa Martinez;,;£14.75   ;,; pink;,;   
09/15/17   ,Patricia Long ;,; £28.10  ;,; 
pink&cyan;,;   09/15/17   , Quincy Hall   ;,; 
£9.91   ;,; lime ;,;09/15/17   ,Martin Vega;,; 
£16.34 ;,; lime ;,;   09/15/17,   Nelson Cruz 
;,;£27.57;,; orange;,;   09/15/17   , Tomas Kelly;,;£5.25;,; orange&cyan   ;,;   09/15/17 ,   
Andres Molina;,; £9.51;,;   orange&navy&cyan   
;,;   09/15/17   ,   Bethany Cook ;,;£20.56 ;,; 
lime;,;   09/15/17,Simon Clarke;,; £21.64   ;,;   
lime&pink;,;09/15/17,Hector Silva ;,;   
£24.99   ;,;   lime&pink&navy;,; 09/15/17 ,   
Justin Howard ;,;£29.70;,; lime ;,; 09/15/17 
,Sofia Rios;,;   £15.52;,;lime;,;   09/15/17 
, Daniela Brooks;,;£15.70 ;,; lime&violet;,; 
09/15/17 ,   Victor Ramirez ;,; £12.36 ;,;lime ;,; 
09/15/17,Nathan Price;,;   £13.66   ;,;   
lime&orange;,;09/15/17,   Marcia Bennett   ;,;£30.52   
;,; lime&orange&cyan   ;,; 09/15/17 , Agnes Turner 
;,;   £22.66   ;,; lime&orange&cyan;,;09/15/17'''

# Replace instances of ;,; and split at commas to separate transactions
daily_transactions = daily_sales.replace(';,;', '|').split(',')

# Initialize objects to store transaction details
customers = []
sales = []
thread_sold_split = []
total_sales = 0

# Loop through transactions stripping newlines/whitespaces and splitting at |
# Append transaction parts to objects
for transaction in daily_transactions:
  
    # Strip newlines/whitespaces and split at |
    transaction_parts = [part.strip().replace("\n", "") for part in transaction.split('|')]
    
    if len(transaction_parts) < 3:
        continue

    customer, sale, threads = transaction_parts[0], transaction_parts[1], transaction_parts[2]
    
    customers.append(customer)
    sales.append(sale)
    total_sales += float(sale.strip("£"))
    thread_sold_split.extend(thread.strip() for thread in threads.split("&"))

# Function to count how many threads of a specific colour were sold
def colour_count(colour):
    return sum(1 for thread_colour in thread_sold_split if thread_colour == colour)

# Test function
print(colour_count("pink"))

# Get distinct colours to count
distinct_colours = list(set(thread_sold_split))

# Loop through colours and print how many threads of each colour were sold
for colour in distinct_colours:
    print("\n"+"Thread Shed sold {0} threads of {1} thread today.".format(colour_count(colour), colour))

# Print total sales for verification
print("\n"+"Total sales: £{0:.2f}".format(total_sales))