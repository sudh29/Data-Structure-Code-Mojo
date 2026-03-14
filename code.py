# # import json

# # # Task 1
# # def parse_categories():
# #     categories = []
# #     def get_categories_recursive(data):
# #         for item in data:
# #             if isinstance(item, list):
# #                 get_categories_recursive(item)
# #             else:
# #                 if item not in categories:
# #                     categories.append(item)

# #     with open('expected_categories.json') as f:
# #         data = json.load(f)
# #         get_categories_recursive(data)
# #     return categories

# # # Call the function
# # res = parse_categories()
# # print(res)


# import csv

# data_year = {}
# data_company = {}

# def read_csv(filename):
#     data = []
#     with open(filename, 'r') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             year = (row['year'])
#             revenue = (row[' revenue'])
#             company = (row[' company'])
#             data_year[year] = data_year.get(year,0) + int(revenue)
#             data_company[company] = data_company.get(company,0) + int(revenue)
#             data.append(row)
#     return data

# filename = r'C:\Users\91945\Documents\data.csv'
# csv_data = read_csv(filename)
# print(data_year)
# print()
# print(data_company)

# dic_data = {'Eka':5,'Dvi':6,'Tri':3,'Chatur':4}
# # print(csv_data)
# def projected_revenue(company_name, year):
#     if year>2030:
#         print('data not available beyond 2030')
#         return
    
    
# projected_revenue('eka', 2021 ) #= 135607.5
# projected_revenue('eka', 2025) #= 164831.76
# projected_revenue('dvi', 2023) #= 211717.39
# projected_revenue('tri', 2031)
    




# arr = [1,4,3,5]
# print(arr)
# n = len(arr)
# data_arr = [i for i in range(1,n+1)]
# print(data_arr)
# sum_arr = n*(n+1)/2
# input_arr_sum = sum(arr)
# diff  = input_arr_sum- sum_arr
# print(diff)

# '''
# Given an array arr[] of positive integers, the task is to find the minimum steps to reduce all the elements to 0. In a single step, -1 can be added to all the non-zero elements of the array at the same time.
# Examples: 
 

# Input: arr[] = {1, 5, 6} 
# Output: 6 
# Operation 1: arr[] = {0, 4, 5} 
# Operation 2: arr[] = {0, 3, 4} 
# Operation 3: arr[] = {0, 2, 3} 
# Operation 4: arr[] = {0, 1, 2} 
# Operation 5: arr[] = {0, 0, 1} 
# Operation 6: arr[] = {0, 0, 0}
# Input: arr[] = {1, 1} 
# Output: 1
# '''
# arr = [1, 5, 6]
# n=len(arr)
# # sum_ip = sum(arr)
# op_count = max(arr)

# # while arr.count(0) < n:
# #     arr = arr - [-1]*n
# #     print(arr)
# #     op_count += 1
# # print(op_count)

# arr = [1,2,3,3,4,5]
# n =len(arr)

# res = 0
# for i in range(1,n+1):
#     res = (arr[i] ^ i)
#     print(res)
#     if res!=0:
#         break










# arrival = [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
# departure = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]


# def min_platform(arr,dep):
#     n=len(arr)
#     arr.sort()
#     dep.sort()
#     i , j = 0,0
#     platforms_needed = 0
#     max_platforms = 0
#     print(arr)
#     print(dep)
#     while i < n and j < n:
#         if arrival[i] < departure[j]:
#             platforms_needed += 1
#             i += 1
#             max_platforms = max(max_platforms,platforms_needed)
#         else:
#             platforms_needed -= 1
#             j += 1
#     return max_platforms

# res = min_platform(arrival,departure)
# print(res)











'''1. API to find available menu items

A menu item ( eg: Dosa ) in a restaurant menu is available on a certain date or a certain weekday or a certain time of day. 
The objective of the application is to find available menu items for a given specific timestamp.

1. Write a GET API which sets the current_time to the cookie
2. Write a POST API that receives a CSV file containing menu items, along with available timings, excluded dates, and excluded days. Retrieve the current time from cookies
and return the available menu items as json
Sample Input :
itemname,available_timings,exclude_dates,exclude_days
Dosa,"16:00-21:00,07:00-10:00,10:45-12:00","20-03-2024, 25-03-2024","Monday, Friday"
'''



from flask import Flask, jsonify, request 
import requests
import datetime
import csv
 
FILE_PATH = r'C:\Users\91945\Documents\data2.csv'

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # print(row)
            itemname = row.get('itemname',None)
            available_timings = row.get('available_timings',None)
            exclude_dates = row.get('exclude_dates',None)
            exclude_days = row.get('exclude_days',None)
            # print(itemname,available_timings,exclude_dates,exclude_days)
    return itemname,available_timings,exclude_dates,exclude_days
  
app = Flask(__name__) 

@app.route('/', methods = ['GET']) 
def set_current_time(): 
    current_time = datetime.datetime.now()
    print(current_time)
    cookies =  jsonify({'current_time': current_time})
    url = ''
    r = requests.get(url, cookies=cookies)
    return 
  
@app.route('/Menu/', methods = ['POST']) 
def get_menu_data():
    itemname,available_timings,exclude_dates,exclude_days = read_csv(FILE_PATH)
    data = jsonify({'itemname': itemname, 'available_timings': available_timings, 'exclude_dates':exclude_dates , 'exclude_days':exclude_days}) 
    return data
    
  
if __name__ == '__main__': 
    app.run(debug = True) 




















