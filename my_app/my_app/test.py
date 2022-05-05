from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    schedule = [
        {
        'Contract Executed Date' : 'Nov 12, 2021',
        'Kickoff Date' : 'Feb 07, 2022',
        'Spec Sign Off' : 'Mar 04, 2022',
        'Smoke Testing Start' : 'Mar 07, 2022',    
        'Smoke Testing Complete' : 'Mar 11, 2022',
        'Validation Start' : 'Mar 14, 2022',    
        'Validation Complete' : 'Apr 01, 2022',
        'UAT Start' : 'Apr 04, 2022',    
        'UAT Complete' : 'Apr 08, 2022',
        'GoLive' : 'Apr 15, 2022',    
        'FPI' : '',
        'Start date' : 'Feb 07, 2022',    
        'End date' : 'Apr 15, 2022',       
        },
        {
        'Contract Executed Date' : '',
        'Kickoff Date' :'',
        'Spec Sign Off' :'',
        'Smoke Testing Start' :'',    
        'Smoke Testing Complete' :'',
        'Validation Start' :'',    
        'Validation Complete' :'',
        'UAT Start' :'',    
        'UAT Complete' :'',
        'GoLive' :'',    
        'FPI' :'',
        'Start date' :'',    
        'End date' :'',       
        },
        {
        'Nov 12, 2021' : '',
        'Feb 07, 2022' : '',
        'Mar 04, 2022' : '',
        'Mar 07, 2022' : '',    
        'Mar 11, 2022' : '',
        'Mar 14, 2022' : '',    
        'Apr 01, 2022' : '',
        'Apr 04, 2022' : '',    
        'Apr 08, 2022' : '',
        'Apr 15, 2022' : '',    
        '' : '',
        'Feb 07, 2022' : '',    
        'Apr 15, 2022' : '',      
        }
    
        

       
    ]

    return JsonResponse({'schedule' : schedule})