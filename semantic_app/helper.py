from models import DrugSales, DrugReview


def fetch_sales(year, drug_type):

    sales = DrugSales.objects.get(year=year, drug_type=drug_type)
    output = sales.objects.values('name').order_by('name').annotate(total_sales=sum('sales'))
    format_value = []
    for i in output:
        format_value.append(i.__dict__)
    
    return format_value


drugs = ['m01ab','m01ae','n02ba','n02be','n05b','n05c','r03','r06'] 
def create_sales_entries():
    with open('PharmaSales.csv', 'r') as file:
        drug = csv.DictReader(file)
        for row in drug:
            for i in range(6):
                drug_type = ''
                if i < 2:
                    drug_type =  'M'
                elif i < 5:
                    drug_type = 'N'
                else:
                    drug_type = 'R'
                
                day = str(row[datum])[8:]
                month = str(row[datum])[5:7]
                DrugSales.objects.create(name=drugs[i], drug_type=drug_type, day=int(day), month=int(month), year=row['year'], sales=row[drugs[i]])
