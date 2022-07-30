from models import DrugSales, DrugReview


def fetch_sales(year, drug_type):

    sales = DrugSales.objects.get(year=year, drug_type=drug_type)
    output = sales.objects.values('name').order_by('name').annotate(total_sales=sum('sales'))
    format_value = []
    for i in output:
        format_value.append(i.__dict__)
    
    return format_value