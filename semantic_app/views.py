from django.shortcuts import render
from models import DrugSales, DrugReview
from django.core.exceptions import ObjectDoesNotExist
from semantic_app.helper import fetch_sales


class WebApiSalesView():

    def get(self, request):
        year = request.GET.get('year')
        drug_type = request.GET.get('drug_type')
        try:
            DrugSales.objects.all()
        except ObjectDoesNotExist:
            create_sales_entries()

        sales_current_year = fetch_sales(year=year, drug_type=drug_type)
        sales_previous_year = {}
        if year > 2014:
            sales_previous_year = fetch_sales(year=year-1, drug_type=drug_type)
            for iter in range(len(sales_current_year)):
                sales_current_year['previous_year_sales'] = sales_previous_year['sales']





