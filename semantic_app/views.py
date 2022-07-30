from models import DrugSales, DrugReview
from django.core.exceptions import ObjectDoesNotExist
from semantic_app.helper import fetch_sales
from django.http.response import JsonResponse
from rest_framework import status


class WebApiSalesView():

    def get(self, request):
        year = request.GET.get('year')
        drug_type = request.GET.get('drug_type')
        try:
            DrugSales.objects.all()
        except ObjectDoesNotExist:
            create_sales_entries()

        sales_details = fetch_sales(year=year, drug_type=drug_type)
        sales_previous_year = {}
        if year > 2014:
            sales_previous_year = fetch_sales(year=year-1, drug_type=drug_type)
            for iter in range(len(sales_details)):
                sales_details[0][iter]['previous_year_sales'] = sales_previous_year[0][iter]['sales']

        return JsonResponse(status=status.HTTP_200_OK, data=sales_current_year)





