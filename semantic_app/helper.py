from models import DrugSales,DrugReview


def querySingle(sql):
    try:
        cursor = cnx.cursor()
        cursor.execute(sql)
        for row in cursor:
            return dict((column[0],row[index]) for index, column in enumerate(cursor.description))
        return {}
    finally:
        cursor.close()


def fetch_sales(year, drug_type):

    sales = DrugSales.objects.get(year=year, drug_type=drug_type)
    output = sales.objects.values('name').order_by('name').annotate(total_sales=sum('sales'))